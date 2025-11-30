import pandas as pd
import numpy as np
import nltk
from bertopic import BERTopic
from sklearn.model_selection import KFold

from helper_functions import *
from sklearn.model_selection import train_test_split
from hdbscan import HDBSCAN
from sklearn.cluster import KMeans
from sklearn.preprocessing import MultiLabelBinarizer

nltk.download('stopwords')
nltk.download('punkt')

np.random.seed(1234)

genre_encoder = MultiLabelBinarizer()

df, df_unknown_genre = preprocess_dataset('data/wiki_movie_plots_deduped.csv')

X = df['Processed_Plot'].values
y = genre_encoder.fit_transform(df['Genre'].values)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

n_genres = len(genre_encoder.classes_)
with open('genre_classes.txt', 'w') as f:
    for cls in genre_encoder.classes_:
        f.write(f"{cls}\n")

kmeans_clusters = 3 * 80
hdbscan_min_cluster_size = 200 * 3


kmeans_model = KMeans(n_clusters=kmeans_clusters, random_state=42)
topic_model_kmeans = BERTopic(hdbscan_model=kmeans_model)
X_train_topics_kmeans, X_train_scores_kmeans = topic_model_kmeans.fit_transform(X_train)
X_train_topics_kmeans, X__train_scores_kmeans = np.array(X_train_topics_kmeans), np.array(X_train_scores_kmeans)

majority_class = np.bincount(np.argmax(y_train, axis=1)).argmax()


y_pred_genres = [majority_class] * len(y_test)
correct = [y_test[i, pred] == 1 for i, pred in enumerate(majority_class)]
accuracy_naive = np.mean(correct).item()
print("Accuracy Naive Method")
print(accuracy_naive)

with open('y_pred_genres_naive.txt', 'w') as f:
    for genre in y_pred_genres:
        f.write(f"{genre}\n")


topic_genre_matrix = np.zeros((kmeans_clusters, n_genres), dtype=int)
for i,j in zip(X_train_topics_kmeans, y_train): #
    topic_genre_matrix[X_train_topics_kmeans[i] , :] += j

max_cols = np.argmax(topic_genre_matrix, axis=1)
max_dict = {i: col.item() for i, col in enumerate(max_cols)}

y_pred_topics = [get_topics(text, topic_model_kmeans, max_topics=1)[0] for text in X_test]
y_pred_topics_flat = list(map(lambda x: x[0] if isinstance(x, list) else x, y_pred_topics))
y_pred_genres = list(map(lambda t: max_dict.get(t, majority_class), y_pred_topics_flat))

with open('y_pred_genres_kmeans.txt', 'w') as f:
    for genre in y_pred_genres:
        f.write(f"{genre}\n")


### Evaluation
correct = [y_test[i, pred] == 1 for i, pred in enumerate(y_pred_genres)]
accuracy_kmeans = np.mean(correct).item()
print("Accuracy K-Means")
print(accuracy_kmeans)


hdbscan_model = HDBSCAN(
            min_cluster_size=hdbscan_min_cluster_size,
            metric='euclidean',
            cluster_selection_method='eom'
        )
topic_model_hdbscan = BERTopic(hdbscan_model=hdbscan_model)
X_train_topics_dbscan, X_train_scores_dbscan = topic_model_hdbscan.fit_transform(X_train)
X_train_topics_dbscan, X_train_scores_dbscan = np.array(X_train_topics_dbscan), np.array(X_train_scores_dbscan)

n_topics = len(np.unique(X_train_topics_dbscan)) # number of unique topics

topic_genre_matrix = np.zeros((n_topics, n_genres), dtype=int)
for i,j in zip(X_train_topics_dbscan, y_train): # the topic corresponds to -1 (trash)
    topic_genre_matrix[X_train_topics_dbscan[i] , :] += j # can  be down more efficiently


max_cols = np.argmax(topic_genre_matrix, axis=1)
max_dict = {i: col.item() for i, col in enumerate(max_cols)}

y_pred_topics = [get_topics(text, topic_model_hdbscan, max_topics=1)[0] for text in X_test]
y_pred_topics_flat = list(
    map(lambda x: x[0] if isinstance(x, list) and x[0] is not None else (-1 if x is None else x), y_pred_topics)
    )


y_pred_genres = list(
    map(lambda t: max_dict[t] if t != -1 else max_dict[n_topics - 1], y_pred_topics_flat)
        )

with open('y_pred_genres_hdbscan.txt', 'w') as f:
    for genre in y_pred_genres:
        f.write(f"{genre}\n")

correct = [y_test[i, pred] == 1 for i, pred in enumerate(y_pred_genres)]
accuracy_hdbscan = np.mean(correct).item()
print("Accuracy HDBscan: ")
print(accuracy_hdbscan)


