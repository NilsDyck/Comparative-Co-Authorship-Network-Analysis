# As the authors who published first to CIAA in 2022 are also downloaded, they need to be removed.
# Nils Dyck, 30.05.2023

import pandas as pd

df = pd.read_csv('data/cleaned/DATASET2.csv',sep=';') 
df = df.loc[df['Year']<2022]

authors = df['Author-URL'].drop_duplicates().to_list()

ciaa = pd.read_csv('data/cleaned/CIAA-CIAA_m2.csv', sep=';')
ciaa = ciaa.loc[ciaa['Year']<2022]
ciaa_authors = ciaa['Author'].drop_duplicates().to_list()

missing_in_ciaa = [author for author in authors if author not in ciaa_authors]
df = df.loc[~(df['Author-URL'].isin(missing_in_ciaa))]

df.to_csv('data/cleaned/DATASET3.csv', sep=';')