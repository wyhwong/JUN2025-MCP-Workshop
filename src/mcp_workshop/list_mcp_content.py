from fastmcp import Client

from mcp_workshop import env


MCP_URL = f"http://localhost:{env.MCP_PORT}/sse"


async def main():
    async with Client(MCP_URL) as client:
        tools = await client.list_tools()
        print(f"Available tools: {tools}")

        print("-" * 20)

        resources = await client.list_resources()
        print(f"Available resources: {resources}")

        print("-" * 20)

        prompts = await client.list_prompts()
        print(f"Available prompts: {prompts}")


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
