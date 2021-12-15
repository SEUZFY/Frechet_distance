import pandas as pd
import seaborn
import csv
import matplotlib.pyplot as plt
import numpy as np

# read from csv and convert to dataframe
tmp_lst = []

with open(r"D:\AlbertQ2\GEO1003\assignment3\frechet.csv", 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        tmp_lst.append(row)

# convert str to float
for i in range(1,len(tmp_lst)): # column names, not converted to float
    for j in range(len(tmp_lst[i])):
        tmp_lst[i][j] = float(tmp_lst[i][j])

df = pd.DataFrame(tmp_lst[1:], columns=tmp_lst[0]) # convert to dataframe
print(df)
# print(df.corr()) # variance-covariance matrix

# draw
#f, (ax1,ax2) = plt.subplots(figsize = (8,8),nrows=2) # use figsize to control size

fig, ax = plt.subplots()
cmap = seaborn.cubehelix_palette(start = 1.5, rot = 3, gamma=0.8, as_cmap = True)
seaborn.heatmap(df, linewidths = 0.05, ax = ax, cmap='Blues',square = True, annot=True, annot_kws={'size':12, 'color':'black'})
ax.set_title('Fréchet Distance in RSS space')
ax.set_xlabel('Locations')
ax.set_ylabel('Locations')

plt.show()

#read big file
#reader = pd.read_csv(r"D:\AlbertQ2\GEO1003\assignment3\frechet.csv",iterator=True,sep=';')
#loop = True
#chunksize = 100000
#chunks = []
#while loop:
#    try:
#        chunk = reader.get_chunk(chunksize)
#        chunk = chunk.dropna(axis=1)
#        chunk = chunk.drop_duplicates()
#        chunks.append(chunk)
#    except StopIteration:
#        loop = False
#        #print("Iteration is stopped.")
#df = pd.concat(chunks,ignore_index=True)
#df = df.dropna(axis=1)
#df = df.drop_duplicates()
#print(df)