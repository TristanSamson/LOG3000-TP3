from flask import Flask, request, render_template
from operators import add, subtract, multiply, divide

app = Flask(__name__)

# Permet d'identifier en temps constant la fonction à utiliser 
# selon l'opérateur mathématique désiré
OPS = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}

def calculate(expr: str):
    """Effectue une opération mathématique à partir de son expression textuelle.
    Supporte l'addition, la soustraction, la multiplication et la division.

    Args:
        expr (str): Expression mathématique. Doit être non-vide. Doit être composée
        de deux nombres séparés d'un seul opérateur. Par exemple: `2+2`, ou `24/3`.

    Returns:
        float: Résultat de l'opération.
        
    Raises:
        ValueError: Si l'expression est vide, n'est pas une chaîne de caractères (str),
            ne contient pas exactement un des opérateur accepté (+, -, *, /),
            ou ne contient pas deux opérandes convertibles en nombres.
        ZeroDivisionError: Si le deuxième opérande d'une division est nul.
    """
    
    if not expr or not isinstance(expr, str):
        raise ValueError("empty expression")

    s = expr.replace(" ", "")

    op_pos = -1
    op_char = None

    for i, ch in enumerate(s):
        if ch in OPS:
            if op_pos != -1:
                raise ValueError("only one operator is allowed")
            op_pos = i
            op_char = ch

    if op_pos <= 0 or op_pos >= len(s) - 1:
        # L'opérateur doit séparer deux opérandes non vides.
        raise ValueError("invalid expression format")

    left = s[:op_pos]
    right = s[op_pos+1:]

    # Convertit les opérandes textuelles en flottants pour accepter les nombres décimaux.
    try:
        a = float(left)
        b = float(right)
    except ValueError:
        raise ValueError("operands must be numbers")

    return OPS[op_char](a, b)

@app.route('/', methods=['GET', 'POST'])
def index():
    """Affiche l'interface de la calculatrice et 
    traite les opérations de calcul, selon le type de requête envoyée.

    Une requête GET affiche l'interface avec un résultat vide.
    Une requête POST évalue l'expression incluse dans le champ de formulaire 
    "display" et affiche le résultat ou un message d'erreur.

    Entrées:
        Aucune en paramètre. Lors d'une requête POST, lit le champ
        de formulaire "display" dans les données de la requête HTTP.

    Sortie:
        str: Page HTML générée à partir du gabarit index.html, avec son
        résultat
    """
    
    result = ""
    if request.method == 'POST':
        expression = request.form.get('display', '')
        try:
            result = calculate(expression)
        except Exception as e:
            result = f"Error: {e}"
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)