lista = []
lista.append(input('Digite uma expressão: '))
pos = a = f = 0

while pos in len(lista):
    if pos == '(':
        a += 1
    if pos == ')':
        f += 1

print(a)
print(f)



