print('Simulador de financiamento de imovél.')

print('=='*10)

casa = float(input('Qual o valor do financiamento? R$'))
sala = float(input('Qual o salario do comprador? R$'))
anos = int(input('Em quantos anos pretende financiar? '))

parc = casa / (anos*12)
cores = {'verde':'\33[32m', 'vermelha':'\33[31m'}
if parc < (sala*0.3):
    print('\33[32mParabens você pode financiar o imovel, e a parcela mensal será de R${:.2f}'.format(parc))
else:
    print('\33[31mSentimos muito seu credito não pode ser aprovado!')
