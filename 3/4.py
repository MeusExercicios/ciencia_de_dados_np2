 # criar a variável centered_price subtraindo a média da coluna "preco" de cada valor da coluna.

import pandas as pd

valores = {"carros": ["Ferrari", "Ferrari", "Jegue"], "preco": [1000000, 15000, 10]}
df = pd.DataFrame(valores)

# Contar a frequência de cada carro
media_carros = df["preco"].mean()


centered_price = df["preco"] - media_carros

print(centered_price)