#!/usr/bin/python3
"""
Unittests for temp class
"""
import unittest
import models
from models.temperature import Temperature

class TestTemperature(unittest.TestCase):
    """
    Test cases for temp class
    """

    def test_initialization(self):
        """
        Test if temp object initializes correctly
        """
        temp = Temperature(100, 'C')
        self.assertEqual(temp.value, 100)
        self.assertEqual(temp.unit, "C")
    
    def test_str(self):
        """
        Test the str method
        """
        temp = Temperature(100, 'C')
        self.assertEqual(str(temp), '100 C')

    def test_convert_to_farenheit(self):
        """
        Tests if converting to same unit returns the same value
        """
        temp = Temperature(100, 'C')
        self.assertAlmostEqual(temp.convert_temp('F'), 212.0, places=1)