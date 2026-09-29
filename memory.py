import requests
import streamlit as st

API_KEY = st.secrets["HINDSIGHT_API_KEY"]
BANK_ID = "feedbackvault"

BASE_URL = "https://api.hindsight.vectorize.io"


def retain_memory(content):
    """Store new organizational experience in Hindsight using REST API."""

    response = requests.post(
        f"{BASE_URL}/v1/default/banks/{BANK_ID}/memories",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "items": [
                {
                    "content": content
                }
            ]
        },
        timeout=30
    )

    response.raise_for_status()
    return response.json()


def recall_memory(query):
    """Recall relevant organizational experience from Hindsight."""

    response = requests.post(
        f"{BASE_URL}/v1/default/banks/{BANK_ID}/memories/recall",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "query": query
        },
        timeout=20
    )

    response.raise_for_status()

    data = response.json()

    return data.get("results", [])
