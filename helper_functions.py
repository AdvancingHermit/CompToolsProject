from nltk.corpus import stopwords
import re
import pandas as pd
import numpy as np

def preprocess_dataset(file_name):
    df = pd.read_csv(file_name, on_bad_lines='skip')
    df = df.drop(columns=['Director', 'Cast', 'Wiki Page'])
    df = df.drop_duplicates(subset=['Plot']).reset_index(drop=True)

    genre_map = {
        # action / adventure
        "action": "action",
        "adventure": "adventure",
        "martial arts": "action",
        "kung fu": "action",
        "superhero": "action",
        "spy": "action",
        "thriller": "thriller",
        "suspense": "thriller",
        "crime": "crime",
        "detective": "crime",
        "heist": "crime",
        "mystery": "mystery",
        # comedy
        "comedy": "comedy",
        "dark comedy": "comedy",
        "parody": "comedy",
        "romantic comedy": "comedy",
        "slapstick": "comedy",
        # drama
        "drama": "drama",
        "biographical": "drama",
        "historical": "drama",
        "war": "drama",
        "family": "drama",
        "youth": "drama",
        "social": "drama",
        "political": "drama",
        # romance
        "romance": "romance",
        "romantic": "romance",
        "love": "romance",
        # musical / dance
        "musical": "musical",
        "dance": "musical",
        "idol": "musical",
        # sci-fi / fantasy
        "sci-fi": "sci-fi",
        "science fiction": "sci-fi",
        "fantasy": "fantasy",
        "magic": "fantasy",
        "magical girl": "fantasy",
        "supernatural": "fantasy",
        "kaiju": "fantasy",
        # horror / thriller
        "horror": "horror",
        "slasher": "horror",
        "found footage": "horror",
        "erotic horror": "horror",
        "zombie": "horror",
        "apocalyptic": "horror",
        # animation
        "animated": "animation",
        "animation": "animation",
        "cartoon": "animation",
        "anime": "animation",
        "tokusatsu": "animation",
        # documentary / biography
        "documentary": "documentary",
        "biopic": "documentary",
        "true crime": "documentary",
        # sports
        "sport": "sports",
        "sports": "sports",
        # unknown / fallback
        "-": "unknown",
    }

    def generalize_genre_multi(genre_string):
        if pd.isna(genre_string):
            return np.nan
        out = set()
        for part in genre_string.lower().replace("/", ",").split(","):
            part = part.strip()
            if not part:
                continue
            if part in genre_map:
                if genre_map[part] == "unknown":
                    continue
                out.add(genre_map[part])
        if not out:
            return np.nan
        return list(out)   # list of generalized genres

    # list of genres per movie
    df["Genre"] = df["Genre"].apply(generalize_genre_multi)

    def preprocess_text(text, return_list=True):
        stop_words = set(stopwords.words('english'))
        text = re.sub(r"[.,?!()\/#*&$^\-_:;'<>\[\]\"\\]", "", text)
        text = re.sub(r"(?<!\d)\d(?!\d)", "", text)
        text = text.lower()
        tokens = text.split()
        filtered_tokens_list = [word for word in tokens if word not in stop_words]
        if return_list:
            filtered_tokens = " ".join(filtered_tokens_list)
        else:
            filtered_tokens = filtered_tokens_list
        return filtered_tokens

    df["Processed_Plot"] = df["Plot"].apply(preprocess_text)

    df_unknown_genre = df[df['Genre'].isna()]
    df = df.dropna(subset=['Genre'])

    class_counts = df["Genre"].value_counts()
    valid_classes = class_counts[class_counts >= 2].index
    df_filtered = df[df["Genre"].isin(valid_classes)].copy()

    return df_filtered, df_unknown_genre




def subset_sampler(df, n=1000):
    len_dataset = df.shape[0]
    n = min(n, len_dataset)
    idxs = np.random.choice(len_dataset, size=n, replace=False)
    return df.iloc[idxs].reset_index(drop=True)


def get_best_topic(model, text):
    topics, _ = model.find_topics(text)
    return topics[0]


def get_topics(text, topic_model, min_score=0.5, max_topics=3):
    topic_ids, scores = topic_model.find_topics(text)

    # Filter topics by threshold
    filtered = [(tid, score) for tid, score in zip(topic_ids, scores) if score >= min_score]

    if not filtered:  # no topic passes threshold
        return [-1], [1]

    # Return at most max_topics
    filtered = filtered[:max_topics]

    # Separate IDs and scores
    filtered_ids, filtered_scores = zip(*filtered)
    return list(filtered_ids), list(filtered_scores)



