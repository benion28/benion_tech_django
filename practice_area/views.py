from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from user_app.models import UserDetail
from practice_area.models import DemoItem
from django.http import HttpResponse


# Create your views here.
def practice_area(request):
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
                message = request.POST['message']

                demo_item = DemoItem.objects.create(
                    firstname=firstname, lastname=lastname, username=username,
                    email=email, message=message
                )
                demo_item.save()
                messages.info(request, 'Message Recieved Successfully!!')
                return redirect('/practice-area')
            else:
                demo_items = DemoItem.objects.all()
                data = {
                    'demo_items': demo_items,
                    'total_demo_items': len(demo_items),
                    'data': {}
                }
                return render(request, 'practice-area.html', data)
        else:
            return redirect('/')


def edit_item(request, params):
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
                message = request.POST['message']

                if DemoItem.objects.filter(id=params).exists():
                    target_item = DemoItem(
                        firstname=firstname, lastname=lastname, username=username,
                        id=params, email=email, message=message
                    )
                    target_item.save(force_update=True)
                    messages.info(request, 'Item updated Successfully!!')
                    return redirect('/practice-area')
                else:
                    messages.info(request, 'Selected item not found!!')
                    return redirect('/practice-area')
            else:
                target_item = DemoItem.objects.get(id=params)
                demo_items = DemoItem.objects.all()
                data = {
                    'demo_items': demo_items,
                    'total_demo_items': len(demo_items),
                    'data': target_item
                }
                return render(request, 'practice-area.html', data)
        else:
            return redirect('/')


def delete_item(request, params):
    if str(auth.get_user(request)) == 'AnonymousUser':
        messages.info(request, 'Please login to view the page!!')
        return redirect('/login')
    else:
        username = auth.get_user(request)
        user_details = UserDetail.objects.get(username=username)
        if user_details.role == 'admin':
            if DemoItem.objects.filter(id=params).exists():
                target_item = DemoItem.objects.get(id=params)
                target_item.delete()
                messages.info(request, 'Item deleted Successfully!!')
                return redirect('/practice-area')
            else:
                messages.info(request, 'Selected item not found!!')
                return redirect('/practice-area')
        else:
            return redirect('/')


def delete_all_item(request):
    if str(auth.get_user(request)) == 'AnonymousUser':
        messages.info(request, 'Please login to view the page!!')
        return redirect('/login')
    else:
        username = auth.get_user(request)
        user_details = UserDetail.objects.get(username=username)
        if user_details.role == 'admin':
            items = DemoItem.objects.all()
            items.delete()
            return redirect('/practice-area')
        else:
            return redirect('/')

