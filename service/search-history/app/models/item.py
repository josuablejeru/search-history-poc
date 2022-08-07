from pydantic import BaseModel


class Item(BaseModel):
    entityId: str
