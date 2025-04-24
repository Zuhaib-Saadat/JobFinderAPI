# Job Finder API Documentation

This documentation explains the FastAPI-based Job Finder API developed for GoAccelovate. It covers the main endpoint, input/output structure, internal logic, and includes relevant screenshots.

---

## API Overview

**Base URL:** `http://127.0.0.1:8000`

### Endpoint: `POST /search-jobs`
This is the primary endpoint for retrieving job listings that match a user's preferences.

---

## Input Schema

**Model:** `Job_Description`
```json
{
  "position": "string",
  "experience": "string",
  "salary": "string",
  "jobNature": "string",
  "location": "string",
  "skills": "string"
}
```

### Example Input
```json
{
  "position": "React Developer",
  "experience": "2 years",
  "salary": "70,000 PKR to 100,000 PKR",
  "jobNature": "onsite",
  "location": "Karachi, Pakistan",
  "skills": "React, Firebase"
}
```

---

## Output Schema

**Model:** `JobSearchOutput`
```json
{
  "relevant_jobs": [
    {
      "job_title": "string",
      "company": "string",
      "experience": "string",
      "jobNature": "string",
      "location": "string",
      "salary": "string",
      "apply_link": "string"
    }
  ]
}
```

### Example Output
```json
{
  "relevant_jobs": [
    {
      "job_title": "React Developer",
      "company": "Glassdoor Pvt Ltd",
      "experience": "2 years",
      "jobNature": "onsite",
      "location": "Karachi, Pakistan",
      "salary": "85,000 PKR",
      "apply_link": "https://glassdoor.com/job789"
    }
  ]
}
```

---

## How Matching Works

### 1. Input Collection
User provides preferences like role, location, salary, and skills.

### 2. Simulated Job Scraping
- `scraper_indeed.py`
- `scraper_linkedin.py`

Both return mock job dictionaries.

### 3. LLM-based Filtering
- `relevance_filtering.py`
- Uses OpenAI's GPT to compare each job against the input preferences.
- Responds "Yes" or "No" — if "Yes", job is added to the output.

### 4. Final Output
Filtered job listings are returned in JSON format under the `relevant_jobs` key.

---

## Summary
- Endpoint accepts detailed job input from users
- Internally mocks data scraping
- Uses GPT filtering to match jobs
- Documented via Swagger
- Easily extendable with real APIs in production

