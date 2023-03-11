from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, permissions, generics
from .models import Course, Category, Lesson
from .serializers import CourseSerializer, CategorySerializer, LessonSerializer
from rest_framework.decorators import action
from rest_framework.views import Response

class CourseViewSet(viewsets.ViewSet, generics.ListAPIView, generics.RetrieveAPIView):
    queryset = Course.objects.filter(active=True)
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    @action(methods=['get'], detail=True, url_path='lessons')
    def lessons(self, request, pk):
        course = self.get_object()
        lessons = course.lesson_set.filter(active=True)
        
        kw = request.query_params.get('kw')
        if kw:
            lessons = lessons.filter(subject__icontains=kw)
        return Response(LessonSerializer(lessons, many=True).data)
    
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]
    
class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.filter(active=True)
    serializer_class = LessonSerializer
    permission_classes = [permissions.IsAuthenticated]

# Create your views here.
def index(request):
    return HttpResponse("e-Course App")