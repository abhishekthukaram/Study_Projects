from flask import Flask
from flask import request, jsonify

app = Flask(__name__)


app.config["DEBUG"] = True


@app.route("/")
def hello():
    return "<h1>Hello World</h1><p>This site is my first developed website.</p>"


books = [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'year_published': '1992'},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'published': '1973'},
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'}
]


@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
    return jsonify(books)


@app.route('/api/v1/resources/books/id', methods=['GET'])
def api_id():
    result = []
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error:Please specify an id"
    for book in books:
        if book['id'] == id:
            result.append(book)
    return jsonify(result)


app.run()
"""
if __name__ == "main":
    app.run(debug=True)
"""
