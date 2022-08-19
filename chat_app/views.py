from django.shortcuts import render, redirect
from django.contrib.auth.models import auth, User
from user_app.models import UserDetail
from .models import Room, Message


bot_name = 'Benion - Tech'


# Create your views here.
def chat_home(request):
    if str(auth.get_user(request)) == 'AnonymousUser':
        return redirect('/login')
    else:
        username = auth.get_user(request)
        users = User.objects.all()
        rooms = Room.objects.all()
        user = User.objects.get(username=username)
        user_details = UserDetail.objects.get(username=username)

        data = {
            'users': users,
            'username': user.username,
            'rooms': rooms,
            'role': user_details.role
        }
        return render(request, 'chat.html', data)


def chat_user(request, params):
    if str(auth.get_user(request)) == 'AnonymousUser':
        return redirect('/login')
    else:
        if User.objects.filter(username=params).exists():
            username = auth.get_user(request)
            user = User.objects.get(username=username)
            user_details = User.objects.get(username=params)
            bot = bot_name
            messages = Message.objects.filter(room='General', sender=username)
            data = {
                'sender': user,
                'reciever': user_details,
                'messages': messages,
                'bot': bot,
                'total_messages': len(messages)
            }
            return render(request, 'chat-user.html', data)
        else:
            return redirect('/chat')


def chat_room(request, params):
    if str(auth.get_user(request)) == 'AnonymousUser':
        return redirect('/login')
    else:
        username = auth.get_user(request)
        user = User.objects.get(username=username)
        users = User.objects.all()
        capitalize_room = params.title()
        bot = f'Benion - Tech ({ params })'
        messages = Message.objects.filter(room=capitalize_room)
        data = {
            'sender': user,
            'room': capitalize_room,
            'bot': bot,
            'username': user.username,
            'users': users,
            'messages': messages
        }

        if Room.objects.filter(name=capitalize_room).exists():
            return render(request, 'chat-room.html', data)
        else:
            return redirect('/chat')


def send_message(request):
    reciever = request.POST['reciever']
    if request.method == 'POST':
        message = request.POST['message']
        room = request.POST['room']
        sender = request.POST['sender']

        print("POST Data Recieved", {'message': message, 'room': room, 'sender': sender, 'reciever': reciever})

        # new_message = Message.objects.create(value=message, room=room, sender=sender, reciever=reciever)
        # new_message.save()
        return redirect(f'/chat/user/{ reciever }')
    else:
        return redirect(f'/chat/user/{reciever}')
        print("GET Data Recieved")



