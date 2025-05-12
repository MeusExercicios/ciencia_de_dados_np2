import pandas as pd

# Produtos mencionados em gaming
gaming_products = pd.DataFrame({
    'product_id': [101, 102, 103, 104],
    'product_name': ['PlayStation 5', 'Xbox Series X', 'Nintendo Switch', 'Gaming Chair'],
    'mentions': [250, 220, 180, 100]
})

# Produtos mencionados em movies
movie_products = pd.DataFrame({
    'product_id': [103, 105, 106],
    'product_name': ['Nintendo Switch', 'Blu-ray Player', 'Netflix Subscription'],
    'mentions': [90, 60, 300]
})

# Juntando os dados (merge com outer para manter todos)
all_products = pd.merge(
    gaming_products,
    movie_products,
    on='product_id',
    how='outer',
    suffixes=('_gaming', '_movies')
)

# Substituir NaN por 0 nos campos de menções
all_products['mentions_gaming'] = all_products['mentions_gaming'].fillna(0)
all_products['mentions_movies'] = all_products['mentions_movies'].fillna(0)

# Soma total de menções por produto
all_products['total_mentions'] = all_products['mentions_gaming'] + all_products['mentions_movies']

# Ordenar pelos mais mencionados
result = all_products[['product_id', 'product_name_gaming', 'product_name_movies', 'total_mentions']] \
    .sort_values(by='total_mentions', ascending=False)

print(result)
