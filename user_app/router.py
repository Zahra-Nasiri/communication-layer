from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
from .models import User
from .http_service import UserHttpService

router = InferringRouter()
http_service = UserHttpService()

@cbv(router)
class UserRouter:

    @router.post("/register")
    async def register(self, user: User):
        return await http_service.register(user)