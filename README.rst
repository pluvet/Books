       ''' with mocker.patch.object(BookMongoModel, "find") as find_mocked:
        
        find_mocked.return_value = BookMongoModel(title="test", description='testD', tags=['tessT'], publication_date='1999-01-01')
        
        book = BookMongoModel.find('test')'''