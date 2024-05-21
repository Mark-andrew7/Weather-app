#!/usr/bin/python
"""
Holds the temp class
"""
from sqlalchemy import Column, Integer, Float, String


class Temperature():
    """
    Representation of temp
    """
    __tablename__ = 'temperatures'
    id = Column(Integer, primary_key=True, autoincrement=True)
    value = Column(Float, nullable=False)
    unit = Column(String(1), default='C')

    def __init__(self, value, unit='C'):
        self.value = value
        self.unit = unit

    def convert_temp(self, target_unit):
        """
        Converts from Celcius to Farenheit and viceversa
        """
        if self.unit == target_unit:
            return self.value
        elif self.unit == 'C' and target_unit == 'F':
            return self.value * 9 / 5 + 32
        elif self.unit == 'F' and target_unit == 'C':
            return (self.value - 32) * 5 / 9
        else:
            raise ValueError(f"Unsupported unit conversion from {self.unit} to {target_unit}")
        
    def __str__(self):
        """
        Returns both value and its unit
        """
        return f"{self.value} {self.unit}"