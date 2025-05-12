import pandas as pd

# Criando um DataFrame fictício
data = {
    'wine_name': ['Cabernet', 'Merlot', 'Syrah', 'Chardonnay', 'Pinot Noir', 'Riesling', 'Zinfandel'],
    'taster_twitter_handle': ['@johnwine', '@winelover', '@johnwine', '@winelover', '@vinotaster', '@johnwine', None]
}

df = pd.DataFrame(data)

review = df['taster_twitter_handle'].value_counts()

print(review)