import time
import warnings
from datetime import datetime, timedelta

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pandas_datareader import data as pdr

warnings.filterwarnings('ignore')



print("# Análises financeiras")
plt.style.use('ggplot')
plt.title("Dados Ibovespa e S&P500")
#
#
# selic = sgs.get(('selic', 432), start = '2022-10-01')
# selic.plot(figsize = (15, 10))
# plt.show()
#
#
indices = ['^BVSP', '^GSPC']
hoje = datetime.now()
um_ano_atras = hoje - timedelta(days=366)
#
dado_mercado = pdr.get_data_yahoo(indices, start=um_ano_atras, end=hoje)
dado_mercado.plot(figsize = (15, 10))
#
#
#
dado_fechamento = dado_mercado['Adj Close']
dado_fechamento.columns = ['Ibov', 'S&P500']
#dado_fechamento.plot(figsize = (15, 10))
#
#
#
dado_anual = dado_fechamento.resample("Y").last()
dado_mensal = dado_fechamento.resample("M").last()
#dado_mensal.plot(figsize = (15, 10))
#dado_anual.plot(figsize = (15, 10))