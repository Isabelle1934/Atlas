from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime
from database import Base

class ReadingEntry(Base):
    __tablename__ = "reading_entries"

    id = Column(Integer, primary_key=True, index=True)
    book_id = Column(String, index=True)
    title = Column(String)
    reflection = Column(Text)
    emotional_score = Column(Integer)   # 0–10
    intellectual_score = Column(Integer) # 0–10
    created_at = Column(DateTime, default=datetime.utcnow)
