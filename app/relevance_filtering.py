from dotenv import load_dotenv
import os, openai
from app.io_model import Job_Description, Job_Results

load_dotenv()  
openai.api_key = os.getenv("OPENAI_API_KEY")

def filter_relevant_jobs(job_list: list[Job_Results], input_data: Job_Description) -> list[Job_Results]:
    relevant = []
    for job in job_list:
        # Fixed: use input_data.position instead of input_data.job_title
        prompt = f"""
Job title: {job.job_title}
Company: {job.company}
Location: {job.location}
Experience: {job.experience}
Candidate skills: {input_data.skills}

User wants:
• Position: {input_data.position}
• Experience: {input_data.experience}
• Location: {input_data.location}
• Salary: {input_data.salary}
• Nature: {input_data.jobNature}

Reply only \"Yes\" or \"No\": should we include this job?
"""
        try:
            resp = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role":"user","content":prompt}],
                temperature=0
            )
            decision = resp.choices[0].message.content.strip().lower()
            if decision == "yes":
                relevant.append(job)
        except openai.error.OpenAIError as err:
            print(f"LLM error for {job.job_title}: {err}")
    return relevant
