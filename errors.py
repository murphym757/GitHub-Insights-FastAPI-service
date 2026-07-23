from fastapi import HTTPException
import httpx

def check_github_response(response: httpx.Response, username: str) -> None:
    if response.status_code == 404:
        raise HTTPException(status_code=404, detail=f"'{username}' not found on GitHub.")
    
    if response.status_code == 403 and response.headers.get("X-RateLimit-Remaining") == "0":
        raise HTTPException(status_code=429, detail="Rate limit exceeded.")