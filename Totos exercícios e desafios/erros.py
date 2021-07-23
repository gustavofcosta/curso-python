try: # Tentar fazer isso tudo
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou.')
except ZeroDivisionError:
    print('Não é possível dividir um número por zero!')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados!')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}')
#Opcionais
else: # se não houve problema
    print(f'O resultado é {r:.1f}')
finally:# Dando certo ou errado precismaos ferchar
    print('Volte sempre muito obrigado!')