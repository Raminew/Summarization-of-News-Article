# -*- coding: utf-8 -*-
"""
Created on Sun May 11 22:25:59 2025
@author: ramib
"""

import streamlit as st
from transformers import BartTokenizer, BartForConditionalGeneration
import os

# Get the current directory of the app.py script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Define the model path relative to the script location
model_path = os.path.join(current_dir, 'bart_summarization_model')

# Load the model and tokenizer
model = BartForConditionalGeneration.from_pretrained(model_path)
tokenizer = BartTokenizer.from_pretrained(model_path)

# Streamlit app title
st.title("📰 News Article Summarizer")

# Text input for the article
article_text = st.text_area("Enter the news article text here:")

# When the button is clicked, generate the summary
if st.button("Summarize"):
    if article_text.strip() == "":
        st.warning("Please enter some text to summarize.")
    else:
        # Tokenize and generate the summary
        inputs = tokenizer.encode(article_text, return_tensors='pt', max_length=1024, truncation=True)
        summary_ids = model.generate(inputs, num_beams=4, max_length=150, min_length=30, early_stopping=True)
        summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
        
        # Display the summary
        st.subheader("Summary:")
        st.write(summary)
