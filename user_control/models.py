import email
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager



class CustomUserManager(BaseUserManager):
  def create_user(self, email, password, **kwargs):
    
    if not email:
      raise ValueError('email field is required')
    
    user = self.model(email=email, **kwargs)
    user.set_password(password)
    user.save()
    
    return user
  
  def create_superuser(self, email,password, **kwargs):
    kwargs.setdefault('is_staff', True)
    kwargs.setdefault('is_superuser', True)
    
    if kwargs.get('is_staff') is not True:
      raise ValueError('superuser must be true')
    if kwargs.get('is_staff') is not True:
      raise ValueError('superuser must be true')
    
    return self.create_user(email,password, **kwargs)
  
class DateAbstract(models.Model):
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  
  class Meta:
    abstract = True
    

class CustomUser(AbstractBaseUser, PermissionsMixin, DateAbstract):
  is_staff = models.BooleanField(default=False)
  email = models.EmailField(unique=True)
  
  USERNAME_FIELD = 'email'
  objects = CustomUserManager()
  
  def __str__(self): #string representation 
      return self.email
    
# Userprofile

class UserProfile(DateAbstract):
  user = models.OneToOneField(CustomUser, related_name='user_profile', on_delete=models.CASCADE)
  first_name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)
  gender = models.CharField(max_length=6, choices=(('male', 'male'), ('female', 'female')))
  dob = models.DateField()
  phone = models.PositiveBigIntegerField()
  city = models.CharField(max_length=50)
  region = models.CharField(max_length=100)
  address = models.TextField()
  
  def __str__(self):
      return self.user.email
    
class Student(DateAbstract):
  about = models.TextField()
  username = models.CharField(max_length=50, unique=True)
  user = models.OneToOneField(CustomUser, related_name='student_profile', on_delete=models.CASCADE)
  
  def __str__(self):
      return self.user.email
    
class Teacher(DateAbstract):
  about = models.TextField()
  user = models.OneToOneField(CustomUser, related_name='teacher_profile', on_delete=models.CASCADE)
  qualification = models.CharField(max_length=5, )
  yof = models.PositiveSmallIntegerField()
  
  def __str__(self):
      return self.user.email
  
  