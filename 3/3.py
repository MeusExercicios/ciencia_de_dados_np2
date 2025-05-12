# Com que frequência cada carro aparece no conjunto de dados? Crie uma série reviews_per_car mapeando os carros para a contagem

import pandas as pd

valores = {"carros": ["Ferrari", "Ferrari", "Jegue"], "preco": [1000000, 15000, 10]}
df = pd.DataFrame(valores)

# Contar a frequência de cada carro
reviews_per_car = df["carros"].value_counts()

print(reviews_per_car)