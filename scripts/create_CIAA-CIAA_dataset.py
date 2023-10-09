# The CIAA-CIAA dataset is extracted out of DATASET.csv
# Nils Dyck, 04.05.2023

import pandas as pd

df = pd.read_csv('data/cleaned/DATASET2.csv', sep=';')

ciaa = df.loc[df['Venue'].isin(['CIAA','WIA','Workshop on Implementing Automata'])]
ciaa.to_csv('data/cleaned/CIAA-CIAA.csv', index=False, sep=';')