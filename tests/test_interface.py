"""Vérification du HTML rendu; ces tests n'exécutent pas JavaScript."""

from html.parser import HTMLParser
import unittest
from app import app


class CalculatorHTMLParser(HTMLParser):
    """Extrait les attributs et libellés des boutons, champs et formulaires."""

    def __init__(self):
        """Entrées : aucune; sortie : aucune, initialise les collections HTML."""
        super().__init__()
        self.buttons = []
        self.inputs = []
        self.forms = []
        self.current_button = None

    def handle_starttag(self, tag, attrs):
        """Entrées : balise et attributs; sortie : aucune, collecte les éléments utiles."""
        attrs = dict(attrs)
        if tag == "button":
            self.current_button = {"attrs": attrs, "label": ""}
            self.buttons.append(self.current_button)
        elif tag == "input":
            self.inputs.append(attrs)
        elif tag == "form":
            self.forms.append(attrs)

    def handle_data(self, data):
        """Entrée : texte HTML; sortie : aucune, accumule le libellé du bouton courant."""
        if self.current_button is not None:
            self.current_button["label"] += data

    def handle_endtag(self, tag):
        """Entrée : balise fermante; sortie : aucune, termine le bouton courant."""
        if tag == "button":
            self.current_button = None


class TestInterface(unittest.TestCase):
    """Vérifie les libellés et les actions déclarées dans le HTML."""

    def setUp(self):
        """Entrées : aucune; sortie : aucune, analyse la page fournie par Flask."""
        self.parser = CalculatorHTMLParser()
        response = app.test_client().get("/")
        self.assertEqual(response.status_code, 200)
        self.parser.feed(response.get_data(as_text=True))

    def test_digit_and_operator_buttons(self):
        """Entrées : chiffres et opérateurs attendus; sortie : aucune, vérifie chaque touche."""
        for value in "0123456789+-*/":
            with self.subTest(value=value):
                buttons = [b for b in self.parser.buttons
                           if b["attrs"].get("onclick") == f"appendToDisplay('{value}')"]
                self.assertEqual(len(buttons), 1)
                self.assertEqual(buttons[0]["label"].strip(), value)
                self.assertEqual(buttons[0]["attrs"].get("type"), "button")

    def test_clear_button(self):
        """Entrées : aucune; sortie : aucune, vérifie le bouton C et son action déclarée."""
        buttons = [b for b in self.parser.buttons
                   if b["attrs"].get("onclick") == "clearDisplay()"]
        self.assertEqual(len(buttons), 1)
        self.assertEqual(buttons[0]["label"].strip(), "C")
        self.assertEqual(buttons[0]["attrs"].get("type"), "button")

    def test_submit_and_display(self):
        """Entrées : aucune; sortie : aucune, vérifie le formulaire, l'écran et le bouton égal."""
        self.assertEqual(len(self.parser.forms), 1)
        self.assertEqual(self.parser.forms[0].get("method", "").upper(), "POST")
        displays = [field for field in self.parser.inputs if field.get("id") == "display"]
        self.assertEqual(len(displays), 1)
        self.assertEqual(displays[0].get("name"), "display")
        self.assertIn("readonly", displays[0])
        self.assertEqual(displays[0].get("value"), "")
        submits = [b for b in self.parser.buttons if b["attrs"].get("type") == "submit"]
        self.assertEqual(len(submits), 1)
        self.assertEqual(submits[0]["label"].strip(), "=")
