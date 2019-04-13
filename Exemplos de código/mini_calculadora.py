num1, num2 = map(int, input('Digite os valores a serem usados (em ordem) : ').split())
opr = input('Digite a operação desejada (som, sub, mult, div) : ')

if opr == 'som':
  resultado = num1 + num2
elif opr == 'sub':
  resultado = num1 - num2
elif opr == 'mult':
  resultado = num1 * num2
else:
  resultado = num1 / num2
  
print('A resposta é : ' + str(resultado))