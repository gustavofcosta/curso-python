n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))

media = (n1 + n2)/2

if media < 5:
    print('\33[31mVocê foi reprovado!')
elif media >= 5 and media <= 6.9:
    print('\33[33mVocê esta de recuperação!')
else:
    print('\33[32mVocê foi aprovado! Parabens...')
