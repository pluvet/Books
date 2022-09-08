from datetime import date
from typing import List, Optional
import uuid
from source.models.book.base import BookBaseModel
from source.views.book import BookView
from werkzeug.exceptions import NotFound



class BookService:
    """Bookactions """
    book_model: BookBaseModel
    
    def __init__(self, book_model):
        
        self.book_model = book_model

    def save(self, title: str, description: str, tags: List[str], publication_date: date)-> dict:
        """this function save books"""

        book = self.book_model(
            title=title,
            description=description,
            tags=tags,
            publication_date=publication_date
        )

        book.save()

        return BookView.show(book)

    def list(self)-> dict:
        """list all books"""

        book_list = self.book_model.list()

        return BookView.show_many(book_list)

    def find_one(self, id: uuid.UUID)-> dict:
        """find one book"""

        book = self.book_model.find(id)

        if not book:
            raise NotFound('book not found')

        return BookView.show(book)

    def update_one(self, id: uuid.UUID, title: Optional[str] = None, description: Optional[str] = None, tags: Optional[List[str]] = None, publication_date: Optional[date] = None)-> dict:
        """update a book"""
        
        book = self.book_model.find(id)

        if not book:
            raise NotFound('book not found')

        book.set(
            title=title,
            description=description,
            tags=tags,
            publication_date=publication_date
        )

        book.save()

        return BookView.show(book)

    def delete_one(self, id: uuid.UUID):
        """ delete a book"""
        
        book = self.book_model.find(id)

        if not book:
            raise NotFound('book not found')
        
        book.delete()
        
        return None
