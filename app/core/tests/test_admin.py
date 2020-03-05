from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTests(TestCase):
  def setUp(self):
    '''setup util'''
    self.client = Client()
    self.admin_user = get_user_model().objects.create_superuser(
      email='andy@gmail.com',
      password='abc12345678'
    )
    self.client.force_login(self.admin_user)
    self.user = get_user_model().objects.create_user(
      'reguser@gmail.com',
      'qwerty',
      name='johnny everyman'
    )

  def test_users_are_listed(self):
    '''test that users aree listed on user's page'''
    url = reverse('admin:core_user_changelist')
    res = self.client.get(url)

    self.assertContains(res, self.user.name)
    self.assertContains(res, self.user.email)
