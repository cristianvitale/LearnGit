'''
Created on 03/06/2013

@author: cristian.vitale
'''
import unittest
from calc.calculator import Calculator

class TestCalc(unittest.TestCase):
    
    def testAdd(self):
        calculator = Calculator()
        result = calculator.add(operanda=2, operandb=3)
        self.assertEqual(result, 5, "Addition failed")