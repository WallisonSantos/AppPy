#  Aula   01
#  Módulo Básico
#  Formatação de strings
#
print('\n@wallison', 'santos', sep='-', end=' enviar para ')
print('\n@kareen', 'assis', sep='.', end=' via outlook')
print('\n')
#
idade = int(input("Qual a sua idade ? "))
peso  = int(input("Qual o seu peso ? "))
altu  = float(input("Qual a sua altura ? "))
nome  = input("Qual o seu nome ? ")
imc   = peso / (altu * altu)
nasc  = 2022-idade
#
print( 'idade:{i} nascimeto:{n} peso:{m}'.format( i=idade, n=nasc, m=peso ))
print(f'idade:{idade} nascimeto:{nasc} peso:{peso}')
print(f'idade:{idade} nascimeto:{peso}   imc:{imc:.2f}')
#
#   Aula   02
#   Módulo Básico
#   Condicionais e Operadores relacionais
#
# - Menos de 18,5 - abaixo do peso
# - 18,5 a 24,9 - peso saudável
# - 25 a 29,9 - sobrepeso
# - 30 a 39,9 - obeso
# - + de 40 - muito obeso (também conhecido como obeso mórbido)
#
def warn(string):
    print(
        "[\033[31m Caution \033[0m] {}".format(string)
    )
#
def error(string):
    print(
        "[\033[31m !!! \033[0m] {}".format(string)
    )
#
def error2(string):
    print(
        "[\033[31m OK \033[0m] {}".format(string)
    )
#
#
print("# Condicionais e Operadores relacionais")
#
#
if (imc == 18.5):
    print("medida está abaixo")
    error(imc)
elif (imc > 18.5 and imc < 24.9):
    print("saudável")
    error2(imc)
elif (imc >= 24.9 and imc < 29.9):
    print("sobrepeso")
    error(imc)
elif (imc >= 29.9 and imc < 39.9):
    print("obeso")
    error(imc)
elif (imc >= 39.9):
    print("muito obeso (também conhecido como obeso mórbido)")
    warn(imc)
else:
    print("tente novamente")
#
#