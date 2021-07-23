dados = []
tabelamedia = []
while True:
    nome = str(input('Nome do aluno: ')).strip().title()
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) /2
    tabelamedia.append([nome,[nota1, nota2], media])
    sair = str(input('Quer Continuar? [S/N]: '))
    if sair not in 'Ss':
        break
print('=-'*20)
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
print('--'*20)
for i, c in enumerate(tabelamedia):
    print(f'{i:<4}{c[0]:<10}{c[2]:>8.1f}')
print('--'*30)
while True:
    n = int(input('Quer mostrar nota de qual aluno? (999 interrompe): '))
    if n == 999:
        break
    if n <= len(tabelamedia) - 1:
        print(f'Notas de {tabelamedia[n][0]} são {tabelamedia[n][1]}')

    elif