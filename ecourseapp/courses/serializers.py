from rest_framework.serializers import ModelSerializer, Serializer
from .models import Course, Category, Lesson
from rest_framework import serializers

class CourseSerializer(ModelSerializer):
    image = serializers.SerializerMethodField(source = 'image')
    
    def get_image(self, course):
        if course.image:
            request = self.context.get('request')
            return request.build_absolute_uri('/static/%s' % (course.image.name))
    
    class Meta:
        model = Course
        fields = ['id', 'subject', 'created_date', 'category', 'image']
        
class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']
        
class LessonSerializer(ModelSerializer):
    image = serializers.SerializerMethodField(source = 'image')
    
    def get_image(self, lesson):
        if lesson.image:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri('/static/%s' % (lesson.image.name))

    
    class Meta:
        model = Lesson
        fields = ['subject', 'content', 'course', 'image', 'tags']
        

