import pandas as pd

# Criando um dataset de exemplo
data = {
    'country': ['Italy', 'US', 'US', 'France', 'Spain'],
    'points': [95, 89, 88, 92, 87],
    'price': [120.0, 15.0, None, 50.0, None],
    'region_1': ['Tuscany', 'Napa Valley', None, 'Bordeaux', None],
    'region_2': ['Fortaleza', 'São Paulo', 'Maceio', 'Brasilia', 'Manaus']
}

reviews = pd.DataFrame(data)

reviews.index.name = 'wines'


print(reviews)
