nomes = [
    'Alice','Miguel','Sophia','Arthur','Helena','Bernardo',
    'Valentina','Heitor','Laura','Davi','Isabella','Lorenzo',
    'Manuela','Théo','Júlia','Pedro','Heloísa','Gabriel','Luiza',
    'Enzo','Maria','Luiza','Matheus', 'Rafael', 'Felipe', 'Stefany'
]


print('Lista de nomes : ')
print(nomes)
print('=======================')
print('Regras :')
print('1. Se o nome não existir, ele vai ser addicionado à lista')
print('2. Se o nome existir, ele vai ser removido da lista')
novo_nome = input('Diigite um nome : ')

if novo_nome in nomes:
    nomes.remove(novo_nome)
else:
    nomes.append(novo_nome)
    
print(nomes)
