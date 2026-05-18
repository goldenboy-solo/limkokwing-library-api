from fastapi import FastAPI
from typing import Dict
import asyncio
from datetime import datetime, timedelta

app = FastAPI(
    title="Limkokwing Library API System",
    description="A simple digital library management API for Limkokwing University Sierra Leone.",
    version="1.0.0"
)

@app.get("/")
async def home():
    return {"message": "Library API is running"}

books = {
    1: {
        "title": "Python Basics",
        "author": "Alusine Jalloh",
        "category": "Programming",
        "available": True
    },
    2: {
        "title": "Data Science Fundamentals",
        "author": "Saidu Bah",
        "category": "Data Science",
        "available": True
    },
    3: {
        "title": "Web Development with HTML",
        "author": "Michael Samura",
        "category": "Web Development",
        "available": True
    },
    4: {
        "title": "Machine Learning Essentials",
        "author": "Sarah Moseray",
        "category": "Artificial Intelligence",
        "available": True
    },
    5: {
        "title": "Introduction to Cybersecurity",
        "author": "Mohamed Lebbie",
        "category": "Security",
        "available": True
    },
    6: {
        "title": "Introduction to Databases",
        "author": "Ahmed Jelil",
        "category": "Database",
        "available": True
    },
    7: {
        "title": "Networking Concepts",
        "author": "Ibrahim Wurie Bah",
        "category": "Networking",
        "available": True
    },
    8: {
        "title": "Java Programming",
        "author": "Amadu Kamara",
        "category": "Programming",
        "available": True
    },
    9: {
        "title": "Cloud Computing",
        "author": "Amadu Kamara",
        "category": "Cloud Technology",
        "available": True
    },
    10: {
        "title": "Software Engineering Principles",
        "author": "Amadus Coker",
        "category": "Software Engineering",
        "available": True
    }
}

users = {
    5588: {
        "name": "Solomon Gibrilla Munu",
        "course": "DIT"
    },
    5582: {
        "name": "Fatmata Kamara",
        "course": "CIT"
    },
    5581: {
        "name": "Ibrahim Sesay",
        "course": "BIT"
    },
    5580: {
        "name": "Mariama Bangura",
        "course": "BBIT"
    },
    5583: {
        "name": "Joseph Koroma",
        "course": "BICT"
    },
    5584: {
        "name": "Hawa Conteh",
        "course": "DIB"
    },
    5585: {
        "name": "Mohamed Turay",
        "course": "DAB"
    },
    5586: {
        "name": "Aminata Kallon",
        "course": "ICT"
    },
    5587: {
        "name": "Abdul Barrie",
        "course": "DIT"
    },
    5589: {
        "name": "Isatu Sankoh",
        "course": "BIT"
    }
}

borrowed_books: Dict[int, Dict] = {}

@app.get("/books")
async def get_books():
    return books

@app.get("/users")
async def get_users():
    return users

@app.post("/borrow")
async def borrow_book(user_id: int, book_id: int):
    await asyncio.sleep(1)

    if user_id not in users:
        return {"message": "User not found"}

    if book_id not in books:
        return {"message": "Book not found"}

    if not books[book_id]["available"]:
        return {"message": "Book is already borrowed"}

    books[book_id]["available"] = False

    borrowed_books[book_id] = {
        "user_id": user_id,
        "borrow_date": str(datetime.now()),
        "due_date": str(datetime.now() + timedelta(days=7))
    }

    return {
        "message": "Book borrowed successfully",
        "book": books[book_id],
        "borrowed_by": users[user_id]
    }

@app.post("/return")
async def return_book(user_id: int, book_id: int):
    await asyncio.sleep(1)

    if book_id not in borrowed_books:
        return {"message": "Book was not borrowed"}

    books[book_id]["available"] = True

    del borrowed_books[book_id]

    return {"message": "Book returned successfully"}

@app.get("/borrowed")
async def get_borrowed_books():
    return borrowed_books