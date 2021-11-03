from app import db
class Book(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    title = db.Column (db.String)
    description = db.Column(db.String)
    __tablename__ = "books"
   # ...if we wanna change table name to books
    # Book is a class name and it is going to be connected to a table name book in postgres
    # books plural for table and book singular personal preference
    # def_to_string(self):
    #     return f"{self.id}: {self.title} Description: {self.description}"

    def to_dict(self):
        return {
               "id" : self.id,
               "title" : self.title,
               "description": self.description

        }