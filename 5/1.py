import pandas as pd
import numpy as np

# Criando um dataset de exemplo
data = {
    'country': ['Italy', 'US', 'US', 'France', 'Spain'],
    'points': [95, 89, 88, 92, 87],
    'price': [120.0, 15.0, None, 50.0, None],
    'region_1': ['Tuscany', 'Napa Valley', None, 'Bordeaux', None]
}

reviews = pd.DataFrame(data)

print(reviews['points'].dtype)
