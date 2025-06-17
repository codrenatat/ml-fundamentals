from mcp.server.fastmcp import FastMCP
from tools import get_current_price

# Crear servidor MCP
mcp = FastMCP(
    name="Stock Price MCP Server",
    host="0.0.0.0",
    port=8050,
)

@mcp.tool()
def get_current_price_tool(symbol: str) -> str:
    """
    Obtiene el precio actual de una acción desde Alpha Vantage API.
    
    Args:
        symbol: Símbolo de la acción (ej: AAPL, GOOGL, MSFT)
    
    Returns:
        Precio actual formateado con timestamp
    """
    try:
        return get_current_price(symbol)
    except Exception as e:
        return f"Error obteniendo precio de {symbol}: {str(e)}"

# Ejecutar servidor
if __name__ == "__main__":
    print("🚀 Iniciando Stock Price MCP Server...")
    print("📊 Herramienta disponible:")
    print("  - get_current_price_tool: Precio actual de acciones")
    print("🔌 Ejecutando con transporte stdio para LLM APIs...")
    mcp.run(transport="stdio")