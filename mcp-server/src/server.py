# Functions from the mcp python sdk 
from mcp.server.fastmcp import FastMCP
from tools import get_current_price

# Creating our MCP server
# Similar to FastAPI 
# If http specify port and host if not standart io 
mcp = FastMCP(
    name = "Alpha Vantage MCP Server",
    host = "0.0.0.0",   # Only used for SSE transport (localhost)
    port = 8050,    # Only used for SSE transport (set to any port)
)

@mcp.tool()
def get_current_price_tool(symbol: str) -> str:
    """
    Gets the current price of a stock from Alpha Vantage API.
    
    Args:
        symbol: Stock symbol (e.g.: AAPL, GOOGL, MSFT)
    
    Returns:
        Current price formatted with timestamp
    """
    try:
        return get_current_price(symbol)
    except Exception as e:
        return f"Error getting price for {symbol}: {str(e)}"

# Run the server
if __name__ == "__main__":
    transport = "sse"
    if transport == "stdio":
        print("Running mcp server with stdio transport")
        mcp.run(transport = "stdio")
    elif transport == "sse":
        print("Running server with SSE transport")
        mcp.run(transport = "sse")
    else:
        raise ValueError(f"Unknown transport: {transport}")
