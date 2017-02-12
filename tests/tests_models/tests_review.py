#!/usr/bin/python3
"""
This is Review class unittest module. This class tests Review class.
"""
import unittest
import uuid
import datetime
from models.review import Review


class TestReview(unittest.TestCase):
    """
    Create object of Review class for testing.
    """
    def setUp(self):
        self.test1 = Review()
        self.test2 = Review()

    """
    Test object attributes.
    """
    def test_attribute(self):
        self.assertTrue(hasattr(self.test1, "place_id"))
        self.assertFalse(hasattr(self.test2, "place"))
        self.assertTrue(hasattr(self.test2, "user_id"))
        self.assertTrue(type(self.test1.place_id) is str)
        self.assertTrue(type(self.test2.id) is str)
        self.assertTrue(self.test1.place_id != self.test1.id)
        test_created1 = self.test1.created_at
        test_created2 = self.test2.created_at
        self.assertTrue(test_created1 != test_created2)
        self.assertTrue(type(test_created2) is datetime.datetime)


if __name__ == '__main__':
    unittest.main()
