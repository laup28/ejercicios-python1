from datetime import datetime #modulo

year_born = int(input('Hola, ingresa tu año de nacimiento: '))

year_current = datetime.now().year

age = year_current - year_born

print(f'Tienes {age} años')