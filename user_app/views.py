from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from .models import UserDetail, CbtUser, CbtExam, ExamScore, ContactMessage, GalleryImage
import json
import urllib.request


base_url = 'https://benion-tech-server.herokuapp.com'
message = ''
error = ''
user_data = False


# Create your views here.
def user_dashboard(request):
    if str(auth.get_user(request)) == 'AnonymousUser':
        return redirect('/login')
    else:
        username = auth.get_user(request)
        user_details = UserDetail.objects.get(username=username)
        total_cbt_users = CbtUser.objects.all()
        total_users = User.objects.all()
        total_exams = CbtExam.objects.all()
        total_scores = ExamScore.objects.all()
        total_contact_messages = ContactMessage.objects.all()
        total_images = GalleryImage.objects.all()
        data = {
            'user_details': user_details,
            'total_cbt_users': len(total_cbt_users),
            'total_users': len(total_users),
            'total_exams': len(total_exams),
            'total_scores': len(total_scores),
            'total_contact_messages': len(total_contact_messages),
            'total_images': len(total_images)
        }
        return render(request, 'user-dashboard.html', data)


def user_profile(request):
    if str(auth.get_user(request)) == 'AnonymousUser':
        return redirect('/login')
    else:
        username = auth.get_user(request)
        user_details = UserDetail.objects.get(username=username)
        if request.method == 'POST':
            params = request.POST['id']
            sex = request.POST['sex']
            job = request.POST['job']
            company = request.POST['company']
            country = request.POST['country']
            address = request.POST['address']
            phone = request.POST['phone']
            twitter = request.POST['twitter']
            facebook = request.POST['facebook']
            instagram = request.POST['instagram']
            linkedin = request.POST['linkedin']
            email = request.POST['email']
            about = request.POST['about']
            role = request.POST['role']
            amount = request.POST['amount']
            target_username = request.POST['username']
            target_params = request.POST['params']
            firstname = request.POST['firstname']
            lastname = request.POST['lastname']
            password = request.POST['password']
            target_password = make_password(password)
            if UserDetail.objects.filter(username=username).exists():
                target_item = UserDetail(
                    id=params, sex=sex, job=job, company=company, country=country, address=address,
                    phone=phone, twitter=twitter, facebook=facebook, instagram=instagram, linkedin=linkedin,
                    about=about, role=role, amount=amount, username=target_username, password=password
                )
                target_user = User(
                    id=target_params, password=target_password, username=target_username,
                    first_name=firstname, last_name=lastname, email=email
                )
                target_user.save(force_update=True)
                target_item.save(force_update=True)
                message = 'Details saved successfully'
                return render(request, 'user-profile.html', {'user_details': user_details, 'success': True, 'message': message})
            else:
                error = 'Target user not found'
                return render(request, 'user-profile.html', {'user_details': user_details, 'success': False, 'error': error})
        else:
            return render(request, 'user-profile.html', {'user_details': user_details})


def user_setting(request):
    if str(auth.get_user(request)) == 'AnonymousUser':
        return redirect('/login')
    else:
        username = auth.get_user(request)
        user_details = UserDetail.objects.get(username=username)
        if request.method == 'POST':
            password1 = request.POST['password1']
            password = request.POST['password']
            password2 = request.POST['password2']
            user = User.objects.get(username=username)
            if user.check_password(password1):
                if password == password2:
                    user.set_password(password)
                    message = 'Password updated successfully'
                    return render(request, 'user-setting.html', {'user_details': user_details, 'success': True, 'message': message})
                else:
                    error = 'Passwords do not match'
                    return render(request, 'user-setting.html', {'user_details': user_details, 'success': False, 'error': error})
            else:
                error = 'Incorrect password'
                return render(request, 'user-setting.html', {'user_details': user_details, 'success': False, 'error': error})
        else:
            return render(request, 'user-setting.html', {'user_details': user_details})


def users_table(request):
    if str(auth.get_user(request)) == 'AnonymousUser':
        return redirect('/login')
    else:
        users = User.objects.all()
        details = UserDetail.objects.all()
        username = auth.get_user(request)
        user_details = UserDetail.objects.get(username=username)
        if user_details.role == 'admin':
            if user_data:
                message = 'User deleted successfully'
                return render(request, 'users-table.html', {
                    'users': users,
                    'total_users': len(users),
                    'user_details': user_details,
                    'total_user_details': len(details),
                    'details': details,
                    'success': True,
                    'message': message
                })
            else:
                error = 'Delete user failed'
                return render(request, 'users-table.html', {
                    'users': users,
                    'total_users': len(users),
                    'user_details': user_details,
                    'total_user_details': len(details),
                    'details': details,
                    'success': False,
                    'error': error
                })
        else:
            return redirect('/user/dashboard')


def cbt_users_table(request):
    if str(auth.get_user(request)) == 'AnonymousUser':
        return redirect('/login')
    else:
        username = auth.get_user(request)
        all_cbt_users = CbtUser.objects.all()
        user_details = UserDetail.objects.get(username=username)
        if user_details.role == 'admin':
            data = {
                'user_details': user_details,
                'cbt_users': all_cbt_users,
                'total_cbt_users': len(all_cbt_users)
            }
            return render(request, 'cbt-users-table.html', data)
        else:
            return redirect('/user/dashboard')


def exams_table(request):
    if str(auth.get_user(request)) == 'AnonymousUser':
        return redirect('/login')
    else:
        all_exams = CbtExam.objects.all()
        username = auth.get_user(request)
        user_details = UserDetail.objects.get(username=username)
        if user_details.role == 'admin':
            data = {
                'user_details': user_details,
                'all_exams': all_exams,
                'total_exams': len(all_exams)
            }
            return render(request, 'exams-table.html', data)
        else:
            return redirect('/user/dashboard')


def scores_table(request):
    if str(auth.get_user(request)) == 'AnonymousUser':
        return redirect('/login')
    else:
        all_scores = ExamScore.objects.all()
        username = auth.get_user(request)
        user_details = UserDetail.objects.get(username=username)
        if user_details.role == 'admin':
            data = {
                'user_details': user_details,
                'all_scores': all_scores,
                'total_scores': len(all_scores)
            }
            return render(request, 'scores-table.html', data)
        else:
            return redirect('/user/dashboard')


def messages_table(request):
    if str(auth.get_user(request)) == 'AnonymousUser':
        return redirect('/login')
    else:
        all_messages = ContactMessage.objects.all()
        username = auth.get_user(request)
        user_details = UserDetail.objects.get(username=username)
        if user_details.role == 'admin':
            data = {
                'user_details': user_details,
                'all_messages': all_messages,
                'total_messages': len(all_messages)
            }
            return render(request, 'messages-table.html', data)
        else:
            return redirect('/user/dashboard')


def remove_profile(request, id):
    if str(auth.get_user(request)) == 'AnonymousUser':
        return redirect('/login')
    else:
        username = auth.get_user(request)
        user_details = UserDetail.objects.get(username=username)
        if user_details.role == 'admin':
            if UserDetail.objects.filter(id=id).exists():
                # update photo
                message = 'Photo updated successfully'
                return render(request, 'user-profile.html', {'user_details': user_details, 'success': True, 'message': message})
            else:
                error = 'Target user not found'
                return render(request, 'user-profile.html', {'user_details': user_details, 'success': False, 'message': error})
        else:
            return redirect('/user/dashboard')


def delete_user(request, user):
    if str(auth.get_user(request)) == 'AnonymousUser':
        return redirect('/login')
    else:
        username = auth.get_user(request)
        user_details = UserDetail.objects.get(username=username)
        if user_details.role == 'admin':
            if User.objects.filter(username=user).exists():
                target_user = User.objects.get(username=user)
                target_user.delete()
                target_details = UserDetail.objects.get(username=user)
                target_details.delete()
                user_data = True
                return redirect('/users/users-table')
            else:
                user_data = False
                return redirect('/users/users-table')
        else:
            return redirect('/user/dashboard')


def edit_user(request, params):
    if str(auth.get_user(request)) == 'AnonymousUser':
        return redirect('/login')
    else:
        username = auth.get_user(request)
        user = User.objects.get(username=params)
        user_details = UserDetail.objects.get(username=username)
        params_details = UserDetail.objects.get(username=params)
        if user_details.role == 'admin':
            if request.method == 'POST':
                params_id = request.POST['id']
                sex = request.POST['sex']
                job = request.POST['job']
                company = request.POST['company']
                country = request.POST['country']
                address = request.POST['address']
                phone = request.POST['phone']
                twitter = request.POST['twitter']
                facebook = request.POST['facebook']
                instagram = request.POST['instagram']
                linkedin = request.POST['linkedin']
                email = request.POST['email']
                about = request.POST['about']
                role = request.POST['role']
                amount = request.POST['amount']
                target_params = request.POST['params']
                firstname = request.POST['firstname']
                lastname = request.POST['lastname']
                password = request.POST['password']
                target_password = make_password(password)
                if UserDetail.objects.filter(username=params).exists():
                    target_item = UserDetail(
                        id=params_id, sex=sex, job=job, company=company, country=country, address=address,
                        phone=phone, twitter=twitter, facebook=facebook, instagram=instagram, linkedin=linkedin,
                        about=about, role=role, amount=amount, username=user.username, password=password
                    )
                    target_user = User(
                        id=target_params, password=target_password, username=params,
                        first_name=firstname, last_name=lastname, email=email
                    )
                    target_user.save(force_update=True)
                    target_item.save(force_update=True)
                    message = f'User {params} updated successfully'
                    return render(request, 'edit-user.html', {
                        'user_details': user_details,
                        'params_details': params_details,
                        'params': user,
                        'message': message,
                        'success': True
                    })
                else:
                    error = 'Target user not found'
                    return render(request, 'edit-user.html', {
                        'user_details': user_details,
                        'params_details': params_details,
                        'params': user,
                        'error': error,
                        'success': False
                    })
            else:
                data = {
                    'user_details': user_details,
                    'params_details': params_details,
                    'params': user
                }
                return render(request, 'edit-user.html', data)
        else:
            return redirect('/user/dashboard')


def cbt_users(request):
    if str(auth.get_user(request)) == 'AnonymousUser':
        return redirect('/login')
    else:
        username = auth.get_user(request)
        user_details = UserDetail.objects.get(username=username)
        if user_details.role == 'admin':
            response = urllib.request.urlopen(f'{base_url}/benion-cbt/api/users').read()
            json_data = json.loads(response)
            users = json_data['data']['allCbtUsers']
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
            return redirect('/user/dashboard')
        else:
            return redirect('/user/dashboard')


def exams(request):
    if str(auth.get_user(request)) == 'AnonymousUser':
        return redirect('/login')
    else:
        username = auth.get_user(request)
        user_details = UserDetail.objects.get(username=username)
        if user_details.role == 'admin':
            response = urllib.request.urlopen(f'{base_url}/benion-cbt/api/cbt-exam-data').read()
            json_data = json.loads(response)
            all_exams = json_data['data'][3]
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
            return redirect('/user/dashboard')
        else:
            return redirect('/user/dashboard')


def scores(request):
    if str(auth.get_user(request)) == 'AnonymousUser':
        return redirect('/login')
    else:
        username = auth.get_user(request)
        user_details = UserDetail.objects.get(username=username)
        if user_details.role == 'admin':
            response = urllib.request.urlopen(f'{base_url}/benion-cbt/api/cbt-scores').read()
            json_data = json.loads(response)
            all_scores = json_data['data'][3]
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
            return redirect('/user/dashboard')
        else:
            return redirect('/user/dashboard')


def messages(request):
    if str(auth.get_user(request)) == 'AnonymousUser':
        return redirect('/login')
    else:
        username = auth.get_user(request)
        user_details = UserDetail.objects.get(username=username)
        if user_details.role == 'admin':
            response = urllib.request.urlopen(f'{base_url}/benion-users/api/contact-messages').read()
            json_data = json.loads(response)
            all_messages = json_data['data'][3]
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
            return redirect('/user/dashboard')
        else:
            return redirect('/user/dashboard')


def images(request):
    if str(auth.get_user(request)) == 'AnonymousUser':
        return redirect('/login')
    else:
        username = auth.get_user(request)
        user_details = UserDetail.objects.get(username=username)
        if user_details.role == 'admin':
            response = urllib.request.urlopen(f'{base_url}/benion-users/api/all-images').read()
            json_data = json.loads(response)
            all_images = json_data['data'][3]
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
            return redirect('/user/dashboard')
        else:
            return redirect('/user/dashboard')


def change_password(request, params):
    if str(auth.get_user(request)) == 'AnonymousUser':
        return redirect('/login')
    else:
        user_details = UserDetail.objects.get(username=params)
        username = auth.get_user(request)
        target_details = UserDetail.objects.get(username=username)
        if request.method == 'POST':
            password1 = request.POST['password1']
            password = request.POST['password']
            password2 = request.POST['password2']
            target_password = make_password(password)
            user = User.objects.get(username=params)
            if user.check_password(password1):
                if password == password2:
                    target_user = User(
                        id=user.id, password=target_password, username=params,
                        first_name=user.first_name, last_name=user.last_name, email=user.email
                    )
                    target_item = UserDetail(
                        id=user_details.id, sex=user_details.sex, job=user_details.job, company=user_details.company,
                        country=user_details.country, address=user_details.address, phone=user_details.phone,
                        twitter=user_details.twitter, facebook=user_details.facebook, instagram=user_details.instagram,
                        linkedin=user_details.linkedin, about=user_details.about, role=user_details.role,
                        amount=user_details.amount, username=user_details.username, password=password
                    )
                    target_user.save(force_update=True)
                    target_item.save(force_update=True)
                    if target_details.role == 'admin' and target_details.id != user_details.id:
                        return redirect(f'/users/edit-user/{params}')
                    else:
                        return redirect('/user/setting')
                else:
                    if target_details.role == 'admin' and target_details.id != user_details.id:
                        return redirect(f'/users/edit-user/{params}')
                    else:
                        return redirect('/user/setting')
            else:
                if target_details.role == 'admin' and target_details.id != user_details.id:
                    return redirect(f'/users/edit-user/{params}')
                else:
                    return redirect('/user/setting')
        else:
            if target_details.role == 'admin' and target_details.id != user_details.id:
                return redirect(f'/users/edit-user/{params}')
            else:
                return redirect('/user/setting')

