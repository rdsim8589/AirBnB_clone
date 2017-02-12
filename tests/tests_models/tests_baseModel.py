#!/usr/bin/python3
"""
This is BaseModel class unittest module. This class tests BaseModel class.
"""
import unittest
import uuid
import datetime
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """
    Create object of BaseModel class for testing.
    """
    def setUp(self):
        self.test1 = BaseModel()
        self.test2 = BaseModel()

    """
    Test object attributes.
    """
    def test_attribute(self):
        self.assertFalse(hasattr(self.test1, "name"))
        self.assertFalse(hasattr(self.test2, "my_number"))
        self.test1.name = ""
        self.test2.my_number = 1
        self.assertTrue(hasattr(self.test1, "name"))
        self.assertTrue(type(self.test1.name) is str)
        self.assertTrue(hasattr(self.test2, "my_number"))
        self.assertTrue(type(self.test2.my_number) is int)
        self.assertTrue(hasattr(self.test2, "id"))
        self.assertTrue(type(self.test2.id) is str)
        self.assertTrue(self.test1.id != self.test2.id)
        test_created1 = self.test1.created_at
        test_created2 = self.test2.created_at
        self.assertTrue(test_created1 != test_created2)
        self.assertTrue(type(test_created2) is datetime.datetime)


if __name__ == '__main__':
    unittest.main()
