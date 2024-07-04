from ginger.db import models


Course_Typeenum = (
    ("compulsary" , "Compulsary"),
    ("elective" , "Elective"),

)


Subjectenum = (
    ("english" , "English"),
    ("hindi" , "Hindi"),
    ("maths" , "Maths"),
    ("science" , "Science"),
    ("social_studies" , "Social Studies"),

)


class Student(models.Model):
    name = models.CharField(max_length=150, null=False)
    roll_number = models.CharField(max_length=40, null=False)
    on_scholarship = models.BooleanField(default=True, null=False)
    father_name = models.CharField(max_length=100, null=True)
    address = models.TextField(max_length=500, null=False)
    data_of_birth = models.DateField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateField(auto_now=True, null=False)
    has_cab_service = models.BooleanField(null=True)

    class Meta:
        managed = False


class Enrollment(models.Model):
    student = models.ForeignKey("Student", on_delete=models.DO_NOTHING, null=False)
    course = models.ForeignKey("Course", on_delete=models.SET_NULL, null=True)

    class Meta:
        managed = False


class Course(models.Model):
    name = models.CharField(max_length=100, null=False)
    course_type = models.CharField(default="compulsary", choices=Course_Typeenum, null=False)
    duration = models.PositiveIntegerField(null=True)

    class Meta:
        managed = False


class Exam(models.Model):
    date = models.DateField(auto_now_add=True, null=False)
    subject = models.CharField(choices=Subjectenum, null=False)

    class Meta:
        managed = False
