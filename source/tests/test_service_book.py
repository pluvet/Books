from source.models.book.fake import BookFakeModel
from source.services.book import BookService

def test_save():
    
    book_service = BookService(BookFakeModel)

    book = book_service.save(title='test', description='desc', tags=['tag'], publication_date='1999-01-01')
    
    assert isinstance(book, dict)
    
def test_list():
    
    book_service = BookService(BookFakeModel)
    
    book = book_service.list()
    
    assert isinstance(book, list)
    
def test_find():
    
    book_service = BookService(BookFakeModel)
    
    book = book_service.find_one('a4f8d469-c652-41a3-9076-3b7df5bf129a')
    
    assert isinstance(book, dict)
    
def test_update():
    
    book_service = BookService(BookFakeModel)
    
    book = book_service.update_one('a4f8d469-c652-41a3-9076-3b7df5bf129a')
    
    assert isinstance(book, dict)
    
def test_delete():
    
    book_service = BookService(BookFakeModel)
    
    book = book_service.delete_one('a4f8d469-c652-41a3-9076-3b7df5bf129a')

    assert not book

#patron adapter

    