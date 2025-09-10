"""
Pruebas unitarias para math_utils.py
"""

import unittest
from math_utils import square, factorial, is_prime, gcd, lcm

class TestMathUtils(unittest.TestCase):
    
    def test_square_happy_path(self):
        """Pruebas exitosas para square"""
        self.assertEqual(square(4), 16)
        self.assertEqual(square(-3), 9)
        self.assertEqual(square(0), 0)
        self.assertEqual(square(2.5), 6.25)
    
    def test_square_error_cases(self):
        """Pruebas de error para square"""
        with self.assertRaises(TypeError):
            square("texto")
        with self.assertRaises(TypeError):
            square(None)
    
    def test_factorial_happy_path(self):
        """Pruebas exitosas para factorial"""
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(3), 6)
    
    def test_factorial_error_cases(self):
        """Pruebas de error para factorial"""
        with self.assertRaises(ValueError):
            factorial(-1)
        with self.assertRaises(TypeError):
            factorial(3.5)
        with self.assertRaises(TypeError):
            factorial("5")
    
    def test_is_prime_happy_path(self):
        """Pruebas exitosas para is_prime"""
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(7))
        self.assertTrue(is_prime(13))
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(9))
        self.assertFalse(is_prime(15))
    
    def test_is_prime_error_cases(self):
        """Pruebas de error para is_prime"""
        with self.assertRaises(ValueError):
            is_prime(1)
        with self.assertRaises(ValueError):
            is_prime(-5)
        with self.assertRaises(TypeError):
            is_prime(3.5)
    
    def test_gcd_happy_path(self):
        """Pruebas exitosas para gcd"""
        self.assertEqual(gcd(12, 8), 4)
        self.assertEqual(gcd(15, 25), 5)
        self.assertEqual(gcd(7, 3), 1)
        self.assertEqual(gcd(-12, 8), 4)  # Con negativos
    
    def test_gcd_error_cases(self):
        """Pruebas de error para gcd"""
        with self.assertRaises(ValueError):
            gcd(0, 0)
        with self.assertRaises(TypeError):
            gcd(3.5, 2)
        with self.assertRaises(TypeError):
            gcd("12", 8)
    
    def test_lcm_happy_path(self):
        """Pruebas exitosas para lcm"""
        self.assertEqual(lcm(12, 8), 24)
        self.assertEqual(lcm(15, 25), 75)
        self.assertEqual(lcm(7, 3), 21)
        self.assertEqual(lcm(4, 6), 12)
    
    def test_lcm_error_cases(self):
        """Pruebas de error para lcm"""
        with self.assertRaises(ValueError):
            lcm(0, 5)
        with self.assertRaises(ValueError):
            lcm(5, 0)
        with self.assertRaises(TypeError):
            lcm(3.5, 2)

if __name__ == '__main__':
    unittest.main()