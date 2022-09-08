from fastapi import FastAPI
from source.controllers.book_fast import book_router

app = FastAPI()

app.include_router(book_router, prefix='/books')

#crear una suite de test para el servicio, aprovechar la inv de dependencias para un modelo fake para el testing de service para evitar mockear
#
