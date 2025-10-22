import pandas as pd
import numpy as np

df = pd.read_csv("wiki_movie_plots_deduped.csv")
df = df[df['Genre'] != 'unknown']
print(df['Plot'])

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
        t = len(x.intersection(y))
        b = len(x.union(y))
        r = t/b
        simMat[idx][idy] = r

print(simMat)










