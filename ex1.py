from flask import Flask, json
import requests
from JsonablePost import JsonablePost

app = Flask(__name__)

posts_storage = {}

@app.before_first_request
def organize_data():
    global posts_storage
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    data= response.json()

    for post in data:
        jsonable_post = JsonablePost(post)
        posts_storage[jsonable_post.id] = jsonable_post


@app.route('/')
def home_page():
    return 'HOME PAGE'


@app.route('/posts')
def get_all_posts():
    posts = []
    for item in posts_storage:
        posts.append(posts_storage[item].format_to_json())

    response = app.response_class(
        response=json.dumps(posts),
        status=200,
        mimetype='application/json')
    return response


@app.route('/posts/<post_id>')
def get_post(post_id):
    data_response = requests.get('https://jsonplaceholder.typicode.com/posts/' + post_id)
    json_response = data_response.json()
    response = app.response_class(
        response=json.dumps(json_response),
        status=200,
        mimetype='application/json')
    return response


@app.route('/posts-by-userId/<user_id>')
def get_user_posts(user_id):
    data_response = requests.get('https://jsonplaceholder.typicode.com/posts?userId=' + user_id)
    posts = data_response.json()

    response = app.response_class(
        response=json.dumps(posts),
        status=200,
        mimetype='application/json')
    return response


@app.route('/posts/<post_id>/comments')
def get_post_comments(post_id):
    data_response = requests.get('https://jsonplaceholder.typicode.com/posts/' + post_id + '/comments')
    comments = data_response.json()

    response = app.response_class(
        response=json.dumps(comments),
        status=200,
        mimetype='application/json')
    return response
