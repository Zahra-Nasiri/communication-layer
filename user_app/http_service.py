from settings import get_settings
from .models import User, UpdateUser, LoginUser
import requests

settings = get_settings()

class UserHttpService:

    user_service_url: str

    def __init__(self):
        self.user_service_url = settings.user_service_url

    async def register(self, user: User):
        request = requests.post(f"{self.user_service_url}/register", json=user.dict())
        return request.json()
