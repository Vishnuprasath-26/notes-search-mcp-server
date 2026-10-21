# Notes Search MCP Server

## 1. Project Overview

The Notes Search MCP Server is a Python application built using the Model Context Protocol (MCP). It allows MCP clients to search local notes and read note content through tools and resources.

## 2. Technologies Used

- Python 3.12
- MCP Python SDK
- FastMCP
- MCP Inspector

## 3. Features

### Say Hello

The `say_hello` tool accepts a name and returns a greeting.

Example:

Input: `Vishnu`

Output: `Hello, Vishnu! Welcome to MCP.`

### Search Notes

The `search_notes` tool searches `.txt` and `.md` files for a keyword and returns matching lines with line numbers.

### Read Note Resource

The `notes://hello` resource provides the contents of `hello.txt`.

## 4. Project Structure

```text
MCP/
├── tests/
│   └── test_hello_server.py
├── hello_server.py
├── requirements.txt
├── README.md
└── .gitignore
```

## 5. Installation

Create and activate a virtual environment:

```powershell
python -m venv .venv
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```powershell
python -m pip install -r requirements.txt
```

## 6. Run the Server

```powershell
python hello_server.py
```

The server uses STDIO transport and communicates with an MCP client.

## 7. Testing

Run the automated tests:

```powershell
python -m unittest discover -s .\tests -v
```

MCP Inspector can also be used to test the tools and the `notes://hello` resource.

## 8. Notes Folder

The notes folder path is configured in `hello_server.py`. Make sure the folder exists and contains `.txt` or `.md` files.
