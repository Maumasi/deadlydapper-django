from django.test import TestCase
from django.contrib.auth import get_user_model


class UserModelTests(TestCase):

  def test_create_user_with_email_success(self):
    '''Test success of creating a new user with an email'''
    email = 'test@gmail.com'
    password = 'pw123'
    user = get_user_model().objects.create_user(email=email, password=password)
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
      get_user_model().objects.create_user(email=None, password='trashPassword')

  def test_create_new_superuser(self):
    '''Create super useer'''
    user = get_user_model().objects.create_superuser('su@gmail.com', 'trashPassword')
    self.assertTrue(user.is_superuser)
    self.assertTrue(user.is_staff)

  def test_superuser_has_invalid_password(self):
    '''
    Test if superuser has an invalid password
      - no password
      - greater than 8 chars
    '''
    # no password
    with self.assertRaises(ValueError):
      get_user_model().objects.create_superuser('su@gmail.com', password=None)
    # password less than 8 chrs
    with self.assertRaises(ValueError):
      get_user_model().objects.create_superuser('su@gmail.com', password='1234657')
