from fastmcp import FastMCP

from mcp_workshop import env


INSTRUCTIONS = """
This server provides a simple interface to interact with file system and postgresDB.
Call get_image() to retrieve an image from the file system.
Call get_description() to retrieve a description from the database.
"""

mcp = FastMCP(name="AlbumAssistant", instructions=INSTRUCTIONS)


@mcp.tool()
def dummy_func(prompt: str) -> int:
    """Return "Hello, World!" anyway."""

    return "Hello, World!"


if __name__ == "__main__":
    mcp.run(transport="sse", port=env.MCP_PORT)
