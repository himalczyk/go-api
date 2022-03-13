from lib2to3.pytree import Base
from multiprocessing.sharedctypes import Value
from unicodedata import name
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    """Manager for user profiles. Specify some functions that can be user to manipulate objects the manager is for."""    

    def create_user(self, email, name, password=None):
        """Create a new user profile."""
        
        if not email:
            raise ValueError('User must have an email address')
        
        #normalize email address, first half is case sensitive, second nope, standarize the second half to lowercase
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)
        
        #user set_password method to protect the password encrypted
        user.set_password(password)
        #use built in db to save the user, comes in handy while working with multiple databases
        user.save(using=self._db)
        
        return user
    
    def create_superuser(self, email, name, password):
        """Create and save a new superuser with given details"""
        
        user = self.create_user(email, name, password)
        
        #superuser field is automatically created by inheritance of PermissionsMixin in the UserProfile class
        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)
        
        return user 

class UserProfile(AbstractBaseUser, PermissionsMixin):
    """"Database model for users in the system"""
    
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    #not yet created
    objects = UserProfileManager()
    
    #override username field with email field above
    USERNAME_FIELD = 'email'
    # user must specify the name
    REQUIRED_FIELDS = ['name']
    
    def get_full_name(self):
        """Retrieve full name of a user"""
        
        return self.name
    
    def get_short_name(self):
        """Retrieve short name of a user"""
        
        return self.name
    
    def __str__(self) -> str:
        """Return string representation of a user"""
        
        return self.email
    

