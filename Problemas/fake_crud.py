"""
=================================================================
=====================     Fake Crud   ===========================
=================================================================

O que é um CRUD?
Crud é um sistema básico que faz 4 operações :
    C - Create (cria)
    R - Retrieve (pega)
    U - Update (atualiza)
    D - Delete (apaga)

Cruds possuem bancos de dados e comunicação via rede.
Por motivos de facilidades, usaremos :
    > Escrita e leitura de arquivos para simulação do banco
    > Entrada e saída no terminal para saída e entrada de dados

=================================================================
=================================================================
"""
def insere():
    # Escreve dado em uma arquivo específico ou cria um arquivo
    pass


def pega():
    # Pega dado de um arquivo específico
    pass


def atualiza():
    # Atualiza dado de um arquivo específico
    pass


def remove():
    # OBS : vocẽ quase NUNCA deve fazer isso, mas, aprender não faz tão mal kk
    # Remove dado de um arquivo específico
    pass


def executa_opcao(opcao):
    if opcao == 1:
        insere()
    elif opcao == 2:
        pega()
    elif opcao == 3:
        atualiza()
    else:
        remove()


def run():
    menu()
    opcao = int(input(""))
    while opcao < 1 or opcao > 5:
        print("\n#####################")
        print("ERRO: Opção inválida!")
        print("#####################")
        print("\nDigite sua opcao corretamente : ")
        opcao = int(input(""))

    if opcao == 5:
        return False
    else:
        executa_opcao(opcao)
        return True


def menu():
    print("\n======== MENU ========\n")
    print("1. Inserir novo dado")
    print("2. Pegar dado")
    print("3. Atualizar dado")
    print("4. Remover dado")
    print("5. Encerrar")
    print("\nDigite a opção desejada : ")


def loop():
    keep_running = True
    while keep_running:
        keep_running = run()
    print("...encerrando...tchau :*")


loop()