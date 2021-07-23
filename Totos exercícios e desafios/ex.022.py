nome = str(input("Qual é seu nome completo: ")).strip()
print('Seu nome é:',nome)
print('Nome com todas letras maiúsculas:',nome.upper())
print('Nome com todas letras minúsculas:',nome.lower())

print('Nome possui {} letras'.format(len(nome) - nome.count(' ')))
pname = (nome.split())
print('O primeiro nome é {} e possui {} letra'.format(pname[0],len(pname[0])))