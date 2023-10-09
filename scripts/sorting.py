# sorting CIAA-authors by name for further use
# Nils Dyck, 08.05.2023

import pandas as pd

df = pd.read_csv('data/processed/CIAA-authors.csv', sep=';')

df = df.sort_values(by='Name')

print(df.head())

df.to_csv('data/processed/CIAA-authors_sorted.csv', sep=';')