from datetime import datetime
from typing import List, Optional
import uuid
from source.models.book.base import BookBaseModel

class BookFakeModel(BookBaseModel):
    """book class"""

    def save(self) -> None:
        """update or create a single book"""
        pass

    @classmethod
    def list(cls) -> List['BookFakeModel']:
        """list all books"""
        
        books = [
            {"_id": "a4f8d469-c652-41a3-9076-3b7df5bf129a","title":"test", "description":'testD', "tags":['tessT'], "publication_date":'1999-01-01'},
            {"_id": "a4f8d469-c652-41a3-9076-3b7df5bf129b","title":"test2", "description":'testD2', "tags":['tessT2'], "publication_date":'1999-01-02'}
        ]
        
        book_list = []

        for book in books:
            book = dict(book)
            book_list.append(cls(
                title=book['title'],
                description=book['description'],
                tags=book['tags'],
                publication_date=book['publication_date'],
                id=book['_id']
            ))

        return book_list

    @classmethod
    def find(cls, id: str) -> 'BookFakeModel':
        """find a single book"""
        
        return cls(
            title='title',
            description='description',
            tags=['tags'],
            publication_date='1999-01-01',
            id='a4f8d469-c652-41a3-9076-3b7df5bf129a'
        )

    def delete(self) -> None:
        """delete a single book"""
        
        pass