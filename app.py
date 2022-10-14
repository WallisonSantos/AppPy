#
# Módulo Básico
#
print('\n@wallison', 'santos', sep='-', end=' \n')
#
# Formatação de strings
#
idade = 26
peso = 80
altura = 1.80
ano = 2022
nome = 'Wallison'
e_maior = idade > 18
nasc = ano - idade
imc = peso / (altura ** 2)
#
#
print(f'1º ex.: {nome} tem {idade} anos de idade e seu imc é {imc}')
print(f'2º ex.: {nome} tem {idade} anos de idade e seu imc é {imc:.2f}')
print('3º ex.: {} tem {} anos de idade e seu imc é {:.2f}'.format(nome, idade, imc))
print('4º ex.: O {n} nasceu em {ns} e tem {i} anos e peso de {p}'.format(
    n=nome, ns=nasc, i=idade, p=peso))
print('__________________________________________________________________________________________________')
#
#
nome = input("Qual o seu nome ? \n")
idade = input("Qual a sua idade ? \n")
nascimento = 2022 - int(idade)
print(
    f'Tipo da variável nome:{type(nome)} idade:{type(idade)} nascimento:{type(nascimento)}')
print(f'Valor da variável nome:{nome} idade:{idade} nascimento:{nascimento}')
#
#
numero_1 = int(input("Primeiro valor: "))
numero_2 = int(input("Segundo valor: "))
#
par1p = (numero_1 % 2 == 0)
print(par1p)
par2p = (numero_2 % 2 == 0)
print(par2p)
imp1p = (numero_1 % 2 != 0)
print(imp1p)
imp2p = (numero_2 % 2 != 0)
print(imp2p)
#
#
if par1p and par2p:
    calculo = numero_1 % numero_2
elif par1p and imp1p:
    calculo = numero_2 % numero_1

print(f'O cálculo de { numero_1 } % { numero_2 } é = { calculo }')
#
#
