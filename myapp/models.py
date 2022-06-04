import datetime

from django.db import models
from django.utils import timezone

from taggit.managers import TaggableManager
# Create your models here.

STATUS_CHOICES = [
    ('新規', '新規'),
    ('確認中', '確認中'),
    ('完了', '完了'),
]

CATEGORY_CHOICES = [
    ('業務', '業務'),
    ('規則', '規則'),
    ('その他', 'その他'),
]

DETAIL_CHOICES = [
    ('全社', '全社'),
    ('営業', '営業'),
    ('仕入', '仕入'),
    ('経理', '経理'),
    ('物流', '物流'),
    ('ICT', 'ICT'),
    ('社内', '社内'),
    ('社外', '社外'),
]

class Question(models.Model):
    status = models.CharField(max_length=50, choices=STATUS_CHOICES,blank=True)
    category_system = models.CharField(max_length=50, choices=CATEGORY_CHOICES, blank=True)
    category_detail = models.CharField(max_length=50, choices=DETAIL_CHOICES,blank=True)
    questioner = models.CharField(max_length=100)

    question_title = models.CharField(max_length=200)
    question_contents = models.TextField(max_length=1000)
    answer = models.TextField(max_length=1000)
    update = models.DateTimeField(default=timezone.now)
    
    tags = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.status} {self.category_system} {self.category_detail} {self.question_title}"

    def split_tag(self, li):
        return li.split(",")


class Category(models.Model):
    
    category = models.CharField(max_length=50,blank=True)

    def __str__(self):
        return f"{self.category}"