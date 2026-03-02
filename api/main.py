from fastapi import FastAPI
from pydantic import BaseModel
import sys
import os

# Ensure project root is accessible
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from retrieval.recommender import recommend

app = FastAPI(title="SHL Assessment Recommendation API")


class QueryRequest(BaseModel):
    query: str


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.post("/recommend")
def recommend_assessments(request: QueryRequest):

    results = recommend(request.query, top_k=10)

    formatted = []

    for r in results:
        formatted.append({
            "assessment_name": r["name"],
            "url": r["url"],
            "test_type": r.get("test_type", ""),
            "description": r.get("description", ""),
            "duration": r.get("duration", ""),
            "remote_support": r.get("remote_support", ""),
            "adaptive_support": r.get("adaptive_support", "")
        })

    return {"recommended_assessments": formatted}