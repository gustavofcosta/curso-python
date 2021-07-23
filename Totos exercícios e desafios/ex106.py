def ajuda(com):
    help(com)
def titulo(msg, cor=0):
    tam = len(msg)
    print('~' * tam)
    print(msg)
    print('~' * tam)

comando = ''
while True:
    titulo('SITEMA DE AJUDA PyHeLP')
    comando = str(input('Função ou Biblioteca> '))
    if comando.upper() == 'FIM' :
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO')