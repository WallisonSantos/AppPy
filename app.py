#
#  Aula   01
#  Módulo Básico
#
print('@wallison', 'santos', sep='-', end=' enviar para ')
print('\n@kareen', 'souza', sep='-', end=' ')
print('\ndados de cpf: ', sep='-', end=' ')
print('824','176','070', sep='.', end='-18')
#
#
idade = int(input("Qual a sua idade ? "))
peso  = int(input("Qual o seu peso ? "))
altu  = int(input("Qual a sua altura ? "))
nome  = input("Qual o seu nome ? ")
imc   = peso / (altu * altu)
nasc  = 2022-idade
#
#
print( 'idade:{i}     nascimeto:{n}    peso:{m}'.format( i=idade, n=nasc, m=peso ))
print(f'idade:{idade} nascimeto:{nasc} peso:{peso}')
print(f'idade:{idade} nascimeto:{peso}  imc:{imc:.}')