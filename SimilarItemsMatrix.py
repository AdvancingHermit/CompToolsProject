import pandas as pd
import numpy as np
from collections import defaultdict

import groupedGenres

df = pd.read_csv("wiki_movie_plots_deduped.csv")
df = df[df['Genre'] != 'unknown'].reset_index(drop=True)
#df = df.sample(n = 500, random_state=1).reset_index(drop=True)
#print(df['Plot'][136])
#print(" NEXT ")
#print(df['Plot'][453])

simMat = np.load("array.npy")
simMat[simMat == 1] = -1
print(np.unravel_index(np.argmax(simMat), simMat.shape), np.max(simMat))

threshold = np.quantile(simMat[simMat != -1], 0.95)
print(threshold)
trueOverAverage = 0
falseOverAverage = 0
trueUnderAverage = 0
falseUnderAverage = 0




# Get all variables from the imported module
all_vars = vars(groupedGenres)

genre_map = defaultdict(set)

for genre_name, values in all_vars.items():
    # We only care about variables that are *lists*
    if isinstance(values, list):
        for value in values:
            genre_map[value].add(genre_name)

# Convert defaultdict to a regular dict if needed
genre_map = dict(genre_map)

# Example print
for k, v in list(genre_map.items())[:20]:
    print(f"{k} → {v}")

print("\nTotal unique genre strings:", len(genre_map))




k = simMat.shape[0]
print(k)
for i in range(k):
    for j in range(k):
        if j+i >= k:
            break
        val = simMat[i][i+j]
        if val >= threshold:
            genre1 = genre_map[df['Genre'][i]]
            genre2 = genre_map[df['Genre'][i+j]]
            if len(genre1.intersection(genre2)) != 0:
                trueOverAverage += 1
            else:
                falseOverAverage += 1


print("True over and under average: ", trueOverAverage, trueUnderAverage)
print("False over and under average: ", falseOverAverage, falseUnderAverage)
print()
print((trueOverAverage + trueUnderAverage)/(falseOverAverage + falseUnderAverage +trueOverAverage + trueUnderAverage ))

print(1/33)
#print(df['Genre'].unique())



