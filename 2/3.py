# QUESTÃO 3
# Enunciado:
# Crie um DataFrame com os dados fornecidos e exiba apenas a primeira linha completa (carro + preço).

import pandas as pd

valor = {"Carros":['mustang', 'ferrari', 'Lamborguini'], 'Preco':[25000,100000,555555]}

# Criando o DataFrame e já aplicando o .head(1) para obter a primeira linha
primeiro = pd.DataFrame(valor).head(1)

# Exibindo o resultado
print(primeiro)