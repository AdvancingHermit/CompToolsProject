import pandas as pd
import numpy as np

df = pd.read_csv("wiki_movie_plots_deduped.csv")
df = df[df['Genre'] != 'unknown'].reset_index(drop=True)
df = df.sample(n = 500, random_state=1).reset_index(drop=True)
print(df['Plot'][136])
print(" NEXT ")
print(df['Plot'][453])

q = 5
plots = {}


#print(testText)
for index,row in df.iterrows():
    words = set()
    p = row['Plot']
    for x in range(len(p) - (q-1)):
        words.add(p[x:x+q])

    plots[index] = words

#print(plots)
'''
#testing
set1 = plots[7]
set2 = plots[7]

print(set1,set2)
t = len(set1.intersection(set2))
b = len(set1.union(set2))
print(t/b)
#end testing
'''

#needs optimization
simMat = np.zeros((len(df['Plot']), len(df['Plot'])), dtype = float)
for idx, x in enumerate(plots.values()):
    for idy, y in enumerate(plots.values()):
        if idx+idy >= simMat.shape[0]:
            break
        y = plots[idy + idx]
        t = len(x.intersection(y))
        b = len(x.union(y))
        r = t/b
        simMat[idx][idy+ idx] = r
#np.save("array.npy", simMat)
print(simMat)













