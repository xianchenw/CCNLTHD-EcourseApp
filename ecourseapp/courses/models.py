from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

class MyUser(User):
    avatar = models.ImageField(upload_to='upload/')

class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Course(BaseModel):
    subject = models.CharField(max_length=255)
    description = RichTextField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    image = models.ImageField(upload_to='courses/%Y/%m', null=True)

    def __str__(self):
        return self.subject
    
class Lesson(BaseModel):
    subject = models.CharField(max_length=255)
    content = RichTextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='courses/%Y/%m', null=True)
    tags = models.ManyToManyField('Tag', blank=True, related_name='lessons')
    
    def __str__(self):
        return self.subject
    
class Tag(BaseModel):
    name = models.CharField(max_length=100, unique=True)
    
    def __str__(self) -> str:
        return self.name
