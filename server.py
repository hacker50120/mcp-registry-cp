import os
import uvicorn
from fastmcp import FastMCP

port = int(os.getenv("PORT", 8080))
mcp = FastMCP("MyCustomAgent")
application = mcp.streamable_http_app(path="/mcp")

@mcp.tool()
def hello(name: str) -> str:
    """Say hello to someone"""
    return f"Hello, {name}!"

if __name__ == "__main__":
    uvicorn.run(
        application,
        host="0.0.0.0",
        port=port,
        proxy_headers=True,
        forwarded_allow_ips="*"
    )
