from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ReadingEntryCreate(BaseModel):
    book_id: str
    title: str
    reflection: str
    emotional_score: int
    intellectual_score: int

class ReadingEntryOut(ReadingEntryCreate):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
