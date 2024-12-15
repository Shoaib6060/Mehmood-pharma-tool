
import streamlit as st
import pandas as pd
import re

# Sample dataset (to be replaced with a larger dataset)
data = {
    "Drug Name": ["Paracetamol", "Ibuprofen", "Aspirin"],
    "Description": [
        "Paracetamol is a medication used to treat fever and mild to moderate pain.",
        "Ibuprofen is a nonsteroidal anti-inflammatory drug (NSAID) used to reduce fever and treat pain or inflammation.",
        "Aspirin is used to reduce pain, fever, or inflammation and is also used as a blood thinner."
    ],
}

# Convert to DataFrame
pharmacy_data = pd.DataFrame(data)

# Function to search for a drug and return its description
def search_drug(query):
    query = query.lower().strip()  # Normalize query text
    for index, row in pharmacy_data.iterrows():
        if re.search(query, row["Drug Name"].lower()):
            return f"**{row['Drug Name']}**: {row['Description']}"
    return "Sorry, I couldn't find information on that drug. Please try another query."

# Streamlit app
st.title("Pharmacy Educational Tool - #Mehmoodpharma")
st.write("Type the name of a drug to learn more about it.")

# Input field for user query
user_query = st.text_input("Enter drug name:")

# Display results when a query is entered
if user_query:
    result = search_drug(user_query)
    st.markdown(result)
