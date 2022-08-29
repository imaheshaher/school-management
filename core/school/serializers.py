from dataclasses import field
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import get_user_model
from school.models import School,StudentGrade
User = get_user_model()


# for school
class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            validators=[UniqueValidator(queryset=User.objects.all())]
            ,required=False)

    password = serializers.CharField(write_only=True, required=True,)
    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name','user_type')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()

        return user


class ListUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["first_name","last_name","email","username"]



class UpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields=["first_name","last_name"]


class SchoolSerializer(serializers.ModelSerializer):
    school = RegisterSerializer()
    class Meta:
        model = School
        fields = ["city","pincode","school"]
    def create(self, validated_data):
        school = validated_data.pop('school')
        schooluser = User(**school)
        schooluser.set_password(school['password'])
        schooluser.save()

        school = School.objects.create(city=validated_data['city'],pincode=validated_data['pincode'],school=schooluser)

        return school



class StudentGradeSerializer(serializers.ModelSerializer):
    school = SchoolSerializer(read_only=True)
    student = ListUserSerializer(read_only=True)
    class Meta:
        model= StudentGrade
        fields="__all__"