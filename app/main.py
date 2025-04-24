from fastapi import FastAPI, HTTPException
from app.io_model import Job_Description, Job_Results, JobSearchOutput
from app.scraper_linkedin import fetch_linkedin_jobs
from app.scraper_indeed import fetch_indeed_jobs
from app.relevance_filtering import filter_relevant_jobs

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Job Finder API. Use /docs to test the /search-jobs endpoint."}

@app.post("/search-jobs", response_model=JobSearchOutput)
def search_jobs(input_data: Job_Description):
    try:
        linkedin_jobs = fetch_linkedin_jobs(input_data)
        indeed_jobs = fetch_indeed_jobs(input_data)

        all_jobs = linkedin_jobs + indeed_jobs
        relevant_jobs = filter_relevant_jobs(all_jobs, input_data)

        return JobSearchOutput(relevant_jobs=relevant_jobs)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
