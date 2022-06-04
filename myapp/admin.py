from django.contrib import admin

# Register your models here.
from .models import Question,Category

admin.site.register(Question)
admin.site.register(Category)