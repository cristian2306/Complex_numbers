# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 10:15:15 2020

@author: Cristian
"""


import unittest
import math
from complex_numbers import complex_number
from complex_numbers import complex_cart
from complex_numbers import complex_polar

class Test_complex(unittest.TestCase):
    
    def setUp(self):
        self.complex_a = complex_cart(1,2)
        self.complex_b = complex_cart(2,4)
        self.complex_c = complex_cart(-6,2)
        self.complex_d = complex_cart(-5,-8)
        self.complex_e = complex_cart(0,0)
        self.complex_f = complex_cart(1,1)
        self.complex_h = complex_cart(1/2,3/4)
        self.complex_A = complex_polar(8,(3*math.pi)/4)
        self.complex_B = complex_polar(3,(23*math.pi)/22)
        self.complex_C = complex_polar(24,(3*math.pi)/5)
        self.complex_D = complex_polar(4.47,1.11)
        
    def test_add(self):
        self.assertEqual(str(self.complex_a + self.complex_b),str((3,6)))
        self.assertEqual(str(self.complex_a + self.complex_a),str((2,4)))
        self.assertEqual(str(self.complex_a + self.complex_e), str((1,2)))
        self.assertEqual(str(self.complex_h + self.complex_h), str((1.0,1.5)))
    
    def test_sub(self):
        self.assertEqual(str(self.complex_a - self.complex_a), str((0,0)))
        self.assertEqual(str(self.complex_b - self.complex_c), str((8,2)))
        self.assertEqual(str(self.complex_c - self.complex_b),str((-8,-2)))
        self.assertEqual(str(self.complex_d - self.complex_a) , str((-6,-10)))
        self.assertEqual(str(self.complex_a - self.complex_e), str((1,2)))
    def test_mul(self):
        self.assertEqual(str(self.complex_a * self.complex_b) , str((-6,8)))
        self.assertEqual(str(self.complex_c * self.complex_f), str((-8,-4)))
        self.assertEqual(str(self.complex_d * self.complex_c), str((46,38)))
        self.assertEqual(str(self.complex_h * self.complex_b) , str((-2.0,3.5)) )        
        
    def test_div(self):
        self.assertEqual(str(self.complex_f / self.complex_h), str((4/5,-4/25)))
        self.assertEqual(str(self.complex_a / self.complex_a), str((5/8,0.0)))
        self.assertEqual(str(self.complex_c / self.complex_f), str((-4/5,8/5)))
        self.assertEqual(str(self.complex_h / self.complex_b), str((64/265, -8/265)))
        
    def test_mod(self):
        self.complex_a_b = (self.complex_a + self.complex_b)
        self.assertEqual(self.complex_a_b.mod(), 6.71)
        self.complex_ab = self.complex_a * self.complex_b
        self.assertEqual(self.complex_ab.mod(), 10)
        self.assertEqual(self.complex_a.mod(), 2.24)
        self.assertEqual(self.complex_b.mod(), 4.47)
        self.assertEqual(self.complex_e.mod(), 0)
        self.assertEqual(self.complex_f.mod(), 1.41)
        
    def test_conjugado(self):
        self.assertEqual(str(self.complex_a.conjugado()),str((1,-2)))
        self.assertEqual(str(self.complex_b.conjugado()),str((2,-4)))
        self.assertEqual(str(self.complex_c.conjugado()),str((-6,-2)))
        self.assertEqual(str(self.complex_d.conjugado()),str((-5,8)))
        self.assertEqual(str(self.complex_e.conjugado()),str((0,0)))
        self.assertEqual(str(self.complex_f.conjugado()),str((1,-1)))
        self.assertEqual(str(self.complex_h.conjugado()),str((1/2,-3/4)))
          
    def test_polar(self):
        self.assertEqual(str(self.complex_a.polar()),str((2.24,1.11)))
        self.assertEqual(str(self.complex_h.polar()),str((0.90,0.98)))
        self.assertEqual(str(self.complex_f.polar()),str((1.41,0.79)))
        self.assertEqual(str(self.complex_b.polar()),str((4.47,1.11)))
        
    def test_phase(self):
        self.assertEqual(self.complex_a.phase(),1.11)
        self.assertEqual(self.complex_h.phase(),0.98)
        self.assertEqual(self.complex_f.phase(),0.79)
        self.assertEqual(self.complex_b.phase(),1.11)
    
    def test_cart(self):
        self.assertEqual(str(self.complex_A.cart()),str((-5.66,5.66)))
        self.assertEqual(str(self.complex_B.cart()),str((-2.97,-0.43)))
        self.assertEqual(str(self.complex_C.cart()),str(((-7.42,22.83))))
        self.assertEqual(str(self.complex_D.cart()),str((1.99,4.0)))
        
        
if __name__== '__main__':
    unittest.main()

