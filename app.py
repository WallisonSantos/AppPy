import re
import random
from pandas_datareader import data as pdr
import pandas as pd
import numpy as np
from datetime import datetime
from datetime import timedelta
import mplfinance as mpf
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import matplotlib.dates as mdates
import mplcyberpunk
import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import requests
from bcb import currency
from bcb import sgs
from fpdf import FPDF
from matplotlib.dates import date2num
import warnings
warnings.filterwarnings('ignore')


def warn(string): print(f'[\033[31m Caution \033[0m] {string:.2f}')
def error(string):print(f'[\033[31m !!! \033[0m] {string:.2f}')
def error2(string):print(f'[\033[31m OK \033[0m] {string:.2f}')

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

print("# Condicionais e Operadores relacionais")


abaixo = "Menos de 18,5 - abaixo do peso"
saudavel = "18,5 a 24,9 - peso saudável"
sobrepeso = "25 a 29,9 - sobrepeso"
obeso = "30 a 39,9 - obeso"
morbido = "40 ou mais - muito obeso (também conhecido como obeso mórbido)"

peso = 80 # input("Digite o seu peso: ")
altu = 1.80 # input("Digite a sua altura: ")
numc = random.randint(10, 20)

if is_number(peso) or is_number(altu):

#    if is_int(peso) and is_int(altu):
#        peso = int(peso)
#        altu = int(altu)
#    elif is_float(peso) and is_float(altu):
#        peso = float(peso)
#        altu = float(altu)
#    elif is_int(peso) and is_float(altu):
#        peso = int(peso)
#        altu = float(altu)
#    elif is_float(peso) and is_int(altu):
#        peso = float(peso)
#        altu = int(altu)

    imc = peso / (altu * altu)

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

print("# Análises financeiras")

selic = sgs.get(('selic', 432), start = '2022-10-01')

plt.style.use('ggplot')
selic.plot(figsize = (15, 10))

plt.title("Taxa de juros - Meta Selic definida pelo Copom - %a.a")
plt.show()