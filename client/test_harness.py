import asyncio
import sys
from pathlib import Path

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

SERVER = (
    Path(__file__).resolve().parent.parent
    / "server"
    / "malicious_server.py"
)


async def main():
    params = StdioServerParameters(
        command=sys.executable,
        args=[str(SERVER)],
    )

    async with stdio_client(params) as (read, write):
        async with ClientSession(read, write) as session:

            await session.initialize()

            result = await session.list_tools()

            print("\nINITIAL TOOLS")
            print("=============")

            for tool in result.tools:
                print(f"{tool.name}: {tool.description}")

            for i in range(1, 5):
                result = await session.call_tool(
                    "format_text",
                    {"text": f"training call {i}"},
                )

                print(f"\nCALL {i}")

                for content in result.content:
                    print(content.text)

            await asyncio.sleep(1)

            result = await session.list_tools()

            print("\nUPDATED TOOLS")
            print("=============")

            for tool in result.tools:
                print(f"{tool.name}: {tool.description}")

            result = await session.call_tool(
                "format_text",
                {"text": "trigger simulated discovery"},
            )

            print("\nSIMULATED DISCOVERY")
            print("===================")

            for content in result.content:
                print(content.text)


if __name__ == "__main__":
    asyncio.run(main())
