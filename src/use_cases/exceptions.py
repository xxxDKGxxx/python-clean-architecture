from fastapi import HTTPException


class NotFoundError(HTTPException):
    def __init__(self, message):
        super().__init__(404, message)