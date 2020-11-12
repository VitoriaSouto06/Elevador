from elevador import Elevador

e = Elevador()
e.inicializa()

while True:
    print('''
        Escolha entre as opções
        1 - Subir 
        2 - Descer
        3 - Adicionar pessoa
        4 - Retirar pessoa
        5 - Verificar número de pessoas
        6 - Verificar andar atual
        7 - Fechar
        ''')
    op = int(input('Opção: '))


    if op == 1:
        e.sobe()

    elif op == 2:
        e.desce()

    elif op == 3:
        e.entra()

    elif op == 4:
        e.sai()

    elif op == 5:
        print(e.capacidade)

    elif op == 6:
        print(e.andarAtual)

    elif op == 7:
        exit()
