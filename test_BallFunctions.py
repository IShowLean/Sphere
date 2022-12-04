import unittest
from math import pi
from BallFunctions import get_ball_square, get_ball_volume

class TestBallFunctions(unittest.TestCase):

    def test_volume(self):
        self.assertEqual(get_ball_volume(0), 0)
        self.assertEqual(get_ball_volume(1), 4/3*pi)
        self.assertEqual(get_ball_volume(7), 4/3*pi*7**3)

    def test_square(self):
        self.assertEqual(get_ball_square(0), 0)
        self.assertEqual(get_ball_square(1), 4*pi)
        self.assertEqual(get_ball_square(10), 4*pi*10**2)

    def test_acceptable_values(self):
        self.assertRaises(ValueError, get_ball_square, -5)
        self.assertRaises(ValueError, get_ball_volume, -12)
    
    def test_acceptable_types(self):
        self.assertRaises(TypeError, get_ball_square, [1,2,3])
        self.assertRaises(TypeError, get_ball_square, {"Ronaldo": 5, "Messi": 3})
        self.assertRaises(TypeError, get_ball_square, 12+7j)
        self.assertRaises(TypeError, get_ball_square, 'World Cup')
        self.assertRaises(TypeError, get_ball_volume, [1,2,3])
        self.assertRaises(TypeError, get_ball_volume, {"Ronaldo": 5, "Messi": 3})
        self.assertRaises(TypeError, get_ball_volume, 12+7j)
        self.assertRaises(TypeError, get_ball_volume, 'World Cup')

if __name__ == '__main__':
    unittest.main()
