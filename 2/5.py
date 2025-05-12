# QUESTÃO 5
# Enunciado:
# Crie um DataFrame com 20 carros e seus preços e selecione apenas os carros nas posições 1, 2 e 3 usando .loc.

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

# Criando o DataFrame e selecionando as linhas de índice 1, 2 e 3
primeiro = pd.DataFrame(valor).loc[[1,2,3]]

print(primeiro)