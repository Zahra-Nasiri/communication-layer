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

    async def get_book(self, book_id: str):
        request = requests.get(
            f"{self.book_service_url}/{book_id}/"
        )
        return request.json()

    async def create_book(self, book: Book):
        request = requests.post(f"{self.book_service_url}", json=book.dict())
        return request.json()

    async def partial_update_book(self, book_id: str, book: UpdateBook):
        request = requests.patch(f"{self.book_service_url}/{book_id}", json=book.dict())
        return request.json()

    async def delete_book(self, book_id: str):
        request = requests.delete(f"{self.book_service_url}/{book_id}")
        return request.json()

