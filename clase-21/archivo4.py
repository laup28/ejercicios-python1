"""
EN ESTE ARCHIVO CONTINUAMOS CON EL JUEGO DE BUSCAR EL NUMERO
"""

num = 50

while True:

    num1 = int(input('Adivina el numero, esta en un rango de 1 a 60: '))

    if num1 == num:
        print('Felicidades acertaste!!!!')
        break
    elif num1 > num:
        print('El numero que buscas en menor')
    else:
        print('Sigue intentando el numero que buscas es mayor')