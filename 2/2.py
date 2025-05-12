# QUESTÃO 2
# Enunciado:
# Crie um DataFrame com os nomes dos carros e selecione apenas o primeiro carro da coluna "Carros".

import pandas as pd

valor = {"Carros":['mustang', 'ferrari', 'Lamborguini'], 'Preco':[25000,100000,555555]}

# Criando o DataFrame
primeiro = pd.DataFrame(valor)

# Exibindo apenas o primeiro elemento da coluna "Carros"
print(primeiro['Carros'].head(1))