from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
from .http_service import BookHttpService
from .models import Product, UpdateProduct


router = InferringRouter()
http_servie = BookHttpService()

@cbv(router)
class BookRouter:
    pass
    @router.get("/")
    async def get_books(self):
        return await http_servie.get_books()

    # @router.get("/{product_id}")
    # async def get_product(self, product_id: str):
    #     return await http_servie.get_product(product_id)

    # @router.post("/")
    # async def create_product(self, product: Product):
    #     return await http_servie.create_product(product)

    # @router.put("/{product_id}")
    # async def update_product(self, product_id: str, product: Product):
    #     return await http_servie.update_product(product_id, product)

    # @router.patch("/{product_id}")
    # async def partial_update_product(self, product_id: str, product: UpdateProduct):
    #     return await http_servie.partial_update_product(product_id, product)

    # @router.delete("/{product_id}")
    # async def delete_product(self, product_id: str):
    #     return await http_servie.delete_product(product_id)
