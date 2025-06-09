from pydantic import BaseModel

class RandomIdResponse(BaseModel):
    name: str
    id: str 