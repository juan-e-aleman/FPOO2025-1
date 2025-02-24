import random

adivina = random.randint(1, 10)
print('Adivina el número entre 1 y 10')
numero = int(input('Ingresa un número: '))
if numero == adivina:
    print('Adivinaste!')
else:
    print('Fallaste! El número era', adivina)