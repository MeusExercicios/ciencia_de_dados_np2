# QUESTÃO 1
# Enunciado:
# Crie um DataFrame com os nomes de carros e seus respectivos preços. 
# Em seguida, selecione apenas a coluna "Preco" e armazene em uma nova variável.

import pandas as pd

# Criando um dicionário com os dados dos carros e preços
valor = {"Carros":['mustang', 'ferrari', 'Lamborguini'], 'Preco':[25000, 100000, 555555]}

# Criando um DataFrame com índice personalizado
df = pd.DataFrame(valor, index=['carro 1','carro2','carro 3'])

# Selecionando a coluna "Preco" e armazenando em novaVariavel
novaVariavel = df['Preco']

# Exibindo os preços dos carros
print(novaVariavel)