from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.hashers import make_password
from django.conf import settings

class UserProfileManager(BaseUserManager):
    """Manager for users profiles"""
    
    def create_user(self, email,  password, **extra_fields):
        """create a new user profile"""

        if not email:
            raise ValueError ('User must have a valid email address')
        if not password:
            raise ValueError("User must have a password")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
       
        
    def create_superuser(self, email,  password, **extra_fields):
        """Create and save a new superuser"""

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """database model for users"""
    email= models.EmailField(max_length=255, unique=True)
    name= models.CharField(max_length= 255)
    is_active= models.BooleanField(default=True)
    is_staff= models.BooleanField(default=False)
    USERNAME_FIELD ='email'
    REQUIRE_FIELDS = []
    objects= UserProfileManager()
 
    def get_full_name (self):
        """Retrieve full name of user"""
        return self.name
    
    def get_short_name (self):
        """Retrieve short name of user"""
        return self.name

    def __str__(self):
        """Return string representation of our user"""
        return self.email


class ProfileFeedItem(models.Model):
    """Profile status update"""
    user_profile= models.ForeignKey(settings.AUTH_USER_MODEL,
    on_delete= models.CASCADE)
    status_text = models.CharField(max_length=255)
    created_on= models.DateTimeField(auto_now_add=True)

    def __str__ (self):
        """Return the model as a string"""
        return self.status_text