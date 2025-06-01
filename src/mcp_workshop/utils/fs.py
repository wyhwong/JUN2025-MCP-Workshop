import logging
import os
from typing import Optional

from mcp_workshop import env


logger = logging.getLogger(__name__)


def create_folder(folder_name: str) -> str:
    """Create a folder in the filesystem."""

    folder_path = os.path.join(env.STORAGE_PATH, folder_name)

    if os.path.exists(folder_path):
        return f"Folder {folder_path} already exists."

    try:
        os.makedirs(folder_path)
        return f"Folder {folder_path} created successfully."

    except Exception as e:
        logger.error(f"Error creating folder {folder_path}: {e}")
        return f"Unknown error creating folder {folder_path}."


def list_folders() -> list[str]:
    """List all folders in the storage path."""

    if not os.path.exists(env.STORAGE_PATH):
        return []

    folders = [f.name for f in os.scandir(env.STORAGE_PATH) if f.is_dir()]
    return folders


def list_files(folder_name: Optional[str] = None) -> list[str]:
    """List all files in a given folder."""

    folder_path = os.path.join(env.STORAGE_PATH, folder_name)

    if not os.path.exists(folder_path):
        return []

    if not os.path.isdir(folder_path):
        return [f"{folder_name} is not a directory."]

    files = [f.name for f in os.scandir(folder_path) if f.is_file()]
    return files


def move_file(src_folder: str, dist_folder: str, file_name: str) -> str:
    """Move a file from one folder to another."""

    src_path = os.path.join(env.STORAGE_PATH, src_folder, file_name)
    dist_path = os.path.join(env.STORAGE_PATH, dist_folder, file_name)

    if not os.path.exists(src_path):
        return f"File {src_path} does not exist."

    if not os.path.exists(os.path.dirname(dist_path)):
        return f"Destination folder {dist_folder} does not exist."

    try:
        os.rename(src_path, dist_path)
        return f"File {file_name} moved from {src_folder} to {dist_folder} successfully."

    except Exception as e:
        logger.error(f"Error moving file {file_name}: {e}")
        return f"Unknown error moving file {file_name}."


def remove_file(file_path: str) -> str:
    """Remove a file from the filesystem."""

    if not os.path.exists(file_path):
        return f"File {file_path} does not exist."

    try:
        os.remove(file_path)
        return f"File {file_path} removed successfully."

    except Exception as e:
        logger.error(f"Error removing file {file_path}: {e}")
        return f"Unknown error removing file {file_path}."
