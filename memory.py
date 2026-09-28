
import os
import requests
from dotenv import load_dotenv
from hindsight_client import Hindsight

load_dotenv()

import streamlit as st

API_KEY = st.secrets["HINDSIGHT_API_KEY"]
BANK_ID = "feedbackvault"

client = Hindsight(
    base_url="https://api.hindsight.vectorize.io",
    api_key=API_KEY
)

def retain_memory(content):
    """Store new organizational experience in Hindsight."""
    return client.retain(
        bank_id=BANK_ID,
        content=content
    )

def recall_memory(query):
    """Recall relevant organizational experience from Hindsight."""
    response = requests.post(
        f"https://api.hindsight.vectorize.io/v1/default/banks/{BANK_ID}/memories/recall",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        },
        json={"query": query},
        timeout=20
    )

    response.raise_for_status()

    data = response.json()

    return data.get("results", [])