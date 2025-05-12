# EXERCÍCIO: Identificar o melhor custo-benefício entre vinhos
# Objetivo: Criar um DataFrame com informações de vinhos, calcular o custo-benefício (pontos por preço)
# e identificar qual vinho oferece o melhor valor com base nessa métrica.

import pandas as pd  # Importa a biblioteca pandas para manipulação de dados

# Criação do dicionário com os dados dos vinhos
data = {
    "title": ["Wine A", "Wine B", "Wine C", "Wine D", "Wine E"],  # Títulos dos vinhos
    "points": [90, 85, 92, 88, 95],  # Pontuação de avaliação de cada vinho
    "price": [45, 30, 60, 22, 80]    # Preço de cada vinho
}

# Criação do DataFrame a partir do dicionário
df = pd.DataFrame(data)

# Criação de uma nova coluna chamada 'points_per_price', que representa o custo-benefício
# Calculamos isso dividindo os pontos pela respectiva faixa de preço
df['points_per_price'] = df['points'] / df['price']

# Exibe o DataFrame com a nova coluna
print(df)

# Encontra o índice do vinho com a melhor relação custo-benefício
melhorIndex = df['points_per_price'].idxmax()

# Usa .loc para localizar o título do vinho que possui o maior 'points_per_price'
bargain_wine = df.loc[melhorIndex, "title"]

# Exibe o nome do vinho com o melhor custo-benefício
print(bargain_wine)
