import random


elementos = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"


longitud = int(input("Introduzca la longitud del pase: "))


contraseña = ""


for i in range(longitud):
    contraseña += random.choice(elementos)

print(contraseña)
