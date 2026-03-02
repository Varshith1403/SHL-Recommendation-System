import json
import faiss
import pickle
import re

index = faiss.read_index("data/faiss_index.index")

with open("data/vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

with open("data/assessments.json", "r", encoding="utf-8") as f:
    assessments = json.load(f)


def clean_query(query):
    query = query.lower()

    stop_words = [
        "experience", "required", "responsibilities",
        "looking", "hiring", "candidate", "role",
        "company", "job", "years", "year",
        "good", "strong", "ability", "skills"
    ]

    words = re.findall(r"\b[a-zA-Z0-9\+\#]+\b", query)

    filtered = [w for w in words if w not in stop_words and len(w) > 2]

    return " ".join(filtered)


def recommend(query, top_k=10):

    cleaned = clean_query(query)

    query_vector = vectorizer.transform([cleaned]).toarray().astype("float32")

    distances, indices = index.search(query_vector, top_k)

    results = []
    for idx in indices[0]:
        results.append(assessments[idx])

    return results