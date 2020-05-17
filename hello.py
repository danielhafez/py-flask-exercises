from flask import Flask, json
import requests

app = Flask(__name__)

@app.route('/')
def home_page():
    return 'HOME PAGE'


@app.route('/posts')
def get_posts():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    posts = response.json()

    # return the data to the client using a response object
    response = app.response_class(
        response= json.dumps(posts),
        status=200,
        mimetype='application/json')
    return response

