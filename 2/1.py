import pandas as pd 

valor = {"Carros":['mustang', 'ferrari', 'Lamborguini'],'Preco':[25000,100000,555555]}

df = pd.DataFrame(valor, index=['carro 1','carro2','carro 3'])

novaVariavel = df['Preco']

print(novaVariavel)

