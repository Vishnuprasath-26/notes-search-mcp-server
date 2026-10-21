
from pathlib import Path
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Notes Search MCP Server")

NOTES_FOLDER = Path(r"C:\Users\HP\Documents\MCP-Notes")


@mcp.tool()
def say_hello(name: str) -> str:
    return f"Hello, {name}! Welcome to MCP."


@mcp.tool()
def search_notes(query: str) -> str:
    if not query.strip():
        return "Please enter a search query."

    if not NOTES_FOLDER.is_dir():
        return f"Notes folder does not exist: {NOTES_FOLDER}"

    results = []

    for file_path in NOTES_FOLDER.rglob("*"):
        if not file_path.is_file():
            continue

        if file_path.suffix.lower() not in {".txt", ".md"}:
            continue

        try:
            with file_path.open("r", encoding="utf-8") as file:
                for line_number, line in enumerate(file, start=1):
                    if query.casefold() in line.casefold():
                        results.append(
                            f"{file_path.name}, line {line_number}: {line.strip()}"
                        )
        except (OSError, UnicodeError):
            continue

    if not results:
        return "No matching notes found."

    return "\n".join(results[:50])


@mcp.resource("notes://hello")
def read_hello_note() -> str:
    file_path = NOTES_FOLDER / "hello.txt"

    if not file_path.is_file():
        return "hello.txt was not found."

    try:
        return file_path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as error:
        return f"Unable to read hello.txt: {error}"


if __name__ == "__main__":
    mcp.run()
