from datetime import datetime
from typing import List, Optional
import uuid
from source.models.book.base import BookBaseModel
from source.config.mongodb import conn

class BookMongoModel(BookBaseModel):
    """book class"""

    def __init__(self, title: str, description: str, tags: List[str], publication_date: datetime, id: Optional[uuid.UUID] = None):
 
        super().__init__(title, description, tags, publication_date, id)
    
    def save(self) -> None:
        """update or create a single book"""
        id = {"_id": self.id}

        conn.local.book.find_one_and_update(id,{
            "$set": {
                'title':self.title,
                'description':self.description,
                'tags':self.tags,
                'publication_date':self.publication_date,
                '_id':self.id
            }
        }, upsert = True) # -> None

    @classmethod
    def list(cls) -> List['BookMongoModel']:
        """list all books"""
        
        books = list(conn.local.book.find())
        
        book_dict = []

        for book in books:
            book = dict(book)
            book_dict.append(cls(
                title=book['title'],
                description=book['description'],
                tags=book['tags'],
                publication_date=book['publication_date'],
                id=book['_id']
            ))
            
        return book_dict

    @classmethod
    def find(cls, id: str) -> 'BookMongoModel':
        """find a single book"""
        
        id = {"_id": uuid.UUID(id)}

        book = conn.local.book.find_one(id)
        
        print(book)
        print(type(book))
        
        if not book:   
            return None
        
        return cls(
            title=book['title'],
            description=book['description'],
            tags=book['tags'],
            publication_date=book['publication_date'],
            id=book['_id']
        )

    def delete(self) -> None:
        """delete a single book"""
        
        id = {"_id": self.id}

        conn.local.book.find_one_and_delete(id)
        

