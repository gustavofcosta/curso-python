frase = str(input('Digite uma frase para saber se ela é PÁLINDROMO ==> ')).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
inverte = ''
for letra in range(len(junto) -1, -1, -1):
    inverte = inverte + junto[letra]
print('O inverso de {} é {}'.format(junto, inverte))
if inverte == junto:
    print('E temos um palíndromo')
else:
    print('E não temos um palíndromo')
