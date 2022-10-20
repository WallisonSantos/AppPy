import time
from datetime import datetime, timedelta

import matplotlib.pyplot as plt
from pandas_datareader import data as pdr

print("# Análises financeiras")
#
plt.style.use('ggplot')
#
# selic = sgs.get(('selic', 432), start = '2022-10-01')
# selic.plot(figsize = (15, 10))
#
#
indices = ['^BVSP', '^GSPC']
hoje = datetime.now()
um_ano_atras = hoje - timedelta(days=366)
dado_mercado = pdr.get_data_yahoo(indices, start=um_ano_atras, end=hoje)
#
#
#
#
dado_fechamento = dado_mercado['Adj Close']
dado_fechamento.columns = ['Ibov', 'S&P500']
#
#
#
#
dado_anual = dado_fechamento.resample("Y").last()
dado_mensal = dado_fechamento.resample("M").last()
#
#
retorno_dia = dado_fechamento.pct_change().dropna()
retorno_mes = dado_mensal.pct_change().dropna()
retorno_mes = retorno_mes.iloc[1: , 0]
#
print(retorno_mes)


# retorno_mes.plot(figsize = (15, 10))
# plt.title("Dados Ibovespa e S&P500")
# plt.show()