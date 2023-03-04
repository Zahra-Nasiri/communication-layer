from settings import get_settings
from .models import Book, UpdateBook
import requests

settings = get_settings()

class BookHttpService:

    book_service_url: str

    def __init__(self):
        self.book_service_url = settings.book_service_url

    async def get_books(self):
        request = requests.get(f"{self.book_service_url}/")
        return request.json()

    # async def get_product(self, product_id: str):
    #     # send request to product sevice
    #     request = requests.get(
    #         f"{self.product_service_url}/{product_id}/"
    #     )
    #     return request.json()

    # async def create_product(self, product: Product):
    #     request = requests.post(f"{self.product_service_url}", json=product.dict())
    #     return request.json()

    # async def update_product(self, product_id: str, product: Product):
    #     request = requests.put(f"{self.product_service_url}/{product_id}", json=product.dict())
    #     return request.json()

    # async def partial_update_product(self, product_id: str, product: UpdateProduct):
    #     request = requests.patch(f"{self.product_service_url}/{product_id}", json=product.dict())
    #     return request.json()

    # async def delete_product(self, product_id: str):
    #     request = requests.delete(f"{self.product_service_url}/{product_id}")
    #     return request.json()

