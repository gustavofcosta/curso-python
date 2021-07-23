print('=='*50)
print('Calculadora de desconto ou juros, conforme a forma de pagamento.')
print(' '*50)

produto = float(input('informe o valor do produto R$ '))

print('Qual é a forma de pagamento?')
print(' '*50)
print('''
[1] - À vista dinheiro/cheque 10% de desconto. 
[2] - À vista cartão 5% de descont 
[3] - Em até 2 vezes no cartão preço normal. 
[4] - 3 vezes ou mais no cartão 20% de juros. ''')

precione = int(input('Qual é a opção? '))

if precione == 1:
    print('À vista dinheiro/cheque 10% de desconto valor de R${}'.format(produto * 0.9))
elif precione == 2:
    print('À vista com cartão 5% de desconto, valor de R${}'.format(produto * 0.95))
elif precione == 3:
    print('Em até 2 vezes no cartão preço normal, valor de R${}'.format(produto))
elif precione == 4:
    quantas = int(input('Quantas parcelas: '))
    divi = (produto*1.2) / quantas
    print('{} X {} no cartão 20% de juros, valor de R${}'.format(quantas, divi, produto*1.2))
