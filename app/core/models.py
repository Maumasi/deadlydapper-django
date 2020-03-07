from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
                                        PermissionsMixin


class UserManager(BaseUserManager):

  def create_user(self, email, password=None, **extra_fields):
    """Creates and saves a new user"""
    if(not email):
      raise ValueError('User email not porvided')

    user = self.model(email=self.normalize_email(email.lower()), **extra_fields)
    user.set_password(password)
    user.save(using=self._db)
    return user

  def create_superuser(self, email, password):
    '''Creates new superuser'''
    if(not password):
      raise ValueError('Superusers are required to have a password')
    if(len(password) < 8):
      raise ValueError('Superusers passwords must be greater than 8 charactors')

    user = self.create_user(email, password)
    user.is_staff = True
    user.is_superuser = True
    user.save(using=self._db)
    return user


class User(AbstractBaseUser, PermissionsMixin):
  """Custom user model that supports using an email for the username"""

  email = models.EmailField(max_length=255, unique=True)
  name = models.CharField(max_length=255)
  is_active = models.BooleanField(default=True)
  is_staff = models.BooleanField(default=False)

  objects = UserManager()

  USERNAME_FIELD = 'email'
