#!/usr/bin/python3
"""
This is the init package?

"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
