#!/usr/bin/python3
import unittest
from models.base import Base


class TestBase_instantiation(unittest.TestCase):
    """ Unit tests for testing instantiation of my first class called Base"""

    def test_no_arg(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_3_bases(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b2.id, b3.id - 1)
        self.assertEqual(b1.id, b2.id - 1)

    def test_id_initialization(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base(12)
        b5 = Base()
        self.assertTrue(b1, self.id == 1)
        self.assertTrue(b2, self.id == 2)
        self.assertTrue(b3, self.id == 3)
        self.assertTrue(b4, self.id == 12)
        self.assertTrue(b5, self.id == 4)

    def test_2_id(self):
        Base._Base__nb_objects = 0
        base = Base()
        self.assertEqual(base.id, 1)
        b1 = Base(100)
        self.assertEqual(b1.id, 100)
        b2 = Base(-100)
        self.assertEqual(b2.id, -100)
        b3 = Base()
        self.assertEqual(b3.id, 2)
