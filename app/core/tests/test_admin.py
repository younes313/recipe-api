from django.test import TestCase, Client
from django.urls import reverse
# from django.utils import
from django.contrib.auth import get_user_model


class AdminTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email="admin@admin.com",
            password="admin123"
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email="user@user.com",
            password="user123",
            name="the user name"
        )

    def test_user_listed(self):
        """test that all users are listed"""
        url = reverse("admin:core_user_changelist")
        res = self.client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)
