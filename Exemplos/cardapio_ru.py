cardapio_carnes_semana = {
    'segunda': 'bife',
    'terca': 'peixe',
    'quarta': 'frango',
    'quinta': 'lombo',
    'sexta': 'quibe',
    'sábado': 'lagarto'
}

dia = input('Digite o dia da semana e descubra a carne do cardápio : ')
while dia not in cardapio_carnes_semana:
    print('Ops, você digitou um dia fora dos dias que o ru serve...ou que nem existe o.O')
    dia = input('Digite outro valor para o dia da semana : ')
print('A carne de {} é : {} .'.format(dia, cardapio_carnes_semana[dia]))