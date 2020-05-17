from flask import Flask, json
import requests

app = Flask(__name__)

@app.route('/')
def home_page():
    return 'HOME PAGE'


@app.route('/posts')
def get_all_posts():
    data_response = requests.get('https://jsonplaceholder.typicode.com/posts')
    posts = data_response.json()

    response = app.response_class(
        response= json.dumps(posts),
        status=200,
        mimetype='application/json')
    return response


@app.route('/posts/<post_id>')
def get_post(post_id):
    data_response = requests.get('https://jsonplaceholder.typicode.com/posts/'+ post_id)
    post =data_response.json()

    response = app.response_class(
        response=json.dumps(post),
        status=200,
        mimetype='application/json')
    return response

