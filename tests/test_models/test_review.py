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
        self.assertTrue(hasattr(self.test2, "text"))
        self.assertTrue(type(self.test1.place_id) is str)
        self.assertTrue(type(self.test2.user_id) is str)
        self.assertTrue(type(self.test2.text) is str)
        self.assertTrue(type(self.test2.id) is str)
        self.assertTrue(self.test1.place_id != self.test1.id)
        test_created1 = self.test1.created_at
        test_created2 = self.test2.created_at
        self.assertIsNot(test_created1, test_created2)
        self.assertTrue(type(test_created2) is datetime.datetime)

    """
    Test inherited methods.
    """
    def test_save(self):
        test_updated = self.test1.updated_at
        self.test1.save()
        updated_save = self.test1.updated_at
        self.assertFalse(test_updated == updated_save)


if __name__ == '__main__':
    unittest.main()
