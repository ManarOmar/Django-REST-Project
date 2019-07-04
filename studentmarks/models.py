from django.db import models


class Exam(models.Model):
    exam_id = models.AutoField(primary_key=True)
    exam = models.TextField()

    class Meta:
        managed = False
        db_table = 'exam'

    def __str__(self):
        return self.exam


class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    adress = models.TextField()
    student_name = models.TextField()
    exams = models.ManyToManyField('Exam', through ="ExamStudent")

    class Meta:
        managed = False
        db_table = 'student'

    def __str__(self):
        return self.student_name


class ExamStudent(models.Model):
    student = models.ForeignKey(Student, models.DO_NOTHING, blank=True, null=True)
    exam = models.ForeignKey(Exam, models.DO_NOTHING, blank=True, null=True)
    mark = models.DecimalField(max_digits=4, decimal_places=2)
    student_exam_id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'exam_student'
