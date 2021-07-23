# ESCREVER ALGO NA TELA
print('Hello World')

# TIPOS PRIMITIVOS E SAÍDAS DE DADOS
# int = numeros inteiros
# float = numeros com pontos flutoantes
# bool = True ou False
# str = igual a strings

# ' = ' -- > RECEBE
n = input('Digite um número')

# SAÍDA DE DADOS
input('Digite um número')

# OPERADORES ARITIMÉTICOS
# +  = ADIÇÃO
# -  = SUBTRAÇÃO
# *  = MUTIPLICAÇÃO
# /  = DIVISÃO
# ** = POTÊNCIA
# // = DIVISÃO INTEIRA
# %  = RESTO DA DIVISÃO

# METODOS
import random
from random import randint

# MANIPULANDO CADEIA DE TEXTO
frase = (Curso em video python)  #= possui 20 caracteres contando com espaços do 0 a 20
print(frase)
print(frase[9]) # printa o 9 caracter
print(frase[9:13])  # printa do 9 caracter ate o 12 sempre um apenos porque começa do 0
print(frase[9:21:2])  # printa do 9 caracter até o 21 ppulando de 2 em 2
print(frase[:5]) # printa do 0 até 5
print(frase[15:]) # printa do 15 até o final
print(frase[9::3]) # printa do 9 até o final pulando de 3 em 3
len(frase) # conta e printa o número de todos caracteres que possui dentro da frase = 21 letras e espaços
frase.count('o') # printa quantas vezes existe a letra 'o' minuscula na frase
frase.count('o', 0 , 13) # printa quantas vezes exite a letra 'o' minuscula entre o inicio até a 12 caracter - 1 porque começa do 0
frase.find('deo') # printa onde esta posicionado o 'deo' na frase
curso in frase = # DENTRO DA FRASE EXISTE A CURSO --- RETORNO SERA TRUE OU FALSE
frase.replace('python', 'Android') # = TROCAR --- ELE VAI PROCURAR POR PYTHON E SUBISTITUIR POR ANDROID
frase.upper() # ele pega a frase troca tudo para maiuscula
frase.upper() # ele pega a frase troca tudo para minusculo
frase.capitalize() # ele coloca somenta a primeira frase em maiuscula
frase.title() # ele coloca totas as palavras com letras maiuscula
frase.strip() # Remove todos os espaços do inicio e do fim da frase
frase.rstrip() # Remove todos os espaços a direta da frase
frase.lstrip() # Remove todos os espaços a esquerda da frase
frase.split() # remove os espaços do meio forma uma lista por palavra(onde tiver espaços)
'-'.join(frase) # faz o contrario do split '-' coloca traço ' ' coloca espaço

if = se #condiçao
else = #senão sem condição
elif  = #senão se outra indição


Vermelho = print('\033[0;30;41mOla mundo')
Azul = print('\033[0;33;44mOla mundo')
amarelo = print('\033[1;35;43mOla mundo')
verde = print('\033[30;42mOla mundo')
preto = print('\033[mOla mundo')
cinza = print('\033[7;30mOla mundo\033[m')


#   LAÇO DE REPETIÇÃO FOR
for c in range(0, 8): # ele conta ou repete de 0 até 7
for c in range(0, 8, 2):  # ele conta ou repete de 0 até 7 pulando de 2 em 2

# ESTRUTUTA DE REPETIÇÃO WHILE SERVE QUANDO NÃO SABEMOS O RANGE
while == 0:
    # SÓ PARA QUANDO A CONDIÇÃO FOR 0

not in # em quanto não estiver na condição informada não para

in # quanto estiver na condição informada para

while True:
    if c in 0:
        break # para a estrutura de repetição


#TUPLAS SÃO IMUTAVEIS = NÃO PODE SER MUDADA DEPOIS DE DECLARADA
tuplas = (gustavo, vanessa, bernardo)


#LISTAS PODE SER MUDADAS OU ADICIONADAS
lista = []
lista = list()

lista.insert(0, 5) # na posição 0 sera inserido 5 e o que estiver na posição 0 vai para frente
#deleta itens da lista
del lista[3]
lista.pop(3)
lista.remove('item')

lista.sort() # colcoa o que estiver na lista em ordem crescente
lista.sort(reverse=True) # coloca o que estiver na lista em ordem decrecente
len(lista) # conta quantos itens tem na lista
lista.append(5) # adiciona o numero 5 na lista

#LISTAS COMPOSTAS
lista = []
dados = list()
lista.append(4)
dados.append(lista[:]) # [:] fazer uma copia

dado = []
galera = list()
for c in range(0, 3):
    dado.append(int(input('Digite um numero')))
    dado.append(int(input('Digite um idade')))
    galera.append(dado[:])
    dado.clear()

# DICIONARIOS
#podemos colocar uma lista dentro do dicionario
dicionairos = dict()
dicionarios = {}
dados = {'nome':'pedro',
         'idade':25   }
print(dados['nome'])
print(dados['idade'])
dados['sexo'] = 'M' # adiciona um elemento no dicionario

del daodos['idade']

print(dado.values()) #Retorna os valores do dicionario
print(dado.keys()) #Retorna as chaves que titulos
print(dado.items()) # retorna todos os dados do dicionario

for k, v in dados.itens:
    print(f'{k} {v}')

print(locadora[0]['ano']) # para quando um dicionario estiver dentro de uma lista


estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla de Estado: '))
    brasil.append(estado.copy()) # [:] não pode fazer fatiamento em uma lista para dicionario
                                  # .copy somente para dicionario


aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['média'] = float(input('Média: '))








