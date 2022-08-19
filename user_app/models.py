from django.db import models


# Create your models here.
class UserDetail(models.Model):
    username = models.CharField(max_length=20)
    profile = models.CharField(default='null', max_length=40)
    role = models.CharField(default='guest', max_length=15)
    sex = models.CharField(default='male', max_length=10)
    password = models.CharField(default='', max_length=20)
    job = models.CharField(default='', max_length=20)
    amount = models.IntegerField(default=0)
    company = models.CharField(default='', max_length=50)
    country = models.CharField(default='', max_length=20)
    address = models.CharField(default='', max_length=50)
    phone = models.CharField(default='', max_length=20)
    twitter = models.CharField(default='#', max_length=40)
    facebook = models.CharField(default='#', max_length=40)
    instagram = models.CharField(default='#', max_length=40)
    linkedin = models.CharField(default='#', max_length=40)
    about = models.TextField(max_length=500)


class CbtUser(models.Model):
    _id = models.CharField(max_length=30)
    firstname = models.CharField(max_length=10)
    lastname = models.CharField(max_length=20)
    username = models.CharField(max_length=10)
    className = models.CharField(max_length=10)
    category = models.CharField(max_length=10)
    gender = models.CharField(max_length=10)
    accessCode = models.IntegerField()
    creator = models.IntegerField()
    school = models.CharField(max_length=10)
    role = models.CharField(max_length=15)
    date = models.CharField(max_length=30)
    regType = models.CharField(max_length=10)


class CbtExam(models.Model):
    _id = models.CharField(max_length=30)
    firstname = models.CharField(max_length=10)
    lastname = models.CharField(max_length=10)
    username = models.CharField(max_length=20)
    className = models.CharField(max_length=10)
    category = models.CharField(max_length=10)
    score = models.IntegerField()
    subject = models.CharField(max_length=15)
    term = models.CharField(max_length=15)
    key = models.CharField(max_length=30)
    answered = models.CharField(max_length=500)
    answers = models.CharField(max_length=200)


class ExamScore(models.Model):
    fullname = models.CharField(max_length=30)
    username = models.CharField(max_length=20)
    comment = models.CharField(max_length=15)
    grade = models.CharField(max_length=2)
    total = models.IntegerField()
    exam = models.IntegerField()
    examiner = models.IntegerField()
    first_ca = models.IntegerField()
    second_ca = models.IntegerField()
    subject = models.CharField(max_length=15)
    term = models.CharField(max_length=15)
    key = models.CharField(max_length=30)
    session = models.CharField(max_length=500)
    className = models.CharField(max_length=10)


class ContactMessage(models.Model):
    fullname = models.CharField(max_length=30)
    message = models.CharField(max_length=300)
    email = models.CharField(max_length=50)
    time = models.CharField(max_length=20)
    date = models.CharField(max_length=20)
    key = models.CharField(max_length=30)


class GalleryImage(models.Model):
    caption = models.CharField(max_length=50)
    category = models.CharField(max_length=10)
    image = models.CharField(max_length=200)
    link = models.CharField(max_length=100)
    tag = models.CharField(max_length=20)
    key = models.CharField(max_length=30)



