print('-=' * 12)
primeiro = int(input('Informe o termo: '))
raz = int(input('Informe a razão: '))
print('-=' * 12)

termo = primeiro
c = 1
mais = 10
total = 0
while mais != 0:
    total = total + mais
    while c <= total:
        print('{} ➔'.format(termo), end=' ')
        termo = termo + raz
        c = c + 1
    print('Pausa')
    mais = int(input('Quer mostrar mais quantos: '))




