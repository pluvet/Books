from datetime import datetime
from typing import List, Optional
import uuid

class BookBaseModel:
    """book class"""

    id= uuid.UUID
    title: str
    description: str
    tags: List[str]
    publication_date: datetime

    def __init__(self, title: str, description: str, tags: List[str], publication_date: datetime, id: Optional[uuid.UUID] = None):
 
        if not id:
            self.id = uuid.uuid4()
        else:
            self.id = id
       
        self.title = title

        self.description = description
        
        self.tags = tags

        self.publication_date = publication_date
        
    def set(self, title: Optional[str], description: Optional[str], tags: Optional[List[str]], publication_date: Optional[datetime]) -> None:
        """set some arguments"""
        if title:
            self.title = title

        if description:
            self.description = description

        if tags:
            self.tags = tags

        if publication_date:
            self.publication_date = publication_date
    
    def save(self):
        """save """
        raise NotImplementedError("please use a child class")

    @classmethod
    def list(cls):
        """list all books"""
        raise NotImplementedError("please use a child class")
    
    @classmethod
    def find(cls, id: str):
        """find a single book"""
        raise NotImplementedError("please use a child class")

    def delete(self) -> None:
        """delete a single book"""
        raise NotImplementedError("please use a child class")
    
    
        

