from uuid import UUID
from source.models.book.mongo import BookMongoModel
from source.tests.test_fixture import mock_find_one

def test_save(mocker):  
    
    mocker.patch('pymongo.collection.Collection.find_one_and_update', return_value=None)

    book = BookMongoModel(
            title='title',
            description='description',
            tags=['tags'],
            publication_date='1999-01-01'
        )

    book.save()

    assert isinstance(book, BookMongoModel)

#estudiar fixture

def test_show(mocker):
    
    return_value = {"_id": "a4f8d469-c652-41a3-9076-3b7df5bf129a","title":"test", "description":'testD', "tags":['tessT'], "publication_date":'1999-01-01'}
    
    mocker.patch('pymongo.collection.Collection.find_one', return_value=return_value)

    book = BookMongoModel.find("a4f8d469-c652-41a3-9076-3b7df5bf129a")

    assert isinstance(book, BookMongoModel)

def test_list(mocker):

    return_value = [
        {"_id": "a4f8d469-c652-41a3-9076-3b7df5bf129a","title":"test", "description":'testD', "tags":['tessT'], "publication_date":'1999-01-01'},
        {"_id": "a4f8d469-c652-41a3-9076-3b7df5bf129b","title":"test2", "description":'testD2', "tags":['tessT2'], "publication_date":'1999-01-02'}
    ]
    
    mocker.patch('pymongo.collection.Collection.find', return_value=return_value)

    book = BookMongoModel.list()
    
    assert isinstance(book, list)

def test_update(mocker, mock_find_one):
    
    book = mock_find_one

    book.set(title='othertitle', description= 'otherD', tags=['otherT'], publication_date='1999-01-02')

    mocker.patch('pymongo.collection.Collection.find_one_and_update', return_value=None)

    book.save()
    
    assert isinstance(book, BookMongoModel)
    assert book.title == 'othertitle'

def test_delete (mocker, mock_find_one):

    book = mock_find_one
    
    mocker.patch('pymongo.collection.Collection.find_one_and_delete', return_value=None)

    book.delete()

    assert isinstance(book, BookMongoModel)
    