from pydantic import BaseModel, Field
from typing import List

class Job_Description(BaseModel):
    position: str                    
    experience: str
    salary: str
    jobNature: str = Field(..., description="Nature of the job")
    location: str = Field(default="Islamabad")
    skills: str = Field(..., description="Comma-separated list of skills")

class Job_Results(BaseModel):
    job_title:   str
    company:     str
    experience:  str
    jobNature:   str
    location:    str
    salary:      str
    apply_link:  str

class JobSearchOutput(BaseModel):
    relevant_jobs: List[Job_Results]
