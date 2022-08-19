from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from user_app.models import UserDetail, GalleryImage
from django.http import HttpResponse


def home(request):
    return render(request, 'coming-soon.html')


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
                user_details = UserDetail.objects.create(username=username, sex=sex)
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
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')


def resume(request):
    return render(request, 'resume.html')


def not_found(request, exception):
    return render(request, 'not-found.html')


def coming_soon(request):
    return render(request, 'coming-soon.html')


def portfolio(request):
    work_images = GalleryImage.objects.filter(category='Works')
    return render(request, 'portfolio.html', {'work_images': work_images})


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
