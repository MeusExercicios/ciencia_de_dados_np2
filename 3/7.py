# EXERCÍCIO: Classificar vinhos com estrelas
# Objetivo: Criar uma nova coluna que atribua uma classificação por estrelas com base no país e na pontuação dos vinhos.

import pandas as pd  # Importa a biblioteca pandas

# Criação do DataFrame com pontuação e país de origem dos vinhos
df = pd.DataFrame({
    "points": [95, 89, 76, 100, 85],
    "country": ["Canada", "US", "France", "Canada", "US"]
})

# Define uma função que classifica os vinhos com base em regras:
# - Se for do Canadá → 3 estrelas (prioridade)
# - Se tiver 95 pontos ou mais → 3 estrelas
# - Se tiver 85 a 94 pontos → 2 estrelas
# - Caso contrário → 1 estrela
def definir_estrelas(row):
    if row["country"] == "Canada":
        return 3
    elif row["points"] >= 95:
        return 3
    elif row["points"] >= 85:
        return 2
    else:
        return 1

# Aplica a função linha por linha (axis=1)
df["star_ratings"] = df.apply(definir_estrelas, axis=1)

# Exibe o DataFrame com a nova coluna de classificações por estrelas
print(df)
