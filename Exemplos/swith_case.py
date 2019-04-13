num = int(input('Digite um número : '))

print('O número digitado é...')

if num > 1000:
    print('Maior que 1000')
elif num > 500:
    print('Menor que 1000 e maior que 500')
elif num > 250:
    print('Menor que 500 e maior que 250')
elif num > 100:
    print('Menor que 250 e maior que 100')
else:
    print('Menor que 100')