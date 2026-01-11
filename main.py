from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import Base, engine, SessionLocal
from schemas import ReadingEntryCreate, ReadingEntryOut
from reviews import create_entry, get_entries_by_book
from books import search_books
from typing import List

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Atlas API",
    description="Global library of books and ideas",
    version="0.2.0"
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/books/search")
def search_books_endpoint(q: str):
    return search_books(q)

@app.post("/entries", response_model=ReadingEntryOut)
def add_entry(entry: ReadingEntryCreate, db: Session = Depends(get_db)):
    return create_entry(db, entry)

@app.get("/entries/{book_id}", response_model=List[ReadingEntryOut])
def list_entries(book_id: str, db: Session = Depends(get_db)):
    return get_entries_by_book(db, book_id)
