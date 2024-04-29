
while True:
    num = int(input("Introduce un número impar: "))
    if num % 2 != 0:
        break
    else:
        print("El número introducido no es impar. Intenta de nuevo.")

print("Número impar introducido correctamente:", num)
