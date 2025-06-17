# Machine Learning Fundamentals

Este proyecto implementa un servidor utilizando el **Model Context Protocol (MCP)** en Python, que expone una herramienta para obtener el precio actual de acciones bursátiles a través de la API de [Alpha Vantage](https://www.alphavantage.co/). Está diseñado para integraciones con modelos LLM que soportan MCP.

---

## ⚙️ Requisitos

- Python 3.8 o superior
- Cuenta gratuita en [Alpha Vantage](https://www.alphavantage.co/support/#api-key) para obtener una API Key
- SDK de MCP para Python (`mcp-sdk`)

---

## Instalación

1. **Clona el repositorio**
2. **Crea un entorno virtual y activalo**
3. **Instala las dependencias**
pip install -r requirements.txt

## Configuración del entorno
1. **Crea un archivo .env en la raíz del proyecto usando .env.example como plantilla:**
   cp .env.example .env
2. **Crea un entorno virtual y activalo**
   ALPHA_VANTAGE_API_KEY=tu_api_key_aqui


