import re


def warn(string):
    print(
        "[\033[31m Caution \033[0m] {}".format(string)
    )


def error(string):
    print(
        "[\033[31m !!! \033[0m] {}".format(string)
    )


def error2(string):
    print(
        "[\033[31m OK \033[0m] {}".format(string)
    )


def is_float(val):
    if isinstance(val, float):
        return True
    if re.search(r'^\-{,1}[0-9]+\.{1}[0-9]+$', val):
        return True

    return False


def is_int(val):
    if isinstance(val, int):
        return True
    if re.search(r'^\-{,1}[0-9]+$', val):
        return True

    return False


def is_number(val):
    return is_int(val) or is_float(val)


#
#   Aula   01
#   Módulo Básico
#
# print("# Formatação de strings")
#
# print('\n@wallison', 'santos', sep='-', end=' enviar para ')
# print('\n@kareen', 'assis', sep='.', end=' via outlook')
# print('\n')
#
idade = int(input("Qual a sua idade ? "))
peso = int(input("Qual o seu peso ? "))
altu = float(input("Qual a sua altura ? "))
nome = input("Qual o seu nome ? ")
imc = peso / (altu * altu)
nasc = 2022-idade
#
# print('idade:{i} nascimeto:{n} peso:{m}'.format(i=idade, n=nasc, m=peso))
# print(f'idade:{idade} nascimeto:{nasc} peso:{peso}')
# print(f'idade:{idade} nascimeto:{peso}   imc:{imc:.2f}')
#
#   Aula   02
#   Módulo Básico
#
print("# Condicionais e Operadores relacionais")
#
# - Menos de 18,5 - abaixo do peso
# - 18,5 a 24,9 - peso saudável
# - 25 a 29,9 - sobrepeso
# - 30 a 39,9 - obeso
# - + de 40 - muito obeso (também conhecido como obeso mórbido)
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
# print(f"quantidade de caracteres nas duas frases: {len(frase1) + len(frase2)}")
# print(f"quantidade de caracteres na frase 1: {len(frase1)} e na frase 2: {len(frase2)}")
#
# Is numerc, Is digit, Is decimal
#
elem1 = input("\nnumero um: ")
elem2 = input("numero dois: ")
#
#


print(elem1.isnumeric())
print(elem2.isnumeric())
#
if elem1.isdigit() and elem2.isdigit():
    elem1 = int(elem1)
    elem2 = int(elem2)

    restOfDiv = elem1 % elem2
    print(f"O resto da divisão de {elem1} por {elem2} é: {restOfDiv}")
else:
    print(
        f"Dados inseridos não permite a realização do cálculo ! => {elem1} e {elem2}")
