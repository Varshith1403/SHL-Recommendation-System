import streamlit as st
import requests

API_URL = "https://shl-recommendation-system-29sw.onrender.com"

st.title("SHL Assessment Recommendation System")

query = st.text_area("Enter Job Description or Query")

if st.button("Recommend"):
    if query.strip() == "":
        st.warning("Please enter a query.")
    else:
        try:
            response = requests.post(
                f"{API_URL}/recommend",
                json={"query": query},
                timeout=30
            )

            data = response.json()

            for item in data["recommended_assessments"]:
                st.subheader(item["assessment_name"])
                st.write(item["url"])
                st.write(item["description"])
                st.write("---")

        except Exception as e:
            st.error(f"Error: {e}")