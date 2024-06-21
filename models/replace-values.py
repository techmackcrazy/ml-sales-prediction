import pandas as pd

df = pd.read_csv('./obt_vendas.csv')
df_values = pd.read_csv('./replaces.csv')

df_values = df_values['valor_venda']


df['valor_venda'] = df_values
print(df)

df.to_csv('./replaced_obt_vendas.csv')