"""Code by Anirudh Das Bezzam"""
import unittest
def classify_triangle(side_a, side_b, side_c):
    """Triangle Classifier"""
    if side_a == side_b and side_b == side_c and side_c == side_a:
        print("Equilateral triangle is the triangle type you entered")
        triangle = 'Equilateral'
    elif side_b in (side_a, side_c):
        print("Isosceles triangle is the triangle type you entered")
        triangle = 'Isosceles'
    else:
        print("Scalene triangle is the triangle type you entered")
        triangle = 'Scalene'
    return triangle
def validate_right_angle(side_a, side_b, side_c):
    """using Pythogoras theoram to validate if a square + b square = C square"""
    if (side_a*side_a) + (side_b*side_b) == (side_c*side_c):
        triangle = 'Right'
    return triangle

class TestTriangles(unittest.TestCase):
    """Verifying Triangles"""
    def test_triangle(self):
        """ Verfiying the test set """
        self.assertEqual(validate_right_angle(3, 4, 5), "Right")
        self.assertEqual(classify_triangle(233, 233, 233), "Equilateral")
        self.assertEqual(classify_triangle(2, 3, 3), "Isosceles")
        self.assertNotEqual(classify_triangle(19, 9, 9), "Equilateral")
        self.assertNotEqual(classify_triangle(10, 10, 10), "Isosceles")

if __name__ == "__main__":
    classify_triangle(3, 4, 5)
    validate_right_angle(3, 4, 5)
    unittest.main(exit=False, verbosity=2)
               