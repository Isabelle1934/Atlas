import requests

GOOGLE_BOOKS_API = "https://www.googleapis.com/books/v1/volumes"

def search_books(query: str, max_results: int = 10):
    params = {
        "q": query,
        "maxResults": max_results,
    }

    response = requests.get(GOOGLE_BOOKS_API, params=params)
    data = response.json()

    books = []

    for item in data.get("items", []):
        volume = item.get("volumeInfo", {})

        books.append({
            "id": item.get("id"),
            "title": volume.get("title"),
            "authors": volume.get("authors", []),
            "description": volume.get("description"),
            "thumbnail": volume.get("imageLinks", {}).get("thumbnail"),
            "published_date": volume.get("publishedDate"),
            "categories": volume.get("categories", [])
        })

    return books
