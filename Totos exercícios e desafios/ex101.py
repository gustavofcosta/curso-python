def voto(ano):
    from datetime import date
    i = date.today().year - ano
    if i < 16:
        return f'Com {i} anos: NÃO VOTA.'
    if 18 <= i < 65:
        return f'Com {i} anos: VOTO OBRIGATÓRIO.'
    if i >= 65:
        return f'Com {i} anos: VOTO OPCIONAL.'

print('=-'*20)
nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))

