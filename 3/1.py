# Media de valor dos preços
import pandas as pd

valores = {
    'carros': ['Ferrari','Uno','Jegue'],
    'preco': [1000000,15000,10]
}

df = pd.DataFrame(valores)

print(df['preco'].mean())


