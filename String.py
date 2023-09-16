def contar_letras_a(cadena):
    return cadena.lower().count('a')

cadena = "Algoritmos"
cantidad_de_a = contar_letras_a(cadena)
print(f"La cantidad de letras 'a' en la cadena es: {cantidad_de_a}")
