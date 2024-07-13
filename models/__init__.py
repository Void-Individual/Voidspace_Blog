#!/usr/bin/python3
"""Init module with the storage function"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
