import sys
import os
sys.path.append(os.path.abspath("."))

import pandas as pd
from retrieval.recommender import recommend


def normalize(url):
    return url.replace("/solutions", "").rstrip("/")


file_path = "data/Gen_AI Dataset.xlsx"

print("Reading Test-Set...")

test_df = pd.read_excel(file_path, sheet_name="Test-Set")

print("Total test queries:", len(test_df))

rows = []

for _, row in test_df.iterrows():
    query = row["Query"]
    print("Processing:", query[:40], "...")

    results = recommend(query, top_k=10)

    for r in results:
        rows.append({
            "Query": query,
            "Assessment_url": normalize(r["url"])
        })

if len(rows) == 0:
    print("No rows generated. Something is wrong.")
else:
    output_df = pd.DataFrame(rows)
    output_df.to_csv("test_predictions.csv", index=False)
    print("Test predictions saved.")
    print("Total rows written:", len(rows))