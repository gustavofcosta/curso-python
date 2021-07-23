palavra = str(input('Digite uma frase para saber se ela é PÁLINDROMO ==> ')).upper()
palavra = ''.join(palavra.split())
inverte = palavra[::-1]

if palavra == inverte:
    print('O inverso de {} é {} e é um PÁLINDROMO!'.format(palavra, inverte))
else:
    print('O inverso de {} é {} e não é um PÁLINDROMO!'.format(palavra, inverte))

