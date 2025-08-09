from fastapi import FastAPI, UploadFile, Form
from nlp.parser import parse_resume
from nlp.featurizer import featurize_texts
from nlp.matcher import match_resume_to_job

app = FastAPI()

@app.post("/match")
async def match_endpoint(file: UploadFile, job_desc: str = Form(...)):
    parsed_resume = parse_resume(await file.read())
    features = featurize_texts([parsed_resume, job_desc])
    score = match_resume_to_job(features[0], features[1])
    return {"match_score": score}
