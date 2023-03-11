from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('courses', views.CourseViewSet)
router.register('categories', views.CategoryViewSet)
router.register('lessons', views.LessonViewSet)

urlpatterns = [
    path('', include(router.urls))
]
