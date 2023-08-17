# Importando as bibliotecas
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use("seaborn")
     

# Upload do arquivo
from google.colab import files
arq = files.upload()
     

# Criando nosso DataFrame
df = pd.read_excel("AdventureWorks.xlsx")
     

# Visualisando as  primeiras linhas
df.head()
     

# Quantidade de linhas e colunas
df.shape()
     

# Verificando tipos de dados
df.dtypes()
     

# Qual a receita?
df["Valor Venda"].sum()
     

# Qual o Custo Total?
df["Custo Total"] = df["Custo Unitário"].mul(df["Quantidade"]) # Criando coluna de custo
     

df.head()
     

# Agora que temos a receita e custo e o total, podemos achar o Lucro total
# Vamos criar uma coluna de Lucro que será Receita - Custo
df["Lucro"] = df["Valor Venda"] - df["Custo"]
     

df.head(1)
     

# Total Lucro
round(df["Lucro"].sum(),2)
     

# Criando uma coluna com total de dias para enviar o produto
df["Tempo_envio"] = df["Data Envio"] - df["Data Venda"]
     

# Extraindo apenas os dias
df["Tempo_envio"] = (df["Data Envio"] - df["Data Venda"]).dt.days
     

df.head(1)
     

# Verificando o tipo da coluna Tempo_Envio
df["Tempo_envio"].dtypes
     

# Média do tempo de envio por Marca
df.groupby("Marca")["Tempo_envio"].mean()
     

# Verificando se temos dados faltantes
df.isnull().sum()
     

# Vamos agrupar por ano e marca
df.groupby([df["Data Venda"].dt.year, "Marca"])["Lucro"].sum().reset_index()
lucro_ano
     

pd.options.display.float_format = '(:20,.sf)'.format
     

# Resetando o index
lucro_ano = df.groupby([df["Data Venda"].dt year, "Marca"])["Lucro"].sum().reset_index()
     

# Qual o total de produtos vendidos?
df.groupby("Produto")["Quantidade"].sum().sort_values(ascending=False)
     

# Gráfico total de produtos vendidos
df.groupby("Produtos")["Quantidade"].sum().sort_values(ascending=False).plot.barh(title="Total Produtos Vendidos")
plt.xlabel("Total")
plt.ylabel("Produtos");
     

# Selecionando apenas as vendas de 2009
df_2009 = df[df["Data Venda"].dt.year == 2009]
     

df_2009.head()
     

# Gráfico de Boxplot
plt.boxplot(df["Tempo_envio"]);
     

# Histograma
plt.hist(df["Tempo_envio"]);
     

# Tempo minimo de envio
df["Tempo_envio"].min()
     

# Identificando o Outlier
df[df["Tempo_envio"] == 20]
     

df.to_csv("df_vendas_novo.csv", index=False)