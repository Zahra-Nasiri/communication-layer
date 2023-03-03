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

    async def login(self, user: LoginUser):
        request = requests.post(f"{self.user_service_url}/login", json=user.dict())
        return request.json()

    async def partial_update_user(self, uid: str, user: UpdateUser):
        request = requests.patch(f"{self.user_service_url}/{uid}", json=user.dict())
        return request.json()

    async def get_user_by_token(self, token: str):
        request = requests.get(f"{self.user_service_url}/",
                headers={'Authorization': f"Bearer {token}"},
        )
        return request.json()