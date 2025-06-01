import os


MCP_PORT = int(os.getenv("MCP_PORT", "8000"))
STORAGE_PATH = os.getenv("STORAGE_PATH", "./storage")

POSTGRES_HOST = os.getenv("POSTGRES_HOST", "localhost")
POSTGRES_PORT = int(os.getenv("POSTGRES_PORT", "5432"))
POSTGRES_USERNAME = os.getenv("POSTGRES_USERNAME", "")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "")
POSTGRES_DATABASE = os.getenv("POSTGRES_DATABASE", "")
