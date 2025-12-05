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

from collections import Counter

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

print(X_train, y_train)

n_genres = len(genre_encoder.classes_)

kmeans_clusters = np.arange(20, 101, 10)
hdbscan_min_cluster_size = np.arange(50, 301, 25)
num_folds = 2

ConfusionMatrixes = []
ConfusionMatrixesGenres = []

#f1_scores_kmeans = np.zeros((num_folds, len(kmeans_clusters)))
accuracy_kmeans  = np.zeros((num_folds, len(kmeans_clusters)))

outer_kf = KFold(n_splits=num_folds, shuffle=True, random_state=42)

print("Started")

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

        for i,j in zip(X_inner_train_topics_kmeans, y_inner_train):
            topic_genre_matrix[i, :] += j

        max_cols = np.argmax(topic_genre_matrix, axis=1)
        max_dict = {i: col.item() for i, col in enumerate(max_cols)}

        y_pred_topics = [get_topics(text, topic_model_kmeans, max_topics=10)[0] for text in X_validation]

        #print("topics", y_pred_topics)

        y_pred_genres = []
        #print(genre_probabilities)

        for t_arr in y_pred_topics:
            #print(t_arr)
            pred_arr = []
            for t in t_arr:
                if t in max_dict and t != -1:
                    pred_arr.append(max_dict[t])
                else:
                    pred_arr.append(majority_class)

            pred_arr = list(set(pred_arr))
            y_pred_genres.append(pred_arr)

        print("pred", y_pred_genres)

        print(y_validation)
        TP = 0
        FP = 0
        FN = 0
        TN = 0

        conf_matrix_genre = []

        for i in range(15):
            matrix = [0]*4
            conf_matrix_genre.append(matrix)

        for i in range(len(y_validation)):

            for j in range(len(y_validation[i])):

                if y_validation[i][j] == 1 and j in y_pred_genres[i]:
                    TP += 1
                    conf_matrix_genre[j][0] += 1
                if y_validation[i][j] == 1 and j not in y_pred_genres[i]:
                    FN += 1
                    conf_matrix_genre[j][2] += 1
                if y_validation[i][j] == 0 and j in y_pred_genres[i]:
                    FP += 1
                    conf_matrix_genre[j][1] += 1
                if y_validation[i][j] == 0 and j not in y_pred_genres[i]:
                    TN += 1
                    conf_matrix_genre[j][3] += 1

        ConfusionMatrixesGenres.append(conf_matrix_genre)
        #print(ConfusionMatrixesGenres)
        print(conf_matrix_genre)


        print("FN", FN)
        print("TN", TN)
        print("FP", FP)
        print("TP", TP)

        #correct = [y_validation[i, pred] == 1 for i, pred_arr in enumerate(y_pred_genres) for pred in pred_arr]

        Accuracy = (TP + TN) / (TP + FP + FN + TN)
        Precision = (TP) / (TP + FP)
        Recall = (TP) / (TP + FN)

        ConfusionMatrixes.append([TP, FP, FN, TN])

        f1_score = (2*Precision*Recall)/(Precision + Recall)

        accuracy_kmeans[fold_idx,k_idx] = f1_score
        print(Accuracy)
        print(f1_score)


print("Ended")

# -------- KMeans --------
mean_accuracy_kmeans = accuracy_kmeans.mean(axis=0)
best_k_idx = np.argmax(mean_accuracy_kmeans)
best_k = kmeans_clusters[best_k_idx]
best_acc = mean_accuracy_kmeans[best_k_idx]

print("Mean accuracy of K-means per number of clusters:")
for k, acc in zip(kmeans_clusters, mean_accuracy_kmeans):
    print(f"{k:>3}  →  {acc:.4f}")
print(f"Best K-means: k={best_k} with mean accuracy {best_acc:.4f}\n")

print("Confusion matrix:")
print(ConfusionMatrixes[best_k_idx])
print("Confusion Matrix Genres")
print(ConfusionMatrixesGenres[best_k_idx])

# Save KMeans accuracy table
np.savetxt("accuracy_kmeans.csv", accuracy_kmeans, delimiter=",",
           header=",".join(map(str, kmeans_clusters)), comments='')

with open("best_conf_matrix.txt", "w") as f:
    for item in ConfusionMatrixes[best_k_idx]:
        f.write(f"{item}\n")

with open("best_conf_genre_matrix.txt", "w") as f:
    for item in ConfusionMatrixesGenres[best_k_idx]:
        f.write(f"{item}\n")