from uuid import UUID
from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from source.services.book import BookService
from source.models.book.mongo import BookMongoModel
from source.models.book.postgres import BookPostgresModel

book_router = APIRouter()
    
@book_router.post('/')
async def save(request: Request)-> JSONResponse:
    """this function save books"""
    request = await request.json()

    book_service = BookService(BookPostgresModel)

    book = book_service.save(
        title=request["title"],
        description=request["description"],
        tags=request["tags"],
        publication_date=request["publication_date"]
    )

    return JSONResponse(book, status_code=200)
#servicio

@book_router.get('/')
async def list()-> JSONResponse:
    """list all books"""
    
    book_service = BookService(BookPostgresModel)

    book_list = book_service.list()

    return JSONResponse(book_list, status_code=200)

@book_router.get('/{id}')
async def find_one(id: UUID)-> JSONResponse:
    """find one book"""
    
    book_service = BookService(BookPostgresModel)

    book = book_service.find_one(id)

    return JSONResponse(book, status_code=200)

@book_router.put('/{id}')
async def update_one(id: UUID, request: Request)-> JSONResponse:
    """update a book"""
    request = await request.json()
    
    book_service = BookService(BookPostgresModel)

    book = book_service.update_one(
        id=id,
        title=request["title"],
        description=request["description"],
        tags=request["tags"],
        publication_date=request["publication_date"]
    )

    return JSONResponse(book, status_code=200)

@book_router.delete('/{id}')
def delete_one(id: UUID)-> JSONResponse:
    """ delete a book"""
    
    book_service = BookService(BookPostgresModel)
    
    book = book_service.delete_one(id)
    
    return JSONResponse(book, status_code=204)