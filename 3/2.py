# Mostrar os nomes dos carros e remover as duplicatas
import pandas as pd

valores = {"carros": ["Ferrari", "Ferrari", "Jegue"], "preco": [1000000, 15000, 10]}

df = pd.DataFrame(valores)

print(df["carros"].drop_duplicates())
