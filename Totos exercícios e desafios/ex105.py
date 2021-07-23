def notas(*num, sit=False):
    """
    => Cria um dicionario com total de notas, maior nota, menor nota, média e situação
    :param num: recebe varias notas
    :param sit: recebe uma condição para exiber ou não a situação do aluno
    :return: retorna um dicionario
    """
    media = sum(num) / len(num)
    aluno = dict()
    aluno['total'] = len(num)
    aluno['maior'] = max(num)
    aluno['menor'] = min(num)
    aluno['média'] = media
    if sit:
        if media >= 7:
            aluno['situação'] = 'BOA'
        elif 5 <= media < 7:
            aluno['situação'] = 'RAZOÁVEL'
        else:
            aluno['situação'] = 'RUIM'
    return aluno


resp = notas(3.5, 2, 6.5, sit=True)
print(resp)
