# GitHub Insights

A small async FastAPI service that aggregates a GitHub user's public repo data into a single, clean JSON summary.

# Goal
Built while learning FastAPI and GitHub Actions hands-on, using AI-assisted guidance to work through the concepts and debug real issues along the way — part of a broader push toward becoming more proficient in Python and cloud-adjacent tooling.

## Example

`GET /profile/murphym757`

```json
{
  "username": "murphym757",
  "repositories": 24,
  "total_stars": 2
}
```

## Setup

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

Visit `http://127.0.0.1:8000/docs` for the interactive API docs.

## Testing

```bash
pytest tests/ -v
```

Tests mock the GitHub API using `respx` — no live network calls required.

![Tests](https://github.com/murphym757/GitHub-Insights-FastAPI-service/actions/workflows/test.yml/badge.svg)