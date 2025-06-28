print("********************************************************************")
print("Bienvenido/a. A continuación deberás ingresar 3 notas.")
print("Por favor, usa punto para los decimales. Ejemplo: 4.5, 3.8, 2.9")
print("********************************************************************")

note_1 = float(input("Ingresa la primera nota: "))
note_2 = float(input("Ingresa la segunda nota: "))
note_3 = float(input("Ingresa la tercera nota: "))

promedio = (note_1 + note_2 + note_3) / 3

print("-----------------------------------")
print(f"Tu promedio es: {promedio:.2f}")
print("-----------------------------------\n")

if promedio >= 3.0:
    print(":D :D :D :D :D :D :D :D :D :D")
    print("¡¡¡Felicidades!!! Has aprobado.")
    print(":D :D :D :D :D :D :D :D :D :D¨")

else:
    print(":( :( :( :( :( :( :( :( :( :(")
    print("Lo siento, no has aprobado.")
    print(":( :( :( :( :( :( :( :( :( :(")

