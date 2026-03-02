from retrieval.recommender import recommend

query = "Need Java developer who collaborates with stakeholders"

results = recommend(query, top_k=5)

for r in results:
    print(r["name"])
    print(r["url"])
    print("----")