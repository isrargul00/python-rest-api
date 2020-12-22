from flask import Flask,jsonify
app = Flask(__name__)
import json
books = [
    {
        "id": 1,
        "title": "Harry Potter and the Goblet of Fire",
        "author": "J.K. Rowling",
        "isbn": "1512379298"
    },
    {
        "id": 2,
        "title": "Lord of the Flies",
        "author": "William Golding",
        "isbn": "0399501487"
    }
]

@app.route('/')
def home():
    return jsonify({'books':books})

@app.route('/create')
def create():
    books.append(    {
        "id": 2,
        "title": "Lord of the Flies",
        "author": "William Golding",
        "isbn": "0399501487"
    })
    return jsonify({'books': books})


@app.route('/delete')
def delete():
    data = books.pop()
    return jsonify({'books': data})

if __name__ == '__main__':
    app.run(debug = True)

