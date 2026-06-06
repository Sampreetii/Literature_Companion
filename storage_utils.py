import json
import os


BOOKS_FILE = "data/books.json"

CACHE_DIR = "data/cache"


os.makedirs(
    CACHE_DIR,
    exist_ok=True
)




def load_books():

    if not os.path.exists(
        BOOKS_FILE
    ):

        return []


    with open(
        BOOKS_FILE,
        "r",
        encoding="utf-8"
    ) as f:

        return json.load(f)




def save_books(books):

    with open(
        BOOKS_FILE,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            books,
            f,
            indent=4,
            ensure_ascii=False
        )




def add_book(title, total_pages):


    books = load_books()


    for book in books:

        if book["title"] == title:

            return


    books.append({

        "title": title,

        "current_page": 0,

        "total_pages": total_pages

    })


    save_books(
        books
    )




def update_progress(
    title,
    page
):


    books = load_books()


    for book in books:

        if book["title"] == title:

            book["current_page"] = page


    save_books(
        books
    )




def get_progress(title):


    books = load_books()


    for book in books:

        if book["title"] == title:

            return book[
                "current_page"
            ]


    return 0




def cache_path(title):


    safe = (

        title
        .replace(" ", "_")
        .lower()

    )


    return f"{CACHE_DIR}/{safe}.json"




def load_cache(title):


    path = cache_path(
        title
    )


    if not os.path.exists(
        path
    ):

        return {}


    with open(
        path,
        "r",
        encoding="utf-8"
    ) as f:

        return json.load(f)




def save_cache(
    title,
    cache
):


    path = cache_path(
        title
    )


    with open(
        path,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            cache,
            f,
            ensure_ascii=False,
            indent=4
        )