#
#  Aula   01
#  Módulo Básico
#
from mailbox import NotEmptyError


print('@wallison', 'santos', sep='-', end=' enviar para ')
print('\n@kareen', 'souza', sep='-', end=' ')
print('\ndados de cpf: ', sep='-', end=' ')
print('824','176','070', sep='.', end='-18')
#
#
idade  = input("Qual a sua idade ? ")
nome   = input("Qual o seu nome ")

print( 'idade:{i} nascimeto:{n} mês:{m}'.format(i=idade, n=nasc, m=mes))
print(f'idade:{idade} nascimeto:{nascimeto} mês:{mes}')
print(f'ome:{nome} peso:{peso} imc:{imc:.}')