num = int(input('Digite um número para ver sua tabuada: '))
print('-'*12)
for c in range(1, 11):
    print('{} x {:2} = {}'.format(c, num, num*c))

