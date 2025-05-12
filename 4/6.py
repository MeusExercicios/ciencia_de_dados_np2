import pandas as pd 

data = {
    "country": ["US", "France", "US", "Italy", "US", "France", "Italy", "Italy", "France", "US"],
    "variety": ["Pinot Noir", "Merlot", "Chardonnay", "Sangiovese", "Pinot Noir", "Merlot", "Sangiovese", "Sangiovese", "Merlot", "Chardonnay"]
}


df = pd.DataFrame(data)

agrupamento = df.groupby(["country","variety"]).size().sort_values(ascending=False)

print(agrupamento)