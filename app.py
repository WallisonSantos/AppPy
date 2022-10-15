#
#  Aula   01
#  Módulo Básico
#
print('\n@wallison', 'santos', sep='-', end=' enviar para ')
print('\n@kareen', 'assis', sep='.', end=' via outlook')
print('\n')
#
#
idade = int(input("Qual a sua idade ? "))
peso  = int(input("Qual o seu peso ? "))
altu  = float(input("Qual a sua altura ? "))
nome  = input("Qual o seu nome ? ")
imc   = peso / (altu * altu)
nasc  = 2022-idade
#
#
print( 'idade:{i} nascimeto:{n} peso:{m}'.format( i=idade, n=nasc, m=peso ))
print(f'idade:{idade} nascimeto:{nasc} peso:{peso}')
print(f'idade:{idade} nascimeto:{peso}   imc:{imc:.2f}')
#
#
def warn(string):
    print(
        "[\033[33m w \033[0m] {}".format(string)
    )
warn(nome)
#
#
def error(string):
    print(
        "[\033[31m ! \033[0m] {}".format(string)
    )
error(nome)
#
#
def make_func(i):
    def func():
        return 'this is {0}'.format(i)
    return func
#
#