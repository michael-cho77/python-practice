from django.test import TestCase
from classroom.models import Student, Classroom

from mixer.backend.django import mixer
import pytest


pytestmark = pytest.mark.django_db


class TestStudentModel(TestCase):

    # def setUp(self):
    #         self.student1 = Student.objects.create(
    #         first_name="John", last_name="Doe", admission_number=12345
    #     )

    def test_student_can_be_created(self):
        
        student1 = mixer.blend(Student, first_name="John")
        
        student_result = Student.objects.last()  # getting the last student

        #self.assertEqual(student_result.first_name, "John")
        assert student_result.first_name == "John"

    def test_str_return(self):
        
        student1 = Student.objects.create(
            first_name="John", last_name="Doe", admission_number=1234, average_score=30
        )
        
        student_result = Student.objects.last()  # getting the last student
        
        #self.assertEqual(str(student_result), "John")
        assert str(student_result) == "John"

    def test_grade_fail(self):
        
        student1 = mixer.blend(Student, average_score=10)

        student_result = Student.objects.last()  # getting the last student
        
        #self.assertEqual(student_result.get_grade(), "Fail")
        assert student_result.get_grade() == "Fail"

    def test_grade_pass(self):

        student1 = mixer.blend(Student, average_score=60)

        student_result = Student.objects.last()  # getting the last student

        #self.assertEqual(student_result.get_grade(), "Pass")
        assert student_result.get_grade() == "Pass"

    def test_grade_excellent(self):

        student1 = Student.objects.create(
            first_name="John", last_name="Doe", admission_number=1234, average_score=90
        )

        student_result = Student.objects.last()  # getting the last student

        #self.assertEqual(student_result.get_grade(), "Excellent")
        assert student_result.get_grade() == "Excellent"
    
    
    def test_grade_error(self):

        student1 = Student.objects.create(
            first_name="John", last_name="Doe", admission_number=1234, average_score=101
        )

        student_result = Student.objects.last()  # getting the last student

        #self.assertEqual(student_result.get_grade(), "Excellent")
        assert student_result.get_grade() == "Error"


    def test_add_a_plus_b(self):
        a = 1
        b = 2
        c = a + b

        #self.assertEqual(c, 3)
        assert c == 3
        

class TestClassroomModel:
    def test_classroom_create(self):
        classroom = mixer.blend(Classroom, name="Math")
        
        classroom_result = Classroom.objects.last()  # getting the last classroom
        
        assert str(classroom_result) == "Math"