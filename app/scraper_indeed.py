from app.io_model import Job_Description, Job_Results
import requests
from bs4 import BeautifulSoup

def fetch_indeed_jobs(input_data: Job_Description):
    #  URL for Indeed job search
    base_url = "https://www.indeed.com/jobs"
    params = {
        'q': input_data.position,  # Use 'position' instead of 'job_title'
        'l': input_data.location,  # Location
    }
    response = requests.get(base_url, params=params)
    if response.status_code != 200:
        print("Failed to fetch jobs from Indeed")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    job_cards = soup.find_all('div', class_='job_seen_beacon')

    results = []
    for job_card in job_cards:
        job_title = job_card.find('h2', class_='jobTitle').text.strip() if job_card.find('h2', class_='jobTitle') else "N/A"
        company = job_card.find('span', class_='companyName').text.strip() if job_card.find('span', class_='companyName') else "N/A"
        location = job_card.find('div', class_='companyLocation').text.strip() if job_card.find('div', class_='companyLocation') else "N/A"
        salary = job_card.find('span', class_='salary-snippet').text.strip() if job_card.find('span', class_='salary-snippet') else "N/A"
        apply_link = f"https://www.indeed.com{job_card.find('a', class_='jcs-JobTitle')['href']}" if job_card.find('a', class_='jcs-JobTitle') else "N/A"

        results.append(Job_Results(
            job_title=job_title,
            company=company,
            experience="N/A",  # Experience is not always available on Indeed
            jobNature="N/A",  # Job nature is not always available on Indeed
            location=location,
            salary=salary,
            apply_link=apply_link
        ))

    return results
