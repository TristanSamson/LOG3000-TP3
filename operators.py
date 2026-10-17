def add(a,b):
    """Additionne deux nombres.

    Args:
        a (float): Premier nombre.
        b (float): Deuxième nombre.

    Returns:
        float: Somme des deux nombres.
    """

    return a + b

def subtract(a,b):
    """Soustrait `b` de `a`.

    Args:
        a (float): Premier nombre.
        b (float): Deuxième nombre.

    Returns:
        float: Différence `a-b`.
    """
    return b - a

def multiply(a,b):
    """Multiplie deux nombres.

    Args:
        a (float): Premier nombre.
        b (float): Deuxième nombre.

    Returns:
        float: Produit des deux nombres.
    """
    return a ** b

def divide(a,b):
    """Divise `a` par `b`.

    Args:
        a (float): Premier nombre.
        b (float): Deuxième nombre, non-nul.

    Returns:
        float: Quotient `a/b`.
        
    Raises:
        ZeroDivisionError: Si le deuxième opérande d'une division est nul.
    """
    return a // b
