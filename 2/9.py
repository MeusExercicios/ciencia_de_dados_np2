# QUESTÃO 9
# Enunciado:
# Crie um DataFrame e filtre apenas os carros que custam mais de 100000 e que sejam do tipo "Ferrari" ou "Lamborghini".

import pandas as pd

valor = {
    "Carros": [
        'Mustang', 'Ferrari', 'Lamborghini', 'Porsche', 'Camaro',
        'BMW M3', 'Audi R8', 'Mercedes AMG', 'Dodge Charger', 'Nissan GT-R',
        'Toyota Supra', 'Chevrolet Corvette', 'Jaguar F-Type', 'Aston Martin DB11',
        'McLaren 720S', 'Rolls-Royce Ghost', 'Bentley Continental', 'Tesla Model S',
        'Bugatti Chiron', 'Koenigsegg Agera'
    ],
    "Preco": [
        25000, 100000, 555555, 120000, 35000,
        67000, 140000, 130000, 40000, 150000,
        45000, 60000, 80000, 200000, 300000,
        400000, 250000, 90000, 3000000, 2800000
    ]
}  

# mesmo conteúdo anterior

# Criando o DataFrame
carros_df = pd.DataFrame(valor)

# Aplicando dois filtros ao mesmo tempo
top_carros = carros_df[(carros_df['Preco'] > 100000) & (carros_df['Carros'].isin(['Ferrari', 'Lamborghini']))]

print(top_carros)