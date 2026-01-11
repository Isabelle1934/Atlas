from sqlalchemy.orm import Session
from models import ReadingEntry

def create_entry(db: Session, entry):
    db_entry = ReadingEntry(**entry.dict())
    db.add(db_entry)
    db.commit()
    db.refresh(db_entry)
    return db_entry

def get_entries_by_book(db: Session, book_id: str):
    return db.query(ReadingEntry)\
             .filter(ReadingEntry.book_id == book_id)\
             .order_by(ReadingEntry.created_at.desc())\
             .all()
