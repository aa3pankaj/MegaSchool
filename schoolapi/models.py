from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser

#from apisite import  settings
from django.contrib.auth import get_user_model
USER_TYPE_CHOICES = (
        ('1', 'student'),
        ('2', 'teacher'),
        ('3','parent'),
        ('4','schooladmin')
    )
class CustomUser(AbstractUser):
    user_type=models.CharField(choices=USER_TYPE_CHOICES,max_length=10)
    # is_student=models.BooleanField(default=False)
    # is_parent = models.BooleanField(default=False)
    # is_teacher = models.BooleanField(default=False)
    # is_school_admin = models.BooleanField(default=False)

class Parent (models.Model):
    user = models.OneToOneField(get_user_model(),on_delete=models.CASCADE)
    fname = models.CharField(max_length=45)
    lname = models.CharField(max_length=45)
    dob = models.DateField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    #user_id=models.CharField(max_length=50)
    mobile=models.CharField(max_length=20,blank=True,null=True)
    last_login_date = models.DateField(null=True, blank=True)
    last_login_ip = models.CharField(max_length=100, null=True, blank=True)
    def __str__(self):
        return self.fname + ' ' + self.lname

class Student(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    fname = models.CharField(max_length=45)
    lname = models.CharField(max_length=45)
    dob = models.DateField(null=True, blank=True)
    #user_id=models.CharField(max_length=50)
    mobile=models.CharField(max_length=15,blank=True,null=True)
    email = models.EmailField(null=True, blank=True)
    parent=models.ManyToManyField('Parent',default='')
    last_login_date = models.DateField(null=True, blank=True)
    last_login_ip = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
         return self.fname+' '+self.lname

# class Role(models.Model):
#   '''
#   The Role entries are managed by the system,
#   automatically created via a Django data migration.
#   '''
#   STUDENT = 1
#   TEACHER = 2
#   PARENT = 3
#   ADMIN = 4
#   ROLE_CHOICES = (
#       (STUDENT, 'student'),
#       (TEACHER, 'teacher'),
#       (PARENT, 'parent'),
#       (ADMIN, 'admin'),
#   )
#
#   id = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, primary_key=True)
#
#   def __str__(self):
#       return self.get_id_display()

class Teacher(models.Model):
    #user = models.OneToOneField(User)
    #username = models.CharField(max_length=45)
    #email = models.CharField(max_length=45, null=True, blank=True)
    #password = models.CharField(max_length=45)
    #reg_number = models.CharField(max_length=30)
    fname = models.CharField(max_length=45)
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    lname = models.CharField(max_length=45)
    dob = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    mobile = models.CharField(max_length=20, null=True, blank=True)
    date_of_join = models.DateField(null=True, blank=True)
    #status = models.BooleanField()
    last_login_date = models.DateField(null=True, blank=True)
    last_login_ip = models.CharField(max_length=100,null=True, blank=True)

    def __str__(self):
        return self.fname+' '+self.lname

class Course(models.Model):
    name=models.CharField(max_length=45)
    desc = models.CharField(max_length=45)
    def __str__(self):
        return self.name
class Subject(models.Model):
    name = models.CharField(max_length=45)
    desc = models.CharField(max_length=45)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    def __str__(self):
        return self.name
class ClassRoom(models.Model):
    student = models.ManyToManyField(Student)
    year =models.CharField(max_length=10)
    section=models.CharField(max_length=10)
    #status=models.BooleanField(default=True)
    teacher=models.ForeignKey(Teacher,on_delete=models.CASCADE)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)

class Attendance(models.Model):
    date=models.DateField()
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    status=models.BooleanField()
    remark=models.TextField(blank=True,null=True)

class ExamType(models.Model):
    name = models.CharField(max_length=45)
    desc = models.CharField(max_length=45,blank=True)
    def __str__(self):
        return self.name

class Exam(models.Model):
    name=models.CharField(max_length=45)
    start_date=models.DateField()
    exam_type=models.ForeignKey(ExamType,on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE,default=1)
    def __str__(self):
        return self.name

class ExamResult(models.Model):
    marks=models.CharField(max_length=45)
    exam=models.ForeignKey(Exam,on_delete=models.CASCADE)
    student = models.ForeignKey(Student,on_delete=models.CASCADE)

