import pandas as pd

# Exemplo de dados com variedades e preços
data = {
    'variety': ['Chardonnay', 'Chardonnay', 'Pinot Noir', 'Merlot', 'Pinot Noir', 'Merlot', 'Cabernet', 'Cabernet'],
    'price':    [10, 15, 20, 12, 35, 8, 200, 300]
}

df = pd.DataFrame(data)

# Agrupa por variety e calcula o preço mínimo e máximo
min_max_prices = df.groupby('variety')['price'].agg(['min', 'max'])

# Ordena primeiro pelo preço mínimo (desc), depois pelo máximo (desc)
sorted_varieties = min_max_prices.sort_values(by=['min', 'max'], ascending=[False, False])

# Exibe o resultado
print(sorted_varieties)
