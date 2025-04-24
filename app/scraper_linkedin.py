import requests
from bs4 import BeautifulSoup
from app.io_model import Job_Description, Job_Results

def fetch_linkedin_jobs(input_data: Job_Description):
    # I constructed the LinkedIn job search URL using the job title and location from the input data.
    search_url = (
        f"https://www.linkedin.com/jobs/search/"
        f"?keywords={input_data.job_title}&location={input_data.location}"
        f"&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0"
    )
    
    # I added headers to mimic a browser request to avoid being blocked by LinkedIn.
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    # I sent a GET request to the LinkedIn job search URL and checked if the response was successful.
    response = requests.get(search_url, headers=headers)
    if response.status_code != 200:
        raise Exception("Failed to fetch data from LinkedIn")
    
    # I used BeautifulSoup to parse the HTML content of the response.
    soup = BeautifulSoup(response.text, 'html.parser')
    job_results = []
    
    # I looped through each job card on the page to extract job details.
    # I updated the selectors based on LinkedIn's HTML structure to ensure accurate data extraction.
    for job_card in soup.select('.job-card-container'):
        # I extracted the job title, company name, location, and apply link from each job card.
        job_title = job_card.select_one('.job-card-list__title').text.strip()
        company = job_card.select_one('.job-card-container__company-name').text.strip()
        location = job_card.select_one('.job-card-container__metadata-item').text.strip()
        apply_link = job_card.select_one('a')['href']
        
        # I appended the extracted job details to the job_results list as Job_Results objects.
        job_results.append(
            Job_Results(
                job_title=job_title,
                company=company,
                experience="N/A",  # I left experience as "N/A" since it's not available in the current structure.
                jobNature="N/A",   # I left job nature as "N/A" since it's not available in the current structure.
                location=location,
                salary="N/A",      # I left salary as "N/A" since it's not available in the current structure.
                apply_link=apply_link
            )
        )
    
    # I returned the list of job results.
    return job_results
