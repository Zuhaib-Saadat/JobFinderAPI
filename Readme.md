# Job Finder API

This document serves as the complete technical documentation for the FastAPI-based Job Finder API built as part of the GoAccelovate assessment. It explains the API's working, input/output schemas, internal logic, and expected behavior.

## Endpoint

### `POST /search-jobs`

This is the **core endpoint** used to retrieve job listings that match the user's preferences.

### Purpose:
- Accepts user job preferences
- Aggregates jobs from simulated sources (LinkedIn, Indeed)
- Uses LLM-based filtering to return only relevant jobs

---

## Input Schema (JSON Request)

```json
{
  "position": "string",
  "experience": "string",
  "salary": "string",
  "jobNature": "string",
  "location": "string",
  "skills": "string"
}
