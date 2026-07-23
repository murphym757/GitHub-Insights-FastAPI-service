from fastapi import FastAPI
import httpx
from models import ProfileSummary
from errors import check_github_response

app = FastAPI()

@app.get('/profile/{username}', response_model=ProfileSummary)
async def get_profile(username: str):
    async with httpx.AsyncClient() as client:
        user_response = await client.get(f'https://api.github.com/users/{username}')
        check_github_response(user_response, username)
        repos_response = await client.get(f'https://api.github.com/users/{username}/repos')
        check_github_response(repos_response, username)
    
    user_data = user_response.json()
    repos_data = repos_response.json()
    
    total_stars = sum(repo['stargazers_count'] for repo in repos_data)
    
    return ProfileSummary(
        username=user_data["login"],
        repositories=len(repos_data),
        total_stars=total_stars
    )