# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 11:40:20 2020

@author: Cristian
"""
import math

class complex_number():
    
    def __init__(self,X,Y):
        self.a = X
        self.b = Y
    
    def __str__(self):
        string = (self.a,self.b)
        return str(string)
    
    def __add__(self,self_1):
        return (self.a + self_1.a, self.b + self_1.b)
    
    def __sub__(self,self_1):
        return (self.a - self_1.a, self.b - self_1.b)
    
    def __mul__(self, self_1):
        ans_1 = (self.a * self_1.a) - (self.b * self_1.b)
        ans_2 = (self.a * self_1.b) + (self.b * self_1.a)
        return(ans_1,ans_2)
    
    def __truediv__(self, self_1):
        ans_1 = (self.a * self_1.a) + (self.b * self_1.b)
        ans_2 = (self.b * self_1.a) - (self.a * self_1.b)
        module = (self.b**2)+(self_1.b**2)
        return (ans_1/module,ans_2/module)
    
    def mod(self):
        return math.sqrt((self.a**2)+(self.b**2))
    
    def conjugado(self):
        self.b = -self.b
        return (self.a,self.b)
    
    def polar(self):
        r = math.sqrt((self.a**2)+(self.b**2))
        tetha = math.atan(self.a/self.b)
        return (r,tetha)
    
    
        
        

