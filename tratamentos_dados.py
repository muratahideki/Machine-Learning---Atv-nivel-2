import pandas as pd
#1. Quais as colunas do Dataset? 
db = pd.read_csv("mymoviedb.csv", nrows=100)
print(db.head(0))

#2. Qual tamanho do DataSet? (Shape)
print(db.shape)

#3. Quantas linhas? 
print(db.shape[0])

