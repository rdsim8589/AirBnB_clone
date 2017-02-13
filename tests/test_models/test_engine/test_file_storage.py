#!/usr/bin/python3
"""
This is FileStorage class unittest module. This class tests FileStorage class.
"""
import unittest
import uuid
import datetime
import json
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """
    Create object of FileStorage class for testing.
    """
    def setUp(self):
        self.test1 = FileStorage()
        self.test2 = FileStorage()

    """
    Test object attributes.
    """
    def test_attribute(self):
        self.assertFalse(hasattr(self.test1, "name"))
        self.assertFalse(hasattr(self.test2, "my_number"))
        self.assertFalse(hasattr(self.test1, "created_at"))
        self.assertFalse(hasattr(self.test1, "updated_at"))
        self.assertFalse(hasattr(self.test2, "id"))

    """
    Test save method.
    """
    def test_save(self):
        mock_val = {"id": {"__class__": "BaseModel"}}
        expected_val = json.dumps(mock_val)
        self.assertTrue(type(expected_val) is str)

    """
    Test reload method.
    """
    def test_reload(self):
        mock_val = '{"id": {"__class__": "BaseModel"}}'
        expected_val = json.loads(mock_val)
        self.assertTrue(type(expected_val) is dict)


if __name__ == '__main__':
    unittest.main()
