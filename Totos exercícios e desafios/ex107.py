import moeda

p = float(input('Digiteo preço R$'))
print(f'A metade de {p} é R${moeda.metade(p)}')
print(f'O dobro de {p} é R${moeda.dobrar(p)}')
print(f'Aumentar 10%, temos R${moeda.aumentar(p, 10)} ')
print(f'Reduzir 13%, temos R${moeda.diminuir(p, 13)} ')
