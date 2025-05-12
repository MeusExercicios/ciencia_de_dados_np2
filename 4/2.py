import pandas as pd 

data = {
    'price': [10, 15, 10, 20, 15, 3300, 4],
    'points': [85, 88, 90, 92, 87, 96, 80]
}

df = pd.DataFrame(data)


best = df.groupby('price')['points'].max().sort_index()

print(best)