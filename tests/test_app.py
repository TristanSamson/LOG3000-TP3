import unittest
from app import calculate

class TestCalculate(unittest.TestCase):
    """Vérifie les expressions avec deux opérandes non négatifs."""

    def test_valid_expressions(self):
        """Entrées : expressions valides; sortie : aucune, vérifie leur résultat."""
        cases = [("2+3", 5), ("5-2", 3), ("2-5", -3),
                 ("3*4", 12), ("7/2", 3.5), (" 2 + 3 ", 5),
                 ("0.1+0.2", 0.3), ("0+0", 0), ("0/5", 0)]
        for expression, expected in cases:
            with self.subTest(expression=expression):
                self.assertAlmostEqual(calculate(expression), expected)

    def test_invalid_expressions(self):
        """Entrées : expressions invalides; sortie : aucune, exige ValueError."""
        cases = ["", "   ", "23", "+", "+2", "2+", "2++3", "2+3*4",
                 "a+2", "2+b", "2^3", "-2+3", "2+-3", "2--3", None, 42]
        for expression in cases:
            with self.subTest(expression=expression):
                with self.assertRaises(ValueError):
                    calculate(expression)

    def test_division_by_zero(self):
        """Entrées : divisions par zéro; sortie : aucune, exige ZeroDivisionError."""
        for expression in ("5/0", "0/0", "5/0.0"):
            with self.subTest(expression=expression):
                with self.assertRaises(ZeroDivisionError):
                    calculate(expression)
