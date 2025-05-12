import pandas as pd 

# DataFrame de eventos (meets)
meets = pd.DataFrame({
    'meet_id': [1, 2, 3],
    'meet_name': ['Nationals', 'State Cup', 'World Championship'],
    'country': ['USA', 'Brazil', 'USA']
})

# DataFrame de atletas (lifters)
lifters = pd.DataFrame({
    'lifter_id': [11, 12, 13, 14],
    'name': ['Alice', 'Bob', 'Carlos', 'Diana'],
    'meet_id': [1, 2, 3, 1]
})

# Juntando os atletas com os eventos
joined = pd.merge(lifters, meets, on='meet_id')

# Agrupando por país e contando quantos atletas competiram
grouped = joined.groupby('country')['lifter_id'].count().sort_values(ascending=False)

print(grouped)
