import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pandas as pd
from collections import defaultdict
from retrieval.recommender import recommend


def normalize(url):
    return url.replace("/solutions", "").rstrip("/")


def recall_at_k(predicted, actual, k=10):
    predicted = predicted[:k]
    return len(set(predicted) & set(actual)) / len(actual)


file_path = "data/Gen_AI Dataset.xlsx"
df = pd.read_excel(file_path, sheet_name="Train-Set")

ground_truth = defaultdict(list)

for _, row in df.iterrows():
    query = row["Query"]
    url = normalize(row["Assessment_url"])
    ground_truth[query].append(url)

recalls = []

for query, actual in ground_truth.items():
    results = recommend(query, top_k=10)
    predicted = [normalize(r["url"]) for r in results]

    recall = recall_at_k(predicted, actual, 10)
    recalls.append(recall)

mean_recall = sum(recalls) / len(recalls)

print("FINAL Mean Recall@10:", mean_recall)