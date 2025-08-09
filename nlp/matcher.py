from sklearn.metrics.pairwise import cosine_similarity

def match_resume_to_job(resume_vec, job_vec):
    sim = cosine_similarity([resume_vec], [job_vec])[0][0]
    return float(sim)
