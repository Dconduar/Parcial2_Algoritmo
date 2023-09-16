def calcular_cuadrado():
    numero = int(input("Por favor, ingrese un número entero: "))
    cuadrado = numero ** 2
    print(f"El cuadrado de {numero} es igual a {cuadrado}.")

def calcular_producto():
    numero1 = float(input("Ingrese un número decimal: "))
    numero2 = float(input("Ingrese otro número decimal: "))
    producto = numero1 * numero2
    print(f"El producto de {numero1} y {numero2} es igual a {producto}.")

calcular_cuadrado()
calcular_producto()

