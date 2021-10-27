from app import db
from app.models.book import Book
from flask import Blueprint, jsonify, make_response,request 

# class Book:
#     def __init__(self, id, title, description):
#         self.id = id
#         self.title = title
#         self.description = description
# books = [Book(1, "Love", "A love story"), Book(2, "action", "wheel of time"), Book(3, "Fictional book title", "A fantasy stoty")]

books_bp = Blueprint("books_bp", __name__,url_prefix="/books")
@books_bp.route("", methods=["POST", "GET"])
def handle_books():
    if request.method == "POST":
        request_body = request.get_json()
        
        if "title" not in request_body or "description" not in request_body:
            return make_response("Invalid request", 400)
        new_book = Book(
            title = request_body["title"],
            description=request_body["description"]

        )
        db.session.add(new_book)
        db.session.commit()

        return make_response(
            f"Book {new_book.title} created", 201
        )
        # return f"Book {new_book.title} created", 201 we can return a tuple without the response object
    elif request.method == "GET":
        # Book.query.filter_by(title="arifee").first()
        # Book.query.limit(100).all()
        title_query = request.args.get("title")  # this is getting the word title in the url and store its value
        # in title_query
        if title_query:  # if there is a query parameter at all with title, then ...
            books = Book.query.filter_by(title=title_query)   # get those books with title == title_query
        else: # else there is no query param and filter in the request, then process to get all books
           books = Book.query.all()
        # if books is []:
        #    return make_response(f"Nothing found", 404)
        # books_response = []
        # for book in books:
        #     books_response.append({"id":book.id, 
        #     "title":book.title, "description":book.description
        #     }
        #     )
        books_response = [book.to_dict() for book in books]
        
        return jsonify(books_response)
@books_bp.route("/<book_id>",methods = ["GET", "PUT", "DELETE"])
def handle_book(book_id):
    # book_id = int(book_id)
    book = Book.query.get(book_id)
    

    if book is None:
        return make_response(f"Book {book_id} not found and check the branch", 404)
        # return {"id": book.id,
        #         "title":book.title,
        #         "description": book.description
                
        #         }
    if request.method == "GET":
        return book.to_dict()

    elif request.method == "PUT":
        form_data = request.get_json()
        book.title = form_data["title"]
        book.description = form_data["description"]

        db.session.commit()

        return make_response(f"Book with #{book.id} updated successfully", 201)
    
    elif request.method == "DELETE":
        db.session.delete(book)
        db.session.commit()
        return make_response(f"Book with #{book_id} deleted")



# hello_world_bp = Blueprint("hello_world", __name__)
# @hello_world_bp.route('/hello-world', methods=["GET"])
# def get_hello_world():
#     my_response = "Hello, world!"
#     return my_response

# @hello_world_bp.route('/hello-world/JSON', methods=["GET"])
# def get_hello_world_json():
#     return {
#         "name" : "HEYA",
#         "message" : "coding is not fun",
#         "hobbies" : ["coding", "writing","singing", "praying"]
#     },201

# @hello_world_bp.route("/broken-endpoint-with-broken-server-code")
# def broken_endpoint():
#     response_body = {
#         "name": "Ada Lovelace",
#         "message": "Hello!",
#         "hobbies": ["Fishing", "Swimming", "Watching Reality Shows"]
#     }
#     new_hobby = "Surfing"
#     response_body["hobbies"].append(new_hobby)
#     return response_body


