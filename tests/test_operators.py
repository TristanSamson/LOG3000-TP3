import unittest

from operators import add, subtract, multiply, divide

class TestOperators(unittest.TestCase):
    """Vérifie le bon fonctionnement des fonctions d'opérateurs avec deux opérandes non négatifs"""    

    def test_add(self):
        """Vérifie les sommes attendues, notamment avec zéro et des décimaux.

        Entrées : aucune en paramètre; les cas sont définis dans le test.
        Sortie : aucune; une assertion échoue si une somme est incorrecte.
        """
        for a, b, expected in [(2, 3, 5), (0, 5, 5), (0, 0, 0), (0.1, 0.2, 0.3)]:
            with self.subTest(a=a, b=b):
                # Tolère les imprécisions reliées aux nombres flottants.
                self.assertAlmostEqual(add(a, b), expected)

    def test_subtract(self):
        """Vérifie l'ordre des opérandes et les différences nulles ou négatives.

        Entrées : aucune en paramètre; les cas sont définis dans le test.
        Sortie : aucune; une assertion échoue si une différence est incorrecte.
        """
        for a, b, expected in [(5, 2, 3), (2, 5, -3), (4, 4, 0), (5, 0, 5), (2.5, 1.2, 1.3)]:
            with self.subTest(a=a, b=b):
                self.assertAlmostEqual(subtract(a, b), expected)

    def test_multiply(self):
        """Vérifie les produits attendus, notamment avec zéro, un et des décimaux.

        Entrées : aucune en paramètre; les cas sont définis dans le test.
        Sortie : aucune; une assertion échoue si un produit est incorrect.
        """
        for a, b, expected in [(3, 4, 12), (5, 0, 0), (0, 5, 0), (5, 1, 5), (1.5, 2.5, 3.75)]:
            with self.subTest(a=a, b=b):
                self.assertAlmostEqual(multiply(a, b), expected)

    def test_divide(self):
        """Vérifie les quotients attendus, y compris les résultats non entiers.

        Entrées : aucune en paramètre; les cas sont définis dans le test.
        Sortie : aucune; une assertion échoue si un quotient est incorrect.
        """
        for a, b, expected in [(8, 2, 4), (7, 2, 3.5), (1, 4, 0.25), (0, 5, 0), (2.5, 0.5, 5)]:
            with self.subTest(a=a, b=b):
                self.assertAlmostEqual(divide(a, b), expected)

    def test_divide_by_zero(self):
        """Vérifie qu'un diviseur nul provoque une ZeroDivisionError.

        Entrées : aucune en paramètre; les dividendes testés sont zéro et cinq.
        Sortie : aucune; une assertion échoue si l'exception n'est pas levée.
        """
        for a in (0, 5):
            with self.subTest(a=a):
                with self.assertRaises(ZeroDivisionError):
                    divide(a, 0)


if __name__ == "__main__":
    unittest.main()
