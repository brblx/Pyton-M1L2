import random

numero = (random.randint(1, 20))


for i in range(10):
    seleccion = (int(input("Introduzca un numero del 1 al 20: ")))
    if seleccion == numero:
        print("Escogiste en numero correcto!")
    elif seleccion > numero:
        print("El numero es menor")
    elif seleccion < numero:
        print("El numero es mayor")

print("Te quedaste sin intentos")
