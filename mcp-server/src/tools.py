import os
import requests
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

def get_current_price(symbol: str) -> str:
    """
    Obtiene el precio actual de una acción desde Alpha Vantage API.
    """
    apikey = os.getenv("ALPHA_VANTAGE_API_KEY")
    if not apikey:
        return "Error: ALPHA_VANTAGE_API_KEY no configurada"
    
    url = (
        "https://www.alphavantage.co/query"
        f"?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=5min&apikey={apikey}"
    )
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        # Verificar si hay error en la respuesta
        if "Error Message" in data:
            return f"Error: Símbolo {symbol} no válido"
        
        if "Note" in data:
            return "Error: Límite de API alcanzado. Intenta más tarde."
        
        if "Time Series (5min)" not in data:
            return f"Error: No se pudieron obtener datos para {symbol}"
        
        # Obtener precio más reciente
        time_series = data["Time Series (5min)"]
        latest_time = sorted(time_series.keys())[-1]
        latest_data = time_series[latest_time]
        latest_price = latest_data["4. close"]
        
        return f"💰 {symbol}: ${latest_price} (actualizado: {latest_time})"
        
    except requests.RequestException as e:
        return f"Error de conexión: {str(e)}"
    except Exception as e:
        return f"Error procesando datos: {str(e)}"