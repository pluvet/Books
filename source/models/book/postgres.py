from datetime import datetime
from typing import List, Optional
from psycopg2 import OperationalError, extras
import uuid
from source.models.book.base import BookBaseModel
from source.config.postgresdb import conn


class BookPostgresModel(BookBaseModel):
    """book class"""

    def __init__(self, title: str, description: str, tags: List[str], publication_date: datetime, id: Optional[uuid.UUID] = None):
 
        super().__init__(title, description, tags, publication_date, id)
    
    def save(self) -> None:
        """update or create a single book"""
        try:
            with conn.cursor() as cursor:

                query = '''
                    INSERT INTO books(id, title, description, tags, publication_date) 
                    VALUES (%s, %s, %s, %s, %s) 
                    ON CONFLICT (id) DO UPDATE SET
                    (title, description, tags, publication_date) = (EXCLUDED.title, EXCLUDED.description, EXCLUDED.tags, EXCLUDED.publication_date);
                '''
                
                cursor.execute(query, (str(self.id), self.title, self.description, self.tags, self.publication_date))

            conn.commit()
        except OperationalError:
            conn.rollback()
        
    @classmethod
    def list(cls) -> List['BookPostgresModel']:
        """list all books"""
        try:
            with conn.cursor(cursor_factory=extras.RealDictCursor) as cursor:
                
                cursor.execute("SELECT * FROM books;")
                
                books = cursor.fetchall()
                
            book_dict = []

            for book in books:
                book = dict(book)
                book_dict.append(cls(
                    title=book['title'],
                    description=book['description'],
                    tags=book['tags'],
                    publication_date=book['publication_date'],
                    id=book['id']
                ))
                
            return book_dict
        except OperationalError:
            conn.rollback()
    
    #class method or static y retorne una instancia de libro
    @classmethod
    def find(cls, id: str) -> 'BookPostgresModel':
        """find a single book"""
        try:
            with conn.cursor(cursor_factory=extras.RealDictCursor) as cursor:
                id = str(id)

                query = f'SELECT * FROM books WHERE id = \'{id}\';'

                cursor.execute(query)

                book = cursor.fetchone()
            
            if not book:   
                return None
            print(book)
            return cls(
                title=book['title'],
                description=book['description'],
                tags=book['tags'],
                publication_date=book['publication_date'],
                id=book['id']
            )

        except OperationalError:
            conn.rollback()

    def delete(self) -> None:
        """delete a single book"""
        try:
            with conn.cursor() as cursor:
                query = "DELETE FROM books WHERE id = %s;"
                
                id = str(self.id) 

                cursor.execute(query, (id,))
                
            conn.commit()

        except OperationalError:
            conn.rollback()
        