import random

l = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!?=+/*-"

length_password = int(input("Ingrese el número de caracteres de la contraseña: "))

password = ""

for i in range(length_password):
    char = random.choice(l)
    password += char

print(password)

input("Presione ENTER para salir...")
