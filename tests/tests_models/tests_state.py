#!/usr/bin/python3
"""
This is State class unittest module. This class tests State class.
"""
import unittest
import uuid
import datetime
from models.state import State


class TestState(unittest.TestCase):
    """
    Create object of State class for testing.
    """
    def setUp(self):
        self.test1 = State()
        self.test2 = State()

    """
    Test object attributes.
    """
    def test_attribute(self):
        self.assertTrue(hasattr(self.test1, "name"))
        self.assertFalse(hasattr(self.test2, "place"))
        self.assertTrue(type(self.test1.name) is str)
        self.assertTrue(type(self.test2.id) is str)
        self.assertTrue(self.test1.id != self.test2.id)
        test_created1 = self.test1.created_at
        test_created2 = self.test2.created_at
        self.assertTrue(test_created1 != test_created2)
        self.assertTrue(type(test_created2) is datetime.datetime)


if __name__ == '__main__':
    unittest.main()
