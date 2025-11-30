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

np.save("X_train.npy", X_train)
np.save("X_test.npy", X_test)
np.save("y_train.npy", y_train)
np.save("y_test.npy", y_test)

n_genres = len(genre_encoder.classes_)

kmeans_clusters = np.arange(20, 101, 10)
hdbscan_min_cluster_size = np.arange(50, 301, 25)
num_folds = 3

#f1_scores_kmeans = np.zeros((num_folds, len(kmeans_clusters)))
accuracy_kmeans  = np.zeros((num_folds, len(kmeans_clusters)))

#Hf1_scores_hdbscan = np.zeros((num_folds, len(hdbscan_min_cluster_size)))
accuracy_hdbscan  = np.zeros((num_folds, len(hdbscan_min_cluster_size)))


outer_kf = KFold(n_splits=num_folds, shuffle=True, random_state=42)

for fold_idx, (inner_train_idx, validation_idx) in enumerate(outer_kf.split(X)):
    X_inner_train, X_validation = X[inner_train_idx], X[validation_idx]
    y_inner_train, y_validation = y[inner_train_idx], y[validation_idx]

    majority_class = np.bincount(np.argmax(y_inner_train, axis=1)).argmax()


    for k_idx, kmeans_k in enumerate(kmeans_clusters):

        kmeans_model = KMeans(n_clusters=kmeans_k, random_state=42)
        topic_model_kmeans = BERTopic(hdbscan_model=kmeans_model)
        X_inner_train_topics_kmeans, X_inner_train_scores_kmeans = topic_model_kmeans.fit_transform(X_inner_train)
        X_inner_train_topics_kmeans, X_inner_train_scores_kmeans = np.array(X_inner_train_topics_kmeans), np.array(X_inner_train_scores_kmeans)

        topic_genre_matrix = np.zeros((kmeans_k, n_genres), dtype=int)
        for i,j in zip(X_inner_train_topics_kmeans, y_inner_train): #
            topic_genre_matrix[X_inner_train_topics_kmeans[i] , :] += j

        max_cols = np.argmax(topic_genre_matrix, axis=1)
        max_dict = {i: col.item() for i, col in enumerate(max_cols)}

        y_pred_topics = [get_topics(text, topic_model_kmeans, max_topics=1)[0] for text in X_validation]
        y_pred_topics_flat = list(map(lambda x: x[0] if isinstance(x, list) else x, y_pred_topics))


        y_pred_genres = list(map(lambda t: max_dict.get(t, majority_class), y_pred_topics_flat))


        ### Evaluation
        correct = [y_validation[i, pred] == 1 for i, pred in enumerate(y_pred_genres)]
        accuracy_kmeans[fold_idx,k_idx] = np.mean(correct).item()
        print(accuracy_kmeans[fold_idx,k_idx])

    for h_idx, hdbscan_size in enumerate(hdbscan_min_cluster_size):

        hdbscan_model = HDBSCAN(
            min_cluster_size=hdbscan_size,
            metric='euclidean',
            cluster_selection_method='eom'
        )
        topic_model_hdbscan = BERTopic(hdbscan_model=hdbscan_model) #BERTopic(hdbscan_model=hdbscan_model)
        X_inner_train_topics_dbscan, X_inner_train_scores_dbscan = topic_model_hdbscan.fit_transform(X_inner_train)
        X_inner_train_topics_dbscan, X_inner_train_scores_dbscan = np.array(X_inner_train_topics_dbscan), np.array(X_inner_train_scores_dbscan)

        n_topics = len(np.unique(X_inner_train_topics_dbscan)) # number of unique topics

        topic_genre_matrix = np.zeros((n_topics, n_genres), dtype=int)
        for i,j in zip(X_inner_train_topics_dbscan, y_inner_train): # the topic corresponds to -1 (trash)
            topic_genre_matrix[X_inner_train_topics_dbscan[i] , :] += j # can  be down more efficiently


        max_cols = np.argmax(topic_genre_matrix, axis=1)
        max_dict = {i: col.item() for i, col in enumerate(max_cols)}

        y_pred_topics = [get_topics(text, topic_model_hdbscan, max_topics=1)[0] for text in X_validation]
        y_pred_topics_flat = list(
            map(lambda x: x[0] if isinstance(x, list) and x[0] is not None else (-1 if x is None else x), y_pred_topics)
        )


        y_pred_genres = list(
            map(lambda t: max_dict[t] if t != -1 else max_dict[n_topics - 1], y_pred_topics_flat)
        )

        correct = [y_validation[i, pred] == 1 for i, pred in enumerate(y_pred_genres)]
        accuracy_hdbscan[fold_idx,h_idx] = np.mean(correct).item()
        print(accuracy_hdbscan[fold_idx, h_idx])



# -------- KMeans --------
mean_accuracy_kmeans = accuracy_kmeans.mean(axis=0)
best_k_idx = np.argmax(mean_accuracy_kmeans)
best_k = kmeans_clusters[best_k_idx]
best_acc = mean_accuracy_kmeans[best_k_idx]

print("Mean accuracy of K-means per number of clusters:")
for k, acc in zip(kmeans_clusters, mean_accuracy_kmeans):
    print(f"{k:>3}  →  {acc:.4f}")
print(f"Best K-means: k={best_k} with mean accuracy {best_acc:.4f}\n")

# -------- HDBSCAN --------
mean_accuracy_hdbscan = accuracy_hdbscan.mean(axis=0)
best_h_idx = np.argmax(mean_accuracy_hdbscan)
best_h_size = hdbscan_min_cluster_size[best_h_idx]
best_h_acc = mean_accuracy_hdbscan[best_h_idx]

print("Mean accuracy of HDBscan per min cluster size:")
for h, acc in zip(hdbscan_min_cluster_size, mean_accuracy_hdbscan):
    print(f"{h:>3}  →  {acc:.4f}")
print(f"Best HDBSCAN: min_cluster_size={best_h_size} with mean accuracy {best_h_acc:.4f}")

# Save KMeans accuracy table
np.savetxt("accuracy_kmeans.csv", accuracy_kmeans, delimiter=",",
           header=",".join(map(str, kmeans_clusters)), comments='')

# Save HDBSCAN accuracy table
np.savetxt("accuracy_hdbscan.csv", accuracy_hdbscan, delimiter=",",
           header=",".join(map(str, hdbscan_min_cluster_size)), comments='')

