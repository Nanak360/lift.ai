import os
from fastapi import UploadFile
from pathlib import Path

def save_and_get_file_path(file: UploadFile):
    file_path = Path("./uploads") / file.filename
    file_path.parent.mkdir(parents=True, exist_ok=True)
    with open(file_path, "wb") as buffer:
        buffer.write(file.file.read())
    return str(file_path)
