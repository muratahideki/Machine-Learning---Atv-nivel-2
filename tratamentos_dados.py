import pandas as pd
#1. Quais as colunas do Dataset? 
db = pd.read_csv("mymoviedb.csv", nrows=100)
print(db.head(0))

#2. Qual tamanho do DataSet? (Shape)
print(db.shape)

#3. Quantas linhas? 
print(db.shape[0])

#4. Qual o tipo de variável de cada coluna? 

for i in range(db.shape[1]):
    colunas =  db.iloc[0,i]
    tipo_colunas = type(colunas)
    print(tipo_colunas)

#5. Qual o filme com maior número de votaçôes?

i= db['Vote_Count'].idxmax()  # índice da linha com maior voto
nome = db.loc[i,"Title"]
print(nome)

#6. Qual filme teve a maior nota (critério de desempate é o filme com mais votos) 

i= db['Vote_Average'].idxmax()  # índice da linha com maior voto
nome = db.loc[i,"Title"]
print(nome)

# 7. Existem dados duplicados?

dados_duplicados = db[db.duplicated()]
print(dados_duplicados)
print("não há dados duplicados")

# 8. Existem valores nulos? Qual a quantidade e a proporção em relação ao total de dados?

valores_nulos = db.isnull().any()
print(valores_nulos)


# 9. Quais insights é possivel obter desses dados? Gere gráficos.

import matplotlib.pyplot as plt

plt.figure(figsize=(10,6))
db['Vote_Count'].hist(bins=50)
plt.title('Distribuição do número de votos dos filmes')
plt.xlabel('Número de votos')
plt.ylabel('Quantidade de filmes')
plt.show()

