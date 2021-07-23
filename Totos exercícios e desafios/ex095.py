time = list()
dados = dict()
gols = list()
#Ler nome do jogador
while True:
    dados['nome'] = str(input('Nome do jogador: '))
    #Ler quantas partidas ele jogou
    partidas = int(input((f"Quantas partidas {dados['nome']} jogou? ")))
    gols.clear()
    #Ler a quantidade de gols feitas em cada partida deve ser colocadas em uma lista
    for g in range(1, partidas + 1):
        gols.append(int(input(f"Quantos gols {dados['nome']} fez na partida {g}? ")))
    #Tudo deve ser quardado em um dicionario incluindo o total de gols feitos durante o campeonato
    dados['gols'] = gols[:]
    total = sum(gols)
    dados['total de gols'] = total
    time.append(dados.copy())
    while True:
        resp = str(input('Quer continuar [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('Erro! tente denovo somente S ou N')
    if resp == 'N':
        break
print('-='*22)
print('Cod ', end='')
for i in dados.keys():
    print(f'{i:<15}', end='')
print()
print('-='*22)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-='*22)
while True:
    busca = int(input('Mostrar dados de qual jogador (999 para parar)'))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'Erro não existe jogador com código {busca}!')
    else:
        print(f' == LEVANTAMENTO DO JOGADOR{time[busca] ["nome"]} ')
        for i, g in enumerate(time[busca]['gols']):
            print(f'    No jogo {i} fez {g} gols.')
    print('-'*30)