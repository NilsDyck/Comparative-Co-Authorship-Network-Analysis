import pandas as pd

sep_parameter = ';'
default = pd.read_csv('data/cleaned/gruber-holzer-rauch_dataset.csv', sep=sep_parameter)
ciaa_ciaa = pd.read_csv('data/cleaned/CIAA-CIAA.csv', sep=sep_parameter)

misstakes = []
for year in range(1996, 2023):
    if year != 2021:
        if len(default[default.Year == year].index) != len(ciaa_ciaa[ciaa_ciaa.Published == year].index):
            misstakes.append(year)

for misstake in misstakes:
    print('Default: '+str(misstake)+': '+str(len(default[default.Year == misstake].index)))
    print('My very own: '+str(misstake)+': '+str(len(ciaa_ciaa[ciaa_ciaa.Published == misstake].index)))

#Now compare the titles of the dataset
ciaa_titles = ciaa_ciaa['Title'].to_list()
default_titles = default['Title'].to_list()

print('CIAA-CIAA: '+str(len(ciaa_titles)))
print('Default: '+str(len(default_titles)))

# print('Missing in Default: ')
# for entry in ciaa_titles:
#     if entry not in default_titles:
#         print(entry)
print('Missing in CIAA-CIAA: ')
missing = []
for entry in default_titles:
    if entry not in ciaa_titles:
        #print(entry)
        missing.append(entry)

print(str(len(missing)))
print(missing)