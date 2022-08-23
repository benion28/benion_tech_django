from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from user_app.models import UserDetail, CbtExam, GalleryImage, ContactMessage, ExamScore, CbtUser
from benion_tech_django.helpers.images import data as images_data
from benion_tech_django.helpers.messages import data as messages_data
from benion_tech_django.helpers.exams import data as exams_data
from benion_tech_django.helpers.scores import data as scores_data
from benion_tech_django.helpers.cbt_users import data as cbt_users_data
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
                users = User.objects.all()
                data = {
                    'demo_items': demo_items,
                    'total_demo_items': len(demo_items),
                    'total_images': len(images_data),
                    'total_scores': len(scores_data),
                    'total_messages': len(messages_data),
                    'total_cbt_users': len(cbt_users_data),
                    'total_exams': len(exams_data),
                    'total_users': len(users),
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


def cbt_users(request):
    if str(auth.get_user(request)) == 'AnonymousUser':
        return redirect('/login')
    else:
        username = auth.get_user(request)
        user_details = UserDetail.objects.get(username=username)
        if user_details.role == 'admin':
            users = cbt_users_data
            for user in users:
                current_user = CbtUser.objects.get(username=user['username'])
                if not CbtUser.objects.filter(username=user['username']).exists():
                    cbt_user = CbtUser.objects.create(
                        _id=user['_id'], firstname=user['firstname'], lastname=user['lastname'],
                        username=user['username'], className=user['className'], category=user['category'],
                        gender=user['gender'], accessCode=user['accessCode'], creator=user['creator'],
                        school=user['school'], role=user['role'], date=user['date'], regType=user['regType']
                    )
                    cbt_user.save()
                else:
                    cbt_user = CbtUser(
                        _id=user['_id'], firstname=user['firstname'], lastname=user['lastname'], id=current_user.id,
                        username=user['username'], className=user['className'], category=user['category'],
                        gender=user['gender'], accessCode=user['accessCode'], creator=user['creator'],
                        school=user['school'], role=user['role'], date=user['date'], regType=user['regType']
                    )
                    cbt_user.save(force_update=True)
            return redirect('/practice-area')
        else:
            return redirect('/user/dashboard')


def exams(request):
    if str(auth.get_user(request)) == 'AnonymousUser':
        return redirect('/login')
    else:
        username = auth.get_user(request)
        user_details = UserDetail.objects.get(username=username)
        if user_details.role == 'admin':
            all_exams = exams_data
            for exam in all_exams:
                current_cbt_user = CbtUser.objects.get(username=exam['username'])
                current_exam = CbtExam.objects.get(username=exam['username'])
                class_name = exam['className'] or ''
                if not CbtExam.objects.filter(username=exam['username']).exists():
                    print(f"Save Exam {all_exams.index(exam)}: {exam} # {class_name}")
                    an_exam = CbtExam.objects.create(
                        _id=exam['id'], firstname=current_cbt_user.firstname, lastname=current_cbt_user.lastname,
                        username=exam['username'], className=class_name, category=exam['category'],
                        subject=exam['subject'], score=exam['score'], term=exam['term'], key=exam['$key'],
                        answered=exam['answered'], answers=exam['answers']
                    )
                    an_exam.save()
                else:
                    print(f"Update Exam {all_exams.index(exam)}: {exam} # {class_name}")
                    an_exam = CbtExam(
                        _id=exam['id'], firstname=current_cbt_user.firstname, lastname=current_cbt_user.lastname,
                        username=exam['username'], className=class_name or '', category=exam['category'],
                        subject=exam['subject'], score=exam['score'], term=exam['term'], key=exam['$key'],
                        answered=exam['answered'], answers=exam['answers'], id=current_exam.id
                    )
                    an_exam.save(force_update=True)
            return redirect('/practice-area')
        else:
            return redirect('/user/dashboard')


def scores(request):
    if str(auth.get_user(request)) == 'AnonymousUser':
        return redirect('/login')
    else:
        username = auth.get_user(request)
        user_details = UserDetail.objects.get(username=username)
        if user_details.role == 'admin':
            all_scores = scores_data
            for score in all_scores:
                current_score = ExamScore.objects.get(username=score['username'])
                if not ExamScore.objects.filter(username=score['username']).exists():
                    print(f"Save Score {all_scores.index(score)}: {score}")
                    a_score = ExamScore.objects.create(
                        fullname=score['fullname'], username=score['username'], className=score['className'],
                        comment=score['comment'], subject=score['subject'], grade=score['grade'], term=score['term'],
                        key=score['$key'], session=score['session'], total=score['total'], exam=score['exam'],
                        examiner=score['examiner'], first_ca=score['firstCA'], second_ca=score['secondCA']
                    )
                    a_score.save()
                else:
                    print(f"Update Score {all_scores.index(score)}: {score}")
                    a_score = ExamScore(
                        fullname=score['fullname'], username=score['username'], className=score['className'],
                        comment=score['comment'], subject=score['subject'], grade=score['grade'], term=score['term'],
                        key=score['$key'], session=score['session'], total=score['total'], exam=score['exam'],
                        examiner=score['examiner'], first_ca=score['firstCA'], second_ca=score['secondCA'],
                        id=current_score.id
                    )
                    a_score.save(force_update=True)
            return redirect('/practice-area')
        else:
            return redirect('/user/dashboard')


def messages(request):
    if str(auth.get_user(request)) == 'AnonymousUser':
        return redirect('/login')
    else:
        username = auth.get_user(request)
        user_details = UserDetail.objects.get(username=username)
        if user_details.role == 'admin':
            all_messages = messages_data
            for message in all_messages:
                current_message = ContactMessage.objects.get(key=message['$key'])
                if not ContactMessage.objects.filter(key=message['$key']).exists():
                    a_message = ContactMessage.objects.create(
                        fullname=message['fullname'], message=message['message'], email=message['email'],
                        time=message['time'], date=message['date'], key=message['$key'],
                    )
                    a_message.save()
                else:
                    a_message = ContactMessage(
                        fullname=message['fullname'], message=message['message'], email=message['email'],
                        time=message['time'], date=message['date'], key=message['$key'], id=current_message.id
                    )
                    a_message.save(force_update=True)
            return redirect('/practice-area')
        else:
            return redirect('/user/dashboard')


def images(request):
    if str(auth.get_user(request)) == 'AnonymousUser':
        return redirect('/login')
    else:
        username = auth.get_user(request)
        user_details = UserDetail.objects.get(username=username)
        if user_details.role == 'admin':
            all_images = images_data
            for image in all_images:
                current_image = GalleryImage.objects.get(key=image['$key'])
                if not GalleryImage.objects.filter(key=image['$key']).exists():
                    an_image = GalleryImage.objects.create(
                        caption=image['caption'], category=image['category'], image=image['image'],
                        link=image['link'], tag=image['tag'], key=image['$key'],
                    )
                    an_image.save()
                else:
                    an_image = GalleryImage(
                        caption=image['caption'], category=image['category'], image=image['image'],
                        link=image['link'], tag=image['tag'], key=image['$key'], id=current_image.id
                    )
                    an_image.save(force_update=True)
            return redirect('/practice-area')
        else:
            return redirect('/user/dashboard')

