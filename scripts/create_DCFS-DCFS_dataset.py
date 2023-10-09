# The DCFS-DCFS dataset is extracted out of DCFS-ALL.csv
# Nils Dyck, 31.05.2023

import pandas as pd

df = pd.read_csv('data/cleaned/DCFS-ALL.csv', sep=';')

ciaa = df.loc[df['Venue'].isin(['DCFS'])]
ciaa.to_csv('data/cleaned/DCFS-DCFS.csv', index=False, sep=';')