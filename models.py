from pydantic import BaseModel

class ProfileSummary(BaseModel):
    username: str
    repositories: int
    total_stars: int