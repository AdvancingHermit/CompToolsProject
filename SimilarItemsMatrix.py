import pandas as pd
import numpy as np
from collections import defaultdict
import itertools
import groupedGenres

df = pd.read_csv("wiki_movie_plots_deduped.csv")
df = df[df['Genre'] != 'unknown'].reset_index(drop=True)
# Uncomment next line to run a quicker example using only 500 random entries
#df = df.sample(n = 500, random_state=1).reset_index(drop=True)

# Load matrix from the file generated from CreateSimilarMatrix.py
simMat = np.load("simmat_hashed.npy")
# Make sure the diagonal is not counted since this is the similarity between themselves
simMat[simMat == 1] = -1
#print(np.unravel_index(np.argmax(simMat), simMat.shape), np.max(simMat))

# Computing top 10% threshold of similarities
threshold = np.quantile(simMat[simMat != -1], 0.90)
#print(threshold)
trueOverThreshold = 0
falseOverThreshold = 0




# Get all variables from groupedGenres
all_vars = vars(groupedGenres)

genre_map = defaultdict(set)
all_genres = df['Genre'].unique().tolist()


#Create a map mapping all genres to a list of the primary genres they fit in
all_vars = vars(groupedGenres)
genre_map = defaultdict(set)
known_keys = [k for k, v in all_vars.items() if isinstance(v, list) and not k.startswith('_')]

for genre, values in all_vars.items():
    if genre in known_keys:
        for value in values:
            genre_map[value].add(genre)
#print(known_keys)
for value in all_genres:
    if value in genre_map.keys():
        continue
    matches = [g for g in known_keys if g.lower().strip() in value.lower().strip()] 
    if matches:
        genre_map[value].update(matches)
    else:
        #print(value)
        genre_map[value].add('other')

genre_map = dict(genre_map)


print("\nTotal unique genre strings:", len(genre_map))

k = simMat.shape[0]
#print(k)
for i in range(k):
    #print(i)
    for j in range(k):
        if j+i >= k:
            break
        val = simMat[i][i+j]
        if val >= threshold:
            genre1 = genre_map[df['Genre'][i]]
            genre2 = genre_map[df['Genre'][i+j]]
            # counting one occurrence of same genre, if they share at least 1 primary genre
            if len(genre1.intersection(genre2)) != 0:
                trueOverThreshold += 1
            else:
                falseOverThreshold += 1


print("True over threshold: ", trueOverThreshold)
print("False over threshold: ", falseOverThreshold)
print("Same genre probability = ", trueOverThreshold / (trueOverThreshold + falseOverThreshold))



