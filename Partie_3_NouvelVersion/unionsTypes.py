# UNION DE TYPES

def operation_speciale(a : int | float):
    if isinstance(a, int | float): # Si a est une instance de type int ou bien de type FLoat
        return a * a
    print("Mauvais type")
    return None

print(operation_speciale(5.5))