from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
import json
from django.contrib import messages
from user_app.models import UserDetail
from benion_tech_django.settings import env
from benion_tech_django.helpers.images import category_images, single_image
from benion_tech_django.helpers.posts import get_posts, category_filter_posts, filter_posts, get_post
from django.http import HttpResponse
import urllib.request

base_url = 'https://benion-tech-server.herokuapp.com'
headers = {'Content-Type': 'application/json'}
message = ''
error = ''
categories = [
    {'name': 'Entertainment', 'value': 'entertainment'}, {'name': 'Business', 'value': 'business'},
    {'name': 'Culture', 'value': 'culture'}, {'name': 'Sport', 'value': 'sport'},
    {'name': 'Food', 'value': 'food'}, {'name': 'Politics', 'value': 'politics'},
    {'name': 'Technology', 'value': 'technology'}, {'name': 'Celebrity', 'value': 'celebrity'},
    {'name': 'Travel', 'value': 'travel'}, {'name': 'Wildlife', 'value': 'wildlife'},
    {'name': 'Programming', 'value': 'programming'}, {'name': 'Lifestyle', 'value': 'lifestyle'},
]
production = env('PRODUCTION') == 'True'


def home(request):
    posts = get_posts()
    blog_posts = category_filter_posts(posts, "blog")
    news_posts = category_filter_posts(posts, "news")
    others_posts = category_filter_posts(posts, "others")
    sports_posts = filter_posts(posts, "sport")
    politics_posts = filter_posts(posts, "politics")
    technology_posts = filter_posts(posts, "technology")
    any_other_post = filter_posts(posts, "others")
    other_posts = []
    blog = []
    news = []
    others = []
    sports = []
    politics = []
    technology = []
    any_other = []
    for index in range(5):
        if len(posts) > 5:
            other_posts.append(posts[index])
        else:
            other_posts = posts
        if len(blog_posts) > 5:
            blog.append(blog_posts[index])
        else:
            blog = blog_posts
        if len(others_posts) > 5:
            others.append(others_posts[index])
        else:
            others = others_posts
        if len(news_posts) > 5:
            news.append(news_posts[index])
        else:
            news = news_posts
    for index in range(3):
        if len(sports_posts) > 3:
            sports.append(sports_posts[index])
        else:
            sports = sports_posts
        if len(politics_posts) > 3:
            politics.append(politics_posts[index])
        else:
            politics = politics_posts
        if len(technology_posts) > 3:
            technology.append(technology_posts[index])
        else:
            technology = technology_posts
        if len(any_other_post) > 3:
            any_other.append(any_other_post[index])
        else:
            any_other = any_other_post
    data = {
        'other_posts': other_posts,
        'categories': categories, 'politics': politics,
        'others': others, 'any_other': any_other,
        'blog': blog, 'technology': technology,
        'news': news, 'sports': sports
    }
    return render(request, 'home.html', data)


def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        sex = request.POST['sex']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already Registered!!')
                return redirect('/register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Already Registered!!')
                return redirect('/register')
            elif len(username) > 10:
                messages.info(request, 'Username should not be more than 10 characters!!')
                return redirect('/register')
            else:
                user = User.objects.create_user(first_name=firstname, last_name=lastname, username=username, email=email, password=password)
                user.save()
                user_details = UserDetail.objects.create(username=username, sex=sex, password=password)
                user_details.save()
                messages.info(request, 'You are now registered, login now!!')
                return redirect('/login')
        else:
            messages.info(request, 'Passwords do not match!!')
            return redirect('/register')
    else:
        if str(auth.get_user(request)) == 'AnonymousUser':
            return render(request, 'register.html')
        else:
            return redirect('/user/dashboard')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/user/dashboard')
        else:
            messages.info(request, 'Incorrect login credentials!!')
            return redirect('/login')
    else:
        if str(auth.get_user(request)) == 'AnonymousUser':
            return render(request, 'login.html')
        else:
            return redirect('/user/dashboard')


def logout(request):
    auth.logout(request)
    return redirect('/')


def contact(request):
    if request.method == 'POST':
        dict_data = {
            'name': request.POST['name'],
            'email': request.POST['email'],
            'subject': request.POST['subject'],
            'message': request.POST['message']
        }
        json_data = json.dumps(dict_data)
        post_data = json_data.encode("utf-8")
        # response = urllib.request.urlopen(
        #     f'{base_url}/benion-cbt/api/cbt-scores', data=post_data, headers=headers
        # ).read()
        response = False
        if response:
            error = 'Sorry an error occurred!'
            return render(request, 'contact.html', {'success': False, 'error': error})
        else:
            message = 'Your message has been sent. Thank you!'
            return render(request, 'contact.html', {'success': True, 'message': message})
    else:
        return render(request, 'contact.html', {})


def about(request):
    return render(request, 'about.html')


def need_help(request):
    return render(request, 'coming-soon.html', {})


def resume(request):
    return render(request, 'resume.html')


def all_posts(request):
    posts = get_posts()
    blog_posts = category_filter_posts(posts, "blog")
    news_posts = category_filter_posts(posts, "news")
    others_posts = category_filter_posts(posts, "others")
    other_posts = []
    blog = []
    news = []
    others = []
    for index in range(5):
        if len(posts) > 5:
            other_posts.append(posts[index])
        else:
            other_posts = posts
        if len(blog_posts) > 5:
            blog.append(blog_posts[index])
        else:
            blog = blog_posts
        if len(others_posts) > 5:
            others.append(others_posts[index])
        else:
            others = others_posts
        if len(news_posts) > 5:
            news.append(news_posts[index])
        else:
            news = news_posts
    data = {
        'posts': posts,
        'other_posts': other_posts,
        'categories': categories,
        'others': others,
        'blog': blog,
        'news': news,
        'total': len(posts)
    }
    return render(request, 'all-posts.html', data)


def category_posts(request, params):
    posts = get_posts()
    blog_posts = category_filter_posts(posts, "blog")
    news_posts = category_filter_posts(posts, "news")
    others_posts = category_filter_posts(posts, "others")
    other_posts = []
    blog = []
    news = []
    others = []
    for index in range(5):
        if len(posts) > 5:
            other_posts.append(posts[index])
        else:
            other_posts = posts
        if len(blog_posts) > 5:
            blog.append(blog_posts[index])
        else:
            blog = blog_posts
        if len(others_posts) > 5:
            others.append(others_posts[index])
        else:
            others = others_posts
        if len(news_posts) > 5:
            news.append(news_posts[index])
        else:
            news = news_posts
    items = []
    for post in posts:
        if production:
            if post["category"] == params or post["tag"] == params:
                items.append(post)
        else:
            if post.category == params or post.tag == params:
                items.append(post)
    data = {
        'posts': items,
        'other_posts': other_posts,
        'categories': categories,
        'others': others,
        'blog': blog,
        'news': news,
        'total': len(items)
    }
    if len(items) > 0:
        return render(request, 'all-posts.html', data)
    else:
        return redirect('/')


def tag_posts(request, params):
    posts = get_posts()
    blog_posts = category_filter_posts(posts, "blog")
    news_posts = category_filter_posts(posts, "news")
    others_posts = category_filter_posts(posts, "others")
    other_posts = []
    blog = []
    news = []
    others = []
    for index in range(5):
        if len(posts) > 5:
            other_posts.append(posts[index])
        else:
            other_posts = posts
        if len(blog_posts) > 5:
            blog.append(blog_posts[index])
        else:
            blog = blog_posts
        if len(others_posts) > 5:
            others.append(others_posts[index])
        else:
            others = others_posts
        if len(news_posts) > 5:
            news.append(news_posts[index])
        else:
            news = news_posts
    items = []
    string = params.lower()
    for post in posts:
        if production:
            if post["title"].lower().__contains__(string) or post["content"].lower().__contains__(string):
                items.append(post)
        else:
                if post.title.lower().__contains__(string) or post.content.lower().__contains__(string):
                    items.append(post)
    data = {
        'posts': items,
        'other_posts': other_posts,
        'categories': categories,
        'others': others,
        'blog': blog,
        'news': news,
        'total': len(items)
    }
    if len(items) > 0:
        return render(request, 'all-posts.html', data)
    else:
        return redirect('/')


def single_post(request, params):
    posts = get_posts()
    post = get_post(params)
    blog_posts = category_filter_posts(posts, "blog")
    news_posts = category_filter_posts(posts, "news")
    others_posts = category_filter_posts(posts, "others")
    other_posts = []
    blog = []
    news = []
    others = []
    for index in range(5):
        if len(posts) > 5:
            other_posts.append(posts[index])
        else:
            other_posts = posts
        if len(blog_posts) > 5:
            blog.append(blog_posts[index])
        else:
            blog = blog_posts
        if len(others_posts) > 5:
            others.append(others_posts[index])
        else:
            others = others_posts
        if len(news_posts) > 5:
            news.append(news_posts[index])
        else:
            news = news_posts
    data = {
        'post': post,
        'other_posts': other_posts,
        'categories': categories,
        'others': others,
        'blog': blog,
        'news': news
    }
    return render(request, 'single-post.html', data)


def tag_search(request):
    if request.method == 'POST':
        keyword = request.POST['keyword']
        return redirect(f'/posts/tag/{keyword }')
    else:
        return redirect('/')


def not_found(request, exception):
    return render(request, 'not-found.html', {'error': exception})


def server_error(request):
    return render(request, 'server-error.html')


def coming_soon(request):
    if request.method == 'POST':
        dict_data = {
            'name': request.POST['name'],
            'email': request.POST['email'],
            'subject': request.POST['subject'],
            'message': request.POST['message']
        }
        json_data = json.dumps(dict_data)
        post_data = json_data.encode("utf-8")
        # response = urllib.request.urlopen(
        #     f'{base_url}/benion-cbt/api/cbt-scores', data=post_data, headers=headers
        # ).read()
        response = False
        if response:
            error = 'Sorry an error occurred!'
            return render(request, 'coming-soon.html', {'success': False, 'message': error})
        else:
            message = 'Your message has been sent. Thank you!'
            return render(request, 'coming-soon.html', {'success': True, 'message': message})
    else:
        return render(request, 'coming-soon.html', {})


def portfolio(request):
    role = 'guest'
    if request.user.is_authenticated:
        username = auth.get_user(request)
        user_details = UserDetail.objects.get(username=username)
        role = user_details.role
    work_images = category_images('Works')
    return render(request, 'portfolio.html', {'work_images': work_images, 'role': role})


def portfolio_details(request, params):
    image = single_image(params)
    work_images = category_images('Works')
    return render(request, 'portfolio-details.html', {'image': image, 'work_images': work_images})


def add_user(request):
    if str(auth.get_user(request)) == 'AnonymousUser':
        messages.info(request, 'Please login to view the page!!')
        return redirect('/login')
    else:
        username = auth.get_user(request)
        user_details = UserDetail.objects.get(username=username)
        if user_details.role == 'admin':
            if request.method == 'POST':
                firstname = request.POST['firstname']
                lastname = request.POST['lastname']
                username = request.POST['username']
                email = request.POST['email']
                password = request.POST['password']
                password2 = request.POST['password2']
                sex = request.POST['sex']
                role = request.POST['role']

                if password == password2:
                    if User.objects.filter(email=email).exists():
                        messages.info(request, 'Email Already Registered!!')
                        return redirect('/register')
                    elif User.objects.filter(username=username).exists():
                        messages.info(request, 'Username Already Registered!!')
                        return redirect('/register')
                    elif len(username) > 10:
                        messages.info(request, 'Username should not be more than 10 characters!!')
                        return redirect('/register')
                    else:
                        if role == 'admin':
                            user = User.objects.create_superuser(
                                first_name=firstname, last_name=lastname, username=username,
                                email=email, password=password
                            )
                        else:
                            user = User.objects.create_user(
                                first_name=firstname, last_name=lastname, username=username,
                                email=email, password=password
                            )
                        user.save()
                        user_details = UserDetail.objects.create(
                            username=username, sex=sex, role=role, password=password
                        )
                        user_details.save()
                        messages.info(request, 'You are now registered, login now!!')
                        return redirect('/login')
                else:
                    messages.info(request, 'Passwords do not match!!')
                    return redirect('/register')
            else:
                return render(request, 'add-user.html')
        else:
            return redirect('/user/dashboard')

