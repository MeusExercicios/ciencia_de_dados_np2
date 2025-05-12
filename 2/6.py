# QUESTÃO 6
# Enunciado:
# Crie um DataFrame com índices personalizados ("carro 1" a "carro 20") e selecione os três primeiros carros usando .loc.

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

# Definindo o DataFrame com índices personalizados
primeiro = pd.DataFrame(valor, index=['carro 1', 'carro 2', 'carro 3', 'carro 4', 'carro 5', 'carro 6', 'carro 7', 'carro 8', 
                                      'carro 9', 'carro 10', 'carro 11', 'carro 12', 'carro 13', 'carro 14', 'carro 15', 
                                      'carro 16', 'carro 17', 'carro 18', 'carro 19', 'carro 20'])

# Selecionando linhas pelos rótulos
primeiro = primeiro.loc[['carro 1', 'carro 2', 'carro 3']]

print(primeiro)