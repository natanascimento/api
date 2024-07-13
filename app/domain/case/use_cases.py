from fastapi import Depends
from app.infrastructure.repositories.database import RepositoryTemplate
from app.routes.xpto.contracts import XPTORequest


class CreateXPTOTemplate:

    def __init__(self, repository: RepositoryTemplate = Depends()):
        self.__repository = repository

    def execute(self, request: XPTORequest):
        return self.__repository.create(request)