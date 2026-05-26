import os
import sys
import datetime
import platform
import uvicorn
from fastmcp import FastMCP

# ---------------------------------------------------------------------------
# Server setup — endpoint MUST be /mcp for Natoma
# ---------------------------------------------------------------------------
mcp = FastMCP("natoma-python-mcp")
application = mcp.streamable_http_app(path="/mcp")


# ---------------------------------------------------------------------------
# Tool 1 — Echo
# ---------------------------------------------------------------------------
@mcp.tool()
def echo(message: str) -> str:
    """Return the input message unchanged. Useful for testing connectivity."""
    return message


# ---------------------------------------------------------------------------
# Tool 2 — Add two numbers
# ---------------------------------------------------------------------------
@mcp.tool()
def add(a: float, b: float) -> float:
    """Add two numbers and return the result."""
    return a + b


# ---------------------------------------------------------------------------
# Tool 3 — Current UTC time
# ---------------------------------------------------------------------------
@mcp.tool()
def get_time() -> str:
    """Return the current UTC date and time as an ISO-8601 string."""
    return datetime.datetime.utcnow().isoformat() + "Z"


# ---------------------------------------------------------------------------
# Tool 4 — Basic system info
# ---------------------------------------------------------------------------
@mcp.tool()
def system_info() -> dict:
    """Return OS name and Python version running this server."""
    return {
        "os": platform.system(),
        "os_version": platform.version(),
        "python": sys.version,
    }


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    port = int(os.getenv("PORT", 8080))
    uvicorn.run(
        application,
        host="0.0.0.0",
        port=port,
        proxy_headers=True,
        forwarded_allow_ips="*",
    )