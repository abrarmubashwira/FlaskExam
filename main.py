from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'

db = SQLAlchemy(app)

#Defines the Book model
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable= False)
    author= db.Column(db.String(50), nullable=False)
    publication_year = db.Column(db.Integer, nullable=False)


def create_db():
    with app.app_context():
       db.create_all()

#Create the routes
@app.route('/')
def index():
    books = Book.query.all()
    return render_template('index.html', books=books)

@app.route('/add-book', methods=['GET', 'POST'])
def add_book():
    if request.method=='POST':
        title= request.form['title']
        author = request.form['author']
        publication_year = request.form['publication_year']


        new_book = Book(title=title, author=author, publication_year= publication_year)
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add-book.html', title='Add a book')

if __name__ == '__main__':
    create_db()
    app.run(port=5001, debug=True)

