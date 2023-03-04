from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
from .http_service import BookHttpService
from .models import Book, UpdateBook
from fastapi import Header
from user_app.http_service import UserHttpService


router = InferringRouter()
http_servie = BookHttpService()
user_http_service = UserHttpService()

@cbv(router)
class BookRouter:

    @router.get("/")
    async def get_books(self):
        return await http_servie.get_books()

    @router.get("/{book_id}")
    async def get_book(self, book_id: str):
        return await http_servie.get_book(book_id)

    @router.post("/")
    async def create_book(self, book: Book, token: str = Header()):
        user_object = await user_http_service.get_user_by_token(token)
        if user_object["is_admin"]:
            return await http_servie.create_book(book)
        else:
            return {"message": "Only admin user can add books"}

    # @router.put("/{product_id}")
    # async def update_product(self, product_id: str, product: Product):
    #     return await http_servie.update_product(product_id, product)

    # @router.patch("/{product_id}")
    # async def partial_update_product(self, product_id: str, product: UpdateProduct):
    #     return await http_servie.partial_update_product(product_id, product)

    # @router.delete("/{product_id}")
    # async def delete_product(self, product_id: str):
    #     return await http_servie.delete_product(product_id)
