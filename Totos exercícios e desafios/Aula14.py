'''for c in range(1, 10):
    print(c)
print('FIM')'''

'''
c = 1
while c < 10:
    print(c)
    c = c + 1
print('FIM')'''

'''r = 'S'
while r == 'S':
    n = int(input(('Digite um numero: ')))
    r = str(input(('Quer continar [S/N] '))).upper()
print('Fim')'''


n = 1
par = 0
impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par = par + 1
        else:
            impar = impar + 1
print('Você digitou {} números pares e {} impares.'.format(par, impar))
