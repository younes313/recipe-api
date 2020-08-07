from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTest(TestCase):

    def test_create_user_with_email_succeful(self):
        """test that create a new user woth email is succefully done"""
        email = "test@test.com"
        password = "test123"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_email_is_normalized(self):
        """test that new user email is normalized"""
        email = "test@TESt.cOM"
        user = get_user_model().objects.create_user(
            email=email,
            password="test123"
        )

        self.assertEqual(user.email, email.lower())

    def test_new_user_should_have_email(self):
        """test that new user requires email"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                email=None,
                password="test123"
            )

    def test_create_superuser(self):
        """test that createsuper user works"""
        user = get_user_model().objects.create_superuser(
            email="test@test.com",
            password="test123"
        )

        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
