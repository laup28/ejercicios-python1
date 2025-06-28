from datetime import datetime

# Pedimos la fecha de nacimiento como string
year_born = input('Hola, ingresa tu fecha de nacimiento (DD/MM/AAAA): ')

# Convertimos el string a datetime
year_born_str = datetime.strptime(year_born, "%d/%m/%Y")

# Fecha actual
year_current = datetime.now()

# Próximo cumpleaños este año
age = datetime(year_current.year, year_born_str.month, year_born_str.day)

# Si ya pasó, usamos el del próximo año
if age < year_current:
    age = datetime(year_current.year + 1, year_born_str.month, year_born_str.day)

# Calculamos cuántos días faltan
dias_faltan = (age - year_current).days

print(f'Te faltan {dias_faltan} días para cumplir años')
