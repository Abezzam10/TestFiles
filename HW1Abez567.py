''' Code by Anirudh Das Bezzam'''

'''Program for testing triangle classification'''

#Importing the unittest, automated test platform library.

import unittest


def classify_triangle(a,b,c):
    '''Triangle Classifier'''

    if a == b and b == c and c == a:
        print("Equilateral triangle is the triangle type you entered")
        triangle = 'Equilateral'
    elif a==b or b==c:
        print("Isosceles triangle is the triangle type you entered")
        triangle = 'Isosceles'
    else:
        print("Scalene triangle is the triangle type you entered")
        triangle = 'Scalene'

    return triangle

def validate_right_angle(a, b, c):
    
    if (a * a) + (b * b) == (c * c):   # using Pythogoras theoram to validate if a square + b square = C square
        triangle = 'Right'

    return triangle

class TestTriangles(unittest.TestCase):

    def testSet(self):
        '''Verfiying the test set'''
        self.assertEqual(validate_right_angle(3, 4, 5),'Right')
        self.assertEqual(classify_triangle(233,233,233),'Equilateral')
        self.assertEqual(classify_triangle(2,3,3),'Isosceles')
        self.assertNotEqual(classify_triangle(19,9,9), 'Equilateral')
        self.assertNotEqual(classify_triangle(10,10,10), 'Isosceles')


if __name__ == '__main__':

    classify_triangle
    validate_right_angle
    unittest.main(exit=False,verbosity=2)
               