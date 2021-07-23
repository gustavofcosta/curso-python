def fatorial(num, show=False):
    """
    ==> Calcula o Fatorial de um número.
    :param num: O número a ser calculado.
    :param show: (opcional) Mostra ou não a conta
    :return: O valor  do Fatorial de um número n.
    """
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(f'{c}',  end=' ')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


print(fatorial(5, True))
help(fatorial)