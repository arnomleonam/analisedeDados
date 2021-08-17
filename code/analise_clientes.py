#importando as bibliotecas
import pandas as pd
import matplotlib.pyplot as plt

#definino a fonte
font = {'family' : 'normal',
        'weight' : 'bold',
        'size'   : 13}
plt.rc('font', **font)

#definindo o estilo do plt
plt.style.use("Solarize_Light2")

#lendo o arquivo excel
df = pd.read_excel("/home/arnomleonam/Área de Trabalho/Analise_de_Estimativa/datasets/AdventureWorks.xlsx")

#definindo a organização do gráfico
df.groupby("ID Cliente")["Valor Venda"].max().nlargest().plot.barh(title="Clientes que mais Compraram")

#definindo o tamanho da tela
fig = plt.gcf()
fig.set_size_inches(18.5, 10.5)

#definindo od parametros do grafico
plt.xlabel("Vendas")
plt.ylabel("ID dos Clientes")
plt.autoscale()

#gerando o arquivo de imagem
plt.savefig("clientes_que_mais_compraram.png", dpi=300)
