from rest_framework import serializers
from .models import Exam, ExamStudent, Student


class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = ('exam_id', 'url', 'exam')


class ExamStudentSerializer(serializers.HyperlinkedModelSerializer):
    exam_id = serializers.ReadOnlyField(source="exam.id")
    exam_name = serializers.ReadOnlyField(source='exam.exam')

    # if I want to read the student name in the mark endpoint
    # student= serializers.ReadOnlyField(source='student.student_name')

    class Meta:
        model = ExamStudent
        fields = ('exam_id', 'exam_name', 'student', 'exam', 'mark')
        extra_kwargs = {
            'student': {'write_only': True},
            'exam': {'write_only': True},
        }


class StudentSerializer(serializers.ModelSerializer):
    exams = ExamStudentSerializer(many=True,source="examstudent_set", read_only=True)

    class Meta:
        model = Student
        fields = ('student_id', 'url', 'student_name', 'exams', 'adress')
