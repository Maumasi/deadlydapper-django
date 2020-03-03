from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):

  def test_create_user_with_email_success(self):
    '''Test success of creating a new user with an email'''

    email = 'test@gmail.com'
    password = 'pw123'
    user = get_user_model().objects.create_user(email=email,password=password)

    self.assertEqual(user.email, email)
    self.assertTrue(user.check_password(password))
  
  def test_new_user_email_normalized(self):
    '''Test that user email is converted to lowercase'''

    email = 'EXAMPLE@gmail.COM'
    user = get_user_model().objects.create_user(email, 'trashPassword')

    self.assertEqual(user.email, email.lower())

  def test_new_user_invalid_email(self):
    '''Test user with no email raises error'''

    with self.assertRaises(ValueError):
      get_user_model().objects.create_user(email=None,password='trashPassword')

  
  def test_create_new_superuser(self):
    '''Create super useer'''
    user = get_user_model().objects.create_superuser('su@gmail.com','trashPassword')

    self.assertTrue(user.is_superuser)
    self.assertTrue(user.is_staff)
