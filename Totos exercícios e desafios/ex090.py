aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['média'] = float(input(f"Média de {aluno['nome']}: "))
if aluno['média'] >= 7:
    aluno['situação'] = 'APROVADO'
elif 5 <= aluno['média'] < 7:
    aluno['situação'] = 'RECUPERAÇÃO'
else:
    aluno['situação'] = 'REPROVADO'
print('=-'*25)
for k, v in aluno.items():
    print(f'O {k} é igual a {v}')







