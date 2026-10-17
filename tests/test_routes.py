import unittest
from unittest.mock import patch
from flask import template_rendered
from app import app


class TestRoutes(unittest.TestCase):
    """Vérifie les réponses HTTP et les valeurs transmises au gabarit."""

    def setUp(self):
        """Entrées : aucune; sortie : aucune, prépare un client et capture le rendu."""
        self.client = app.test_client()
        self.contexts = []
        template_rendered.connect(self.capture_template, app)
        self.addCleanup(template_rendered.disconnect, self.capture_template, app)

    def capture_template(self, sender, template, context, **extra):
        """Entrées : signal Flask et contexte; sortie : aucune, mémorise le contexte."""
        self.contexts.append(context)

    def test_get(self):
        """Entrée : GET /; sortie : aucune, vérifie la page et son écran vide."""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.mimetype, "text/html")
        self.assertIn(b'name="display"', response.data)
        self.assertEqual(self.contexts[-1]["result"], "")

    def test_post_results(self):
        """Entrées : formulaires valides; sortie : aucune, vérifie les résultats."""
        for expression, expected in [("2+3", 5), ("5-2", 3),
                                     ("3*4", 12), ("7/2", 3.5)]:
            with self.subTest(expression=expression):
                response = self.client.post("/", data={"display": expression})
                self.assertEqual(response.status_code, 200)
                self.assertAlmostEqual(self.contexts[-1]["result"], expected)

    def test_post_errors(self):
        """Entrées : formulaires invalides; sortie : aucune, vérifie les erreurs affichées."""
        for data in ({}, {"display": ""}, {"display": "2+"},
                     {"display": "-2+3"}, {"display": "5/0"}):
            with self.subTest(data=data):
                response = self.client.post("/", data=data)
                self.assertEqual(response.status_code, 200)
                result = self.contexts[-1]["result"]
                self.assertTrue(result.startswith("Error:"))
                self.assertIn(result, response.get_data(as_text=True))

    def test_post_passes_expression_to_calculate(self):
        """Entrée : expression du formulaire; sortie : aucune, vérifie sa transmission."""
        # Isole le contrat HTTP des bogues éventuels dans les opérations.
        with patch("app.calculate", return_value=42) as mocked_calculate:
            response = self.client.post("/", data={"display": " 20 + 22 "})
        mocked_calculate.assert_called_once_with(" 20 + 22 ")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.contexts[-1]["result"], 42)
