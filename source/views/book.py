from flask import Response
from typing import List
from source.models.book.base import BookBaseModel # pylint: disable=import-error

class BookView():
    """class for book views"""
    
    @staticmethod
    def show(book: BookBaseModel)-> Response:
        """show a book"""
        book = book.__dict__

        book["id"] = str(book["id"])
        
        book['publication_date'] = str(book['publication_date'])

        return book
    
    @staticmethod
    def show_many(books: List[BookBaseModel])-> Response:
        """show list of book created"""
        
        books_dict = []
        
        for book in books:

            book_dict = book.__dict__

            book_dict['id'] = str(book_dict['id'])
            
            book_dict['publication_date'] = str(book_dict['publication_date'])

            books_dict.append(book_dict)
            
        return books_dict
    

