#!/usr/bin/python3
"""Initialization module for the models.engine package.

Contains modules related to the engine for managing models in the application

Modules:
    - file_storage:
            Implements a file-based storage system for Python objects.

Classes:
    - FileStorage:
            A class providing methods to store, retrieve, and manage objects.
"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
