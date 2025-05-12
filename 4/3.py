import pandas as pd 

data = {
    'variety': ['Chardonnay', 'Chardonnay', 'Pinot Noir', 'Merlot', 'Pinot Noir', 'Merlot'],
    'price':    [10, 15, 20, 12, 35, 8]
}

df = pd.DataFrame(data)


grupo = df.groupby('variety')['price'].agg(['min','max'])

print(grupo)
