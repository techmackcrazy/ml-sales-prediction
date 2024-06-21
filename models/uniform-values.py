import numpy as np
import pandas as pd

# Definindo os limites inferior e superior do intervalo
limite_inferior = 237_500
limite_superior = 800_000

# Gerando 27000 preços fictícios entre 237.500 e 800.000
valores_simulados = np.random.uniform(limite_inferior, limite_superior, size=29512)

# Convertendo para um DataFrame do pandas para facilitar a manipulação
df_simulado = pd.DataFrame({'valor_venda': valores_simulados.round(2)})


df_simulado.to_csv('./replaces.csv')