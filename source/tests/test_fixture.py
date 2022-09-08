from uuid import UUID
from source.models.book.mongo import BookMongoModel
import pytest 

@pytest.fixture
def mock_book():
    
    book = BookMongoModel(
            title='testTitle',
            description='testDescription',
            tags=['testTags'],
            publication_date='2000-01-01',
            id= UUID('bb7b1a13-64cb-43fc-8ed8-7eee2bbd99d4')
        )

    return book

@pytest.fixture
def mock_find_one(mocker):
    return_value = {"_id": "a4f8d469-c652-41a3-9076-3b7df5bf129a","title":"test", "description":'testD', "tags":['tessT'], "publication_date":'1999-01-01'}

    mocker.patch('pymongo.collection.Collection.find_one', return_value=return_value)

    book = BookMongoModel.find("a4f8d469-c652-41a3-9076-3b7df5bf129a")

    return book

#TODO: 
    
    
