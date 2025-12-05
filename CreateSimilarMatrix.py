import pandas as pd
import numpy as np
import hashlib

# Load data
df = pd.read_csv("wiki_movie_plots_deduped.csv")
df = df[df['Genre'] != 'unknown'].reset_index(drop=True)
#df = df.sample(n = 500, random_state=1).reset_index(drop=True)

#np.int64(14367), np.int64(20340)
print(df['Title'][14367], df['Plot'].get(14367),"\nText 2:\n", df['Title'][20340], df['Plot'].get(20340) )

#Get and compress shingles from all movie plots
q = 5 # Shingle size
shingles_of_plots = {}
for index,row in df.iterrows():
    shingles = set()
    p = row['Plot']
    for x in range(len(p) - (q-1)):
        compressed_hashed_shingle = int.from_bytes(hashlib.blake2b(p[x:x+q].encode('utf-8'), digest_size=6).digest())
        shingles.add(compressed_hashed_shingle)
    shingles_of_plots[index] = shingles



np.random.seed(11)
max_rand_val = len(shingles_of_plots) -1
num_hashes = 100
coeff_a = np.random.randint(1, max_rand_val, size=(num_hashes,1))
coeff_b = np.random.randint(0, max_rand_val, size=(num_hashes,1))
fun_prime = 88888888888889 # One of the most prime numbers
# Get hashed shingles
signatures = {}
for i, shingles_set in shingles_of_plots.items():
    shingles = np.array(list(shingles_set), dtype=np.int64).reshape(1, -1)
    hash_values = (coeff_a @ shingles + coeff_b) % fun_prime
    min_values = np.min(hash_values, axis=1)
    signatures[i] = min_values

def estimate_jaccard_sim(a, b):
    counter = 0
    for x, y in zip(a, b):
        if x == y:
            counter += 1
    return counter / num_hashes

l = len(df['Plot'])
simMat = np.zeros((len(df['Plot']), len(df['Plot'])), dtype = float)
for idx, x in enumerate(signatures.values()):
    print(idx, "/", l)
    for idy, y in enumerate(signatures.values()):
        if idx+idy >= simMat.shape[0]:
            break
        y = signatures[idy + idx]
        simMat[idx][idy+ idx] = estimate_jaccard_sim(x, y)
print(simMat)
np.save("simmat_hashed.npy", simMat)



'''
# Exact Jaccard

l = len(df['Plot'])
#needs optimization
simMat = np.zeros((len(df['Plot']), len(df['Plot'])), dtype = float)
for idx, x in enumerate(plots.values()):
    print(idx, "/", l)
    for idy, y in enumerate(plots.values()):
        if idx+idy >= simMat.shape[0]:
            break
        y = plots[idy + idx]
        t = len(x.intersection(y))
        b = len(x.union(y))
        r = t/b
        simMat[idx][idy+ idx] = r
print(simMat)
'''












