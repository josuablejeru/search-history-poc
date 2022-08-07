import string
from pydantic import BaseModel


class UserSession(BaseModel):
    orgId: string
    userId: string
