import json
from uuid import UUID
from flask import Response, request, Blueprint
from source.models.book.postgres import BookPostgresModel
from source.models.book.mongo import BookMongoModel
from source.services.book import BookService

book_blueprint = Blueprint('book', __name__, url_prefix='/books')

@book_blueprint.route('/', methods=['POST'])
def save()-> Response:
    """this function save books"""
    
    book_service = BookService(BookMongoModel)

    book = book_service.save(
        title=request.json["title"],
        description=request.json["description"],
        tags=request.json["tags"],
        publication_date=request.json["publication_date"]
    )

    return Response(json.dumps(book), status=201, mimetype='application/json')

@book_blueprint.route('/', methods=['GET'])
def list()-> Response:
    """list all books"""

    book_service = BookService(BookPostgresModel)

    book_list = book_service.list()

    return Response(json.dumps(book_list), status=200, mimetype='application/json')

@book_blueprint.route('/<string:id>', methods=['GET'])
def find_one(id: UUID)-> Response:
    """find one book"""

    book_service = BookService(BookPostgresModel)

    book = book_service.find_one(id)

    return Response(json.dumps(book), status=200, mimetype='application/json')

@book_blueprint.route('/<string:id>', methods=['PUT'])
def update_one(id: UUID)-> Response:
    """update a book"""
    
    book_service = BookService(BookPostgresModel)

    book = book_service.update_one(
        id=id,
        title=request.json["title"],
        description=request.json["description"],
        tags=request.json["tags"],
        publication_date=request.json["publication_date"]
    )

    return Response(json.dumps(book), status=200, mimetype='application/json')

@book_blueprint.route('/<string:id>', methods=['DELETE'])
def delete_one(id: UUID):
    """ delete a book"""
    
    book_service = BookService(BookPostgresModel)
    
    book = book_service.delete_one(id)
    
    return Response(book, status=204, mimetype='application/json')
