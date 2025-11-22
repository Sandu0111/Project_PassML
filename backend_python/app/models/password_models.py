from pydantic import BaseModel
from typing import List


class PasswordAnalyzeRequest(BaseModel):
    password:str

class PasswordAnalyzeResponse(BaseModel):
    score:int
    strength:str
    issues:List[str]
    suggestions:List[str]