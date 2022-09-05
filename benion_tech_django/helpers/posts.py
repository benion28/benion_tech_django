import json
import urllib.request
from benion_tech_django.settings import env
from practice_area.models import Post

base_url = env('BASE_URL')
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


def filter_posts_category(posts, value):
    items = []
    for post in posts:
        if production:
            if post["category"] == value or post["tag"] == value:
                items.append(post)
        else:
            if post.category == value or post.tag == value:
                items.append(post)
    return items


def filter_posts_tag(posts, value):
    items = []
    for post in posts:
        if production:
            if post["title"].lower().__contains__(value) or post["content"].lower().__contains__(value):
                items.append(post)
        else:
            if post.title.lower().__contains__(value) or post.content.lower().__contains__(value):
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


def limit_post(posts, total):
    items = []
    if len(posts) > total:
        for index in range(total):
            items.append(posts[index])
    else:
        items = posts
    return items
