import json
import numpy as np
import faiss
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer

with open("data/assessments.json", "r", encoding="utf-8") as f:
    assessments = json.load(f)

texts = [
    item["name"] + " " + item["description"]
    for item in assessments
]

vectorizer = TfidfVectorizer(stop_words="english")
tfidf_matrix = vectorizer.fit_transform(texts)

embeddings = tfidf_matrix.toarray().astype("float32")

dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

faiss.write_index(index, "data/faiss_index.index")

with open("data/vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

print("Index built:", index.ntotal)