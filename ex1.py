from flask import Flask, json
import requests
from BasePost import BasePost
from ExtendedPost import ExtendedPost
from JsonablePost import JsonablePost

app = Flask(__name__)

@app.before_first_request
def organize_data():
    all_posts_response = requests.get('https://jsonplaceholder.typicode.com/posts')
    for post in all_posts_response:



@app.route('/')
def home_page():
    return 'HOME PAGE'


@app.route('/posts')
def get_all_posts():
    data_response = requests.get('https://jsonplaceholder.typicode.com/posts')
    posts = data_response.json()

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
