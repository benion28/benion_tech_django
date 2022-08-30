from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
import json
from django.contrib import messages
from user_app.models import UserDetail, GalleryImage
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


def home(request):
    data = {
        'categories': categories
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
    data = {
        'categories': categories
    }
    return render(request, 'all-posts.html', data)


def category_posts(request, params):
    data = {
        'categories': categories
    }
    return render(request, 'all-posts.html', data)


def tag_posts(request, params):
    data = {
        'categories': categories
    }
    return render(request, 'all-posts.html', data)


def single_post(request, params):
    data = {
        'categories': categories
    }
    return render(request, 'single-post.html', data)


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
    work_images = GalleryImage.objects.filter(category='Works')
    return render(request, 'portfolio.html', {'work_images': work_images, 'role': role})


def portfolio_details(request, params):
    image = GalleryImage.objects.get(id=params)
    work_images = GalleryImage.objects.filter(category='Works')
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

