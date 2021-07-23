print('-=' * 12)
primeiro = int(input('Informe o termo: '))
raz = int(input('Informe a razão: '))
print('-=' * 12)

termo = primeiro
c = 1

while c <= 10:
    print('{} ➔'.format(termo), end=' ')
    termo = termo + raz
    c = c + 1
print('Fim')


