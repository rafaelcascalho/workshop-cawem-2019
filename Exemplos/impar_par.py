def par(num):
    return num % 2 == 0

def mostra_resultado(num, resultado):
    if resultado == True:
        print('O número %i é par.' % num)
    else:
        print('O número %i é impar.' % num)

def main():
    num = int(input('Digite um número para ser avaliado como ímpar ou par : '))
    resultado = par(num)
    mostra_resultado(num, resultado)

main()