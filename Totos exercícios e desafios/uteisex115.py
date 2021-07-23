def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('ERRO: por favor, digite um número do menu.')
            continue
        except KeyboardInterrupt:
            print('Usuário preferiu não digitar esse número.')
            return 0
        else:
            return n


def linha(tam=42):
    return '-' * 42


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(list):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in list:
        print(f'{c} - {item}')
        c += 1
    print(linha())
    opc = leiaInt('Sua Opção: ')