import imp
from django.urls import path
from school.views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
       path('register/', RegisterView.as_view(), name='auth_register'),
       path('student/', StudentAPIView.as_view()),
       path('student/<int:pk>', StudentAPIView.as_view()),
       path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
       path('school/', RegisterSchoolView.as_view(), name='school'),
       path('grade/', RegisterStudentGrade.as_view(), name='grade'),
       path('student-grade/', StudentGradeView.as_view(), name='grade'),


    
]
