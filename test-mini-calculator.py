import unittest
from unittest import TestCase

from main import MyMiniCalculator


class TestMyMiniCalculator(unittest, TestCase):
    def test_add(self):
        add_object = MyMiniCalculator()
        self.assertEqual(add_object.add(1, 1), 2)
