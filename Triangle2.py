
"""-*- coding: utf-8 -*-
Created on Thu Jan 14 13:44:00 2016
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple python program to classify triangles
@author: jrr
@author: rk
"""

def classifyTriangle(a, b, c):
    """
    This function returns a string with the type of triangle from three integer values
    corresponding to the lengths of the three sides of the Triangle.
    
    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isoceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the square of the third side, then return 'Right'
      
      BEWARE: there may be a bug or two in this code
    """ 
    # require that the input values be >= 0 and <= 200
    if a > 200 or b > 200 or c > 200:
        return 'InvalidInput'
    
    if a <= 0 or b <= 0 or c <= 0:
        return 'InvalidInput'
    
    # verify that all 3 inputs are integers  
    # Python's "isinstance(object,type) returns True if the object is of the specified type
    if not(isinstance(a,int)) or not(isinstance(b,int)) or not(isinstance(c,int)):
        return 'InvalidInput'
    
    # checks for false/true as they extend int in python but won't work here
    if a is False or b is False or c is False:
      return 'InvalidInput'
    if a is True or b is True or c is True:
      return 'InvalidInput'
      
    # This information was not in the requirements spec but 
    # is important for correctness
    # the sum of any two sides must be strictly less than the third side
    # of the specified shape is not a triangle
    if (a >= (b + c)) or (b >= (a + c)) or (c >= (a + b)):
        return 'NotATriangle'
        
    # now we know that we have a valid triangle 
    if a == b and b == a and c == b:
        return 'Equilateral'
    # A method to classify which is the hypotenuse of the triangle (Pythogoras Theoram)
    if round(a ** 2 + b ** 2) == round(c ** 2):
        return 'Right'
    if round(b ** 2 + c ** 2) == round(a ** 2):
        return 'Right'
    if round(c ** 2 + a ** 2) == round(b ** 2):
        return 'Right'
    if (a != b) and  (b != c) and (a != c):
        return 'Scalene'
    return 'Isoceles'

