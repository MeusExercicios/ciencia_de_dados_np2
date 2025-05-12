import pandas as pd 

data = {
    "taster_name": ["Alice", "Bob", "Alice", "Bob", "Carol", "Alice", "Carol"],
    "points": [90, 88, 95, 85, 92, 87, 94]
}


df = pd.DataFrame(data)

agrupamento = df.groupby("taster_name")["points"].mean()

print(agrupamento)