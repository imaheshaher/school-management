
from rest_framework import filters
from django.contrib.auth.models import User
from school.serializers import ListUserSerializer, RegisterSerializer, SchoolSerializer, UpdateUserSerializer,StudentGradeSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny,IsAuthenticated
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import login
User = get_user_model()
from school.constant_data import USER_TYPE_DICT
from school.models import Grade, School, StudentGrade
from django_filters.rest_framework import DjangoFilterBackend

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer



#Genric class for updating and get user detail for school and student
class StudentAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def get_object(self, pk=None):
        try:
            if pk:
                return User.objects.get(pk=pk,user_type='student')
            return User.objects.filter(user_type='student')
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk=None, format=None):
        if request.user.user_type==USER_TYPE_DICT['student']:
            user = self.get_object(request.user.id)
            serializer = ListUserSerializer(user)
            return Response(serializer.data)
        if pk:
            user = self.get_object(pk)
            serializer = ListUserSerializer(user)
        else:
            user = self.get_object()
            serializer = ListUserSerializer(user,many=True)
        
        return Response(serializer.data)

    def post(self,request):
        if request.user.user_type!=USER_TYPE_DICT['school']:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None, format=None):
        if request.user.user_type==USER_TYPE_DICT['student']:
            student = self.get_object(request.user.id)
        else:
            student = self.get_object(pk)
        serializer = UpdateUserSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        student = self.get_object(pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class RegisterSchoolView(APIView):
    permission_classes = (AllowAny,)

    def post(self,request):
        serializer = SchoolSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



class RegisterStudentGrade(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self,request):
        for data in request.data:
            serializer = RegisterSerializer(data=data["student"])

            if serializer.is_valid():
                student = serializer.save()
                school=School.objects.get(school=request.user.id)
                grade = Grade.objects.get(id=data['grade'])
                StudentGrade.objects.create(student=student,grade=grade,school=school)
                print(student)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            return Response("created")


class StudentGradeView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)

    queryset = StudentGrade.objects.all()
    serializer_class = StudentGradeSerializer
    filter_backends = [DjangoFilterBackend,filters.OrderingFilter]
    filterset_fields = ['student', 'grade']
    ordering_fields = ['student', 'grade']
