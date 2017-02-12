#!/usr/bin/python3
"""
This is the init package?

"""

from .engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
