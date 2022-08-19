from django.contrib import admin
from .models import UserDetail, CbtUser, CbtExam, ExamScore, ContactMessage, GalleryImage


# Register your models here.
admin.site.register(UserDetail)
admin.site.register(CbtUser)
admin.site.register(CbtExam)
admin.site.register(ExamScore)
admin.site.register(ContactMessage)
admin.site.register(GalleryImage)