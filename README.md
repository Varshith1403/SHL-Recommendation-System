# SHL Assessment Recommendation Engine

## Overview

This project implements an intelligent Assessment Recommendation Engine using SHL's product catalog.

The system takes a job description or hiring query as input and recommends the most relevant SHL assessments using information retrieval techniques.

The solution includes:

- Web scraping of SHL product catalog (518 assessments)
- Vector-based retrieval using TF-IDF
- Fast similarity search using FAISS
- Evaluation using Recall@10
- Public API deployment (Render)
- Public frontend interface (Streamlit)

---

## System Architecture

Scraper → Data Storage → Embedding Generation → FAISS Index → FastAPI Backend → Streamlit Frontend

### Components

- `scraper/` – Scrapes SHL catalog
- `data/assessments.json` – Clean structured assessment data
- `embeddings/` – TF-IDF vector generation and FAISS index creation
- `retrieval/` – Recommendation logic
- `evaluation/` – Recall@10 evaluation on labeled dataset
- `api/` – FastAPI backend
- `frontend/` – Streamlit UI

---

## Data Collection

- Scraped 518 individual assessments from SHL product catalog
- Extracted:
  - Name
  - URL
  - Description
  - Test Type
  - Duration
  - Remote Support
  - Adaptive Support

Packaged solutions were excluded to ensure only individual assessments were indexed.

---

## Retrieval Method

- TF-IDF vectorization of assessment descriptions
- Query cleaning and preprocessing
- FAISS index for efficient similarity search
- Top-k retrieval (k=10)

---

## Evaluation

Evaluation dataset: Gen_AI Dataset.xlsx

Metric used:
- Recall@10

### Results

- Baseline Recall@10: 0.2255
- Improved Recall@10: 0.2455

---

---

## Frontend Deployment

Streamlit app deployed on Streamlit Cloud.

Users can:
- Enter job description
- Get top recommended SHL assessments
- View assessment URLs and descriptions

---

## Test Predictions

The file `test_predictions.csv` contains predictions generated for the test dataset.

---

## Future Improvements

- Replace TF-IDF with Sentence-BERT embeddings
- Hybrid ranking (metadata + semantic similarity)
- Fine-tuning using labeled dataset
- Reranking with cross-encoder models
- Filtering by duration constraints

---

## Author

Varshith Reddy

## API Deployment

Backend deployed on Render:

Health Endpoint:
