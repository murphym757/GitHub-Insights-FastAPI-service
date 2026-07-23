import respx
from httpx import Response
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


@respx.mock
def test_get_profile_success():
    username = "murphym757"
    
    respx.get(f"https://api.github.com/users/{username}").mock(
        return_value=Response(200, json={"login": username})
    )
    respx.get(f'https://api.github.com/users/{username}/repos').mock(
        return_value=Response(200, json=[
            {"name": "bayside-vaporwave", "stargazers_count": 10},
            {"name": "bayside-vaporwave-2", "stargazers_count": 5}
        ])
    )
    
    response = client.get(f"/profile/{username}")
    
    assert response.status_code == 200
    data = response.json()
    assert data["username"] == username
    assert data["repositories"] == 2
    assert data["total_stars"] == 15