frase = str(input('Escreva uma frase: ')).strip()

print('A letra A aparece {} vezes na frase'.format(frase.upper().count('A')))
print('A letra A aparece a primeira vez na posição', frase.upper().find('A')+1)
print('A letra A aparece a última vez na posição', frase.upper().rfind('A')+1)