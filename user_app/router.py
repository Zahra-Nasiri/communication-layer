from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
from .models import User, LoginUser, UpdateUser
from .http_service import UserHttpService
from fastapi import Header

router = InferringRouter()
http_service = UserHttpService()

@cbv(router)
class UserRouter:

    @router.post("/register")
    async def register(self, user: User):
        return await http_service.register(user)

    @router.post("/login")
    async def login(self, user: LoginUser):
        return await http_service.login(user)

    @router.patch("/")
    async def partial_update_user(self, user: UpdateUser, token: str=Header()):
        user_object = await http_service.get_user_by_token(token)
        return await http_service.partial_update_user(user_object["_id"], user)