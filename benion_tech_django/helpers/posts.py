import json
import urllib.request

base_url = 'https://benion-tech-server.herokuapp.com'
data = []


def get_posts():
    response = urllib.request.urlopen(f'{base_url}/benion-users/api/all-posts').read()
    json_data = json.loads(response)
    all_posts = json_data['data'][3]
    return all_posts

