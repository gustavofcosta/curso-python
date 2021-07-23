dados = dict()
gols = list()
#Ler nome do jogador
dados['nome'] = str(input('Nome do jogador: '))
#Ler quantas partidas ele jogou
partidas = int(input((f"Quantas partidas {dados['nome']} jogou? ")))
#Ler a quantidade de gols feitas em cada partida deve ser colocadas em uma lista
for g in range(1, partidas + 1):
    gols.append(int(input(f"Quantos gols {dados['nome']} fez na partida {g}? ")))
#Tudo deve ser quardado em um dicionario incluindo o total de gols feitos durante o campeonato
dados['gols'] = gols
total = sum(gols)
dados['total de gols'] = total
print('-='*22)
print(dados)
print('-='*22)
# Organizar dados
for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}.')
print('-='*22)
print(f"O jogador {dados['nome']} jogou {partidas} partidas.")
c = 1
for i, v in enumerate(gols):
    print(f'   => na partida {i + 1}, fez {v} gols.')
print(f'Foi um total de {dados["total de gols"]} gols')