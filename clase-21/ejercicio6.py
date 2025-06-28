
print('*******************')
print('INGRESE 5 NUMEROS')
print('*******************')

sum = 0

for i in range(5):
    num = int(input(f'Ingrese el numero {i + 1}: '))
    
    sum += num
    print(f'la suma de los numeros ingresados es: {sum}')