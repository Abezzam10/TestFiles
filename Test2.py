'''
Updated Jan 21, 2018
the primary goal of this file is to demonstrate a simple unittest
implementation
@author: jrr
@author: rk'''



import unittest

from Triangle2 import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

S = 'Scalene'
E = 'Equilateral'
R = 'Right'
I = 'Isoceles'
NotTriangle = 'NotATriangle'
Invalid_inp = 'InvalidInput'

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self):
        self.assertEqual( classifyTriangle(3, 4, 5), R, '3, 4, 5 is a Right triangle' )

    def testRightTriangleB(self): 
        self.assertEqual( classifyTriangle(5, 3, 4), R, '5, 3, 4 is a Right triangle' )
    
    def testRightTriangleC(self): 
        self.assertEqual( classifyTriangle(4, 5, 3), R, '4, 5, 3 is a Right triangle' )

    def testRightTriangleD(self): 
        self.assertEqual( classifyTriangle(5, 12, 13), R, '5, 12, 13 is a Right triangle' )

    def testRightTriangleE(self): 
        self.assertEqual( classifyTriangle(24, 7, 25), R, '24, 7, 25 is a Right triangle' )

    def testNotaRightTriangle(self):
        self.assertNotEqual( classifyTriangle( 2, 2, 2), R, "2, 2, 2 is not a right triangle")
   
    def testEquilateralTrianglesSmall(self): 
        self.assertEqual( classifyTriangle(1, 1, 1), E, '1, 1, 1 should be equilateral' )
    
    def testEquilateralTrianglesMed(self): 
        self.assertEqual( classifyTriangle(10, 10, 10), E, '10, 10, 10 should be equilateral' )

    def testNotEquilateralTriangles(self):
        self.assertNotEqual( classifyTriangle(10, 9, 10), E, '10, 9, 10 is not equilateral'  )

    def testScaleneA(self):
        self.assertEqual( classifyTriangle(4, 5, 6), S, '4, 5, 6 should be scalene' )

    def testScaleneB(self):
        self.assertEqual( classifyTriangle(5, 6, 4), S, '5, 6, 4 should be scalene' )

    def testScaleneC(self):
        self.assertEqual( classifyTriangle(6, 4, 5), S, '6, 4, 5 should be scalene' )

    def NotScalene(self):
        self.assertNotEqual( classifyTriangle( 2, 3, 4), S, '2, 3, 4 is Not scalene' )

    def testIsoscelesA(self):
        self.assertEqual( classifyTriangle(3, 4, 4), I , '3, 4, 4 should be isosceles' )

    def testIsoscelesB(self):
        self.assertEqual( classifyTriangle(4, 3, 4), I , '4, 3, 4 should be isosceles' )

    def testIsoscelesC(self):
        self.assertEqual( classifyTriangle(4, 4, 3), I , '4, 4, 3 should be isosceles' )
    
    def testNotATriangleA(self):
        self.assertEqual( classifyTriangle(2, 3, 10), NotTriangle , '2, 3, 10 is not a triangle' )

    def testNotATriangleB(self):
        self.assertEqual( classifyTriangle(2, 10, 3), NotTriangle , '2, 10, 3 is not a triangle' )

    def testNotATriangleC(self):
        self.assertEqual( classifyTriangle(10, 2, 3), NotTriangle , '10, 2, 3 is not a triangle' )

    def testBadInputsFloatA(self):
        self.assertEqual( classifyTriangle(1, 0.25, 3), Invalid_inp , '1, 0.25, 3 is invalid input' )
    
    def testBadInputsFloatB(self):
        self.assertEqual( classifyTriangle(0.25, 1, 3), Invalid_inp , '0.25, 1, 3 is invalid input' )
    
    def testBadInputsFloatC(self):
        self.assertEqual( classifyTriangle(1, 3, 0.25), Invalid_inp , '1, 3, 0.25 is invalid input' )
    
    def testBadInputsNegA(self):
        self.assertEqual( classifyTriangle(-1, 4, 4), Invalid_inp , '-1, 4, 4 is invalid input' )

    def testBadInputsNegB(self):
        self.assertEqual( classifyTriangle(4, -1, 4), Invalid_inp , '4, -1, 4 is invalid input' )

    def testBadInputsNegC(self):
        self.assertEqual( classifyTriangle(4, 4, -1), Invalid_inp , '4, 4, -1 is invalid input' )

    def testBadInputsObjA(self):
        self.assertEqual( classifyTriangle(False, 2, 1), Invalid_inp , 'False, 2, 1 is invalid input' )

    def testBadInputsObjB(self):
        self.assertEqual( classifyTriangle(4, False, 1), Invalid_inp , '4, False, 1 is invalid input' )

    def testBadInputsObjC(self):
        self.assertEqual( classifyTriangle(4, 2, True), Invalid_inp , '4, 2, True is invalid input' )
    
    def testBadInputsZeroA(self):
        self.assertEqual( classifyTriangle(4, 4, 0), Invalid_inp , '4, 4, 0 is invalid input' )
    
    def testBadInputsZeroB(self):
        self.assertEqual( classifyTriangle(4, 0, 4), Invalid_inp , '4, 0, 4 is invalid input' )
    
    def testBadInputsZeroC(self):
        self.assertEqual( classifyTriangle(0, 4, 4), Invalid_inp , '0, 4, 4 is invalid input' )

    def Hugenos(self):
        self.assertEqual( classifyTriangle(200, 204, 304), Invalid_inp , '200, 204, 304 is invalid input' )

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

