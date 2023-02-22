from django.contrib import admin
from .models import Category, Course, Lesson, Tag
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class LessonForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = Lesson
        fields = '__all__'
        

class TagInlineAdmin(admin.StackedInline):
    model = Lesson.tags.through
        
class LessonAdmin(admin.ModelAdmin):
    list_display = ['subject', 'content', 'course', 'image']
    search_field = ['tags']
    form = LessonForm
    inlines = [TagInlineAdmin,]
    
class CourseForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = Course
        fields = '__all__'


class CourseAdmin(admin.ModelAdmin):
    list_display = ['pk', 'subject', 'created_date', 'category']
    search_fields = ['subject']
    list_filter = ['id', 'subject', 'created_date']
    form = CourseForm

admin.site.register(Category)
admin.site.register(Course, CourseAdmin)
admin.site.register(Tag)
admin.site.register(Lesson, LessonAdmin)
