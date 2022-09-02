import json
import urllib.request
from benion_tech_django.settings import env
from practice_area.models import Post

base_url = 'https://benion-tech-server.herokuapp.com'
production = env('PRODUCTION') == 'True'


def get_posts():
    items = Post.objects.all()
    posts = []
    for item in items:
        posts.append(item)
    all_posts = posts
    if production:
        response = urllib.request.urlopen(f'{base_url}/benion-news/api/all-posts').read()
        json_data = json.loads(response)
        all_posts = json_data['data'][3]
    return all_posts


def filter_posts(posts, value):
    items = []
    for post in posts:
        if production:
            if post["category"] == value or post["tag"] == value:
                items.append(post)
        else:
            if post.category == value or post.tag == value:
                items.append(post)
    return items


def category_filter_posts(posts, value):
    items = []
    for post in posts:
        if production:
            if post["category"] == value:
                items.append(post)
        else:
            if post.category == value:
                items.append(post)
    return items


def get_post(value):
    posts = get_posts()
    item = {}
    for post in posts:
        if production:
            if post["title"] == value:
                item = post
        else:
            if post.title == value:
                item = post
    return item

