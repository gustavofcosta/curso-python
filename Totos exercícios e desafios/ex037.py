
num = int(input('Dite um numero inteiro: '))
print('--'*10)
print('''Escolha uma das opções para a conversção:
[ 1 ] Converter para BINÀRIO
[ 2 ] Converter para OCTAL
[ 3 ] Converter para HEXADECIMAL''')
tecla = int(input('Sua opção: '))

if tecla == 1:
    print('O numero {} em Binario é {}'.format(num, bin(num)[2:]))
elif tecla == 2:
    print('O numero {} em Octal é {}'.format(num, oct(num)[2:]))
elif tecla == 3:
    print('O numero {} em Hexadecimal é {}'.format(num, hex(num)[2:]))
else:
    print('Não possui esta opção.')







