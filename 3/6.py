# EXERCÍCIO: Contar descritores em análises de vinhos
# Objetivo: Contar quantas vezes as palavras "tropical" e "fruity" aparecem nas descrições de vinhos.

import pandas as pd  # Importa a biblioteca pandas

# Cria um DataFrame com uma coluna de descrições de vinhos
df = pd.DataFrame({
    "description": [
        "This wine has a tropical aroma with hints of pineapple.",
        "Fruity and sweet, perfect for summer days.",
        "Notes of tropical fruit and citrus.",
        "A dry red with fruity undertones.",
        "Complex and earthy, no fruity or tropical hints."
    ]
})

# Junta todas as descrições em uma única string e converte para minúsculas
all_descriptions = " ".join(df["description"].dropna()).lower()

# Conta quantas vezes a palavra "tropical" aparece na string
tropical_count = all_descriptions.count("tropical")

# Conta quantas vezes a palavra "fruity" aparece na string
fruity_count = all_descriptions.count("fruity")

# Cria uma Series com os contadores das palavras
descriptor_counts = pd.Series({
    "tropical": tropical_count,
    "fruity": fruity_count
})

# Exibe os resultados finais
print(descriptor_counts)
