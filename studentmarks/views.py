from django.shortcuts import render
from rest_framework import viewsets
from .models import Exam, ExamStudent, Student
from .serializers import ExamSerializer, ExamStudentSerializer, StudentSerializer

class StudentView(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class ExamView(viewsets.ModelViewSet):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer

class ExamStudentView(viewsets.ModelViewSet):
    queryset = ExamStudent.objects
    serializer_class = ExamStudentSerializer





