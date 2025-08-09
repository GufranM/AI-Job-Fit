
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from nlp.parser import parse_resume
from nlp.featurizer import featurize_texts
from nlp.matcher import match_resume_to_job
import pandas as pd

st.set_page_config(page_title="AI-JobFit", layout="wide")

st.title("🤖 AI-JobFit — Resume & Job Description Matcher")
st.markdown("Upload your resume and paste the job description to see the match score.")

uploaded_resume = st.file_uploader("Upload Resume (TXT or PDF)", type=["txt", "pdf"])
job_description = st.text_area("Paste Job Description", height=200)

if st.button("Match Now"):
    if uploaded_resume and job_description.strip():
        parsed_resume = parse_resume(uploaded_resume)
        features = featurize_texts([parsed_resume, job_description])
        score = match_resume_to_job(features[0], features[1])
        st.metric("Match Score", f"{score:.2f} / 1.00")
    else:
        st.warning("Please upload a resume and enter a job description.")
