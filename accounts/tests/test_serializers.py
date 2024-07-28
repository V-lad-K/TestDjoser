from django.contrib.auth import get_user_model
from django.test import TestCase

# from ..models import User
from ..serializers import CustomUserCreateSerializer

User = get_user_model()


class UserRegistrationSerializerTestCase(TestCase):
    def test_serialize(self):
        user1 = User.objects.create_user(username="testUser1", email="testEmail1@gmail.com", password="testPassword123")
        user2 = User.objects.create_user(username="testUser2", email="testEmail2@gmail.com", password="testPassword456")

        data = CustomUserCreateSerializer([user1, user2], many=True).data

        expected_data = [
            {
                "id": user1.id,
                "username": "testUser1",
                "email": "testEmail1@gmail.com",
            },
            {
                "id": user2.id,
                "username": "testUser2",
                "email": "testEmail2@gmail.com"
            }
        ]

        self.assertEqual(expected_data, data)

    def test_valid_data(self):
        data = {
            "username": "gfdgfdgfd",
            "email": "krugonovskiy@gmail.com",
            "password": "jgkfdjkkJKJKjkgjfdkg546546jhjhHj",
            "re_password": "jgkfdjkkJKJKjkgjfdkg546546jhjhHj"
        }

        serializer = CustomUserCreateSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        serializer.save()

    def test_invalid_username_contain_space(self):
        data = {
            "email": "krugonovskiy@gmail.com",
            "password": "jgkfdjkkJKJKjkgjfdkg546546jhjhHj",
            "re_password": "jgkfdjkkJKJKjkgjfdkg546546jhjhHj"
        }
        invalid_username = "test name"
        data["username"] = invalid_username
        serializer = CustomUserCreateSerializer(data=data)

        self.assertFalse(serializer.is_valid())
        self.assertIn("username", serializer.errors)

    def test_username_too_short(self):
        data = {
            "email": "krugonovskiy@gmail.com",
            "password": "jgkfdjkkJKJKjkgjfdkg546546jhjhHj",
            "re_password": "jgkfdjkkJKJKjkgjfdkg546546jhjhHj"
        }
        invalid_username = "qwe"
        data["username"] = invalid_username
        serializer = CustomUserCreateSerializer(data=data)

        self.assertFalse(serializer.is_valid())
        self.assertIn("username", serializer.errors)

    def test_username_too_long(self):
        data = {
            "email": "krugonovskiy@gmail.com",
            "password": "jgkfdjkkJKJKjkgjfdkg546546jhjhHj",
            "re_password": "jgkfdjkkJKJKjkgjfdkg546546jhjhHj"
        }
        invalid_username = "t" * 151
        data["username"] = invalid_username
        serializer = CustomUserCreateSerializer(data=data)

        self.assertFalse(serializer.is_valid())
        self.assertIn("username", serializer.errors)

    def test_username_contain_cyrillic(self):
        data = {
            "email": "krugonovskiy@gmail.com",
            "password": "jgkfdjkkJKJKjkgjfdkg546546jhjhHj",
            "re_password": "jgkfdjkkJKJKjkgjfdkg546546jhjhHj"
        }
        invalid_username = "тестовийКористувач"
        data["username"] = invalid_username
        serializer = CustomUserCreateSerializer(data=data)

        self.assertFalse(serializer.is_valid())
        self.assertIn("username", serializer.errors)

    def test_username_contain_dot(self):
        data = {
            "email": "krugonovskiy@gmail.com",
            "password": "jgkfdjkkJKJKjkgjfdkg546546jhjhHj",
            "re_password": "jgkfdjkkJKJKjkgjfdkg546546jhjhHj"
        }
        invalid_username = "gfhkgkghmkgfhfg.hgfhgf"
        data["username"] = invalid_username
        serializer = CustomUserCreateSerializer(data=data)

        self.assertFalse(serializer.is_valid())
        self.assertIn("username", serializer.errors)

    def test_username_contain_slash(self):
        data = {
            "email": "krugonovskiy@gmail.com",
            "password": "jgkfdjkkJKJKjkgjfdkg546546jhjhHj",
            "re_password": "jgkfdjkkJKJKjkgjfdkg546546jhjhHj"
        }
        invalid_username = "gfhkgkghmkgfhfg//hgfhgf"
        data["username"] = invalid_username
        serializer = CustomUserCreateSerializer(data=data)

        self.assertFalse(serializer.is_valid())
        self.assertIn("username", serializer.errors)

    def test_username_contain_only_numbers(self):
        data = {
            "email": "krugonovskiy@gmail.com",
            "password": "jgkfdjkkJKJKjkgjfdkg546546jhjhHj",
            "re_password": "jgkfdjkkJKJKjkgjfdkg546546jhjhHj"
        }
        invalid_username = "455155"
        data["username"] = invalid_username
        serializer = CustomUserCreateSerializer(data=data)

        self.assertFalse(serializer.is_valid())
        self.assertIn("username", serializer.errors)

    def test_invalid_email_contain_space(self):
        data = {
            "username": "TestUsername",
            "password": "jgkfdjkkJKJKjkgjfdkg546546jhjhHj",
            "re_password": "jgkfdjkkJKJKjkgjfdkg546546jhjhHj"
        }
        invalid_email = "test email@gmail.com"
        data["email"] = invalid_email
        serializer = CustomUserCreateSerializer(data=data)

        self.assertFalse(serializer.is_valid())
        self.assertIn("email", serializer.errors)

    def test_invalid_email_too_short(self):
        data = {
            "username": "TestUsername",
            "password": "jgkfdjkkJKJKjkgjfdkg546546jhjhHj",
            "re_password": "jgkfdjkkJKJKjkgjfdkg546546jhjhHj"
        }
        invalid_email = "kr@gmail.com"
        data["email"] = invalid_email
        serializer = CustomUserCreateSerializer(data=data)

        self.assertFalse(serializer.is_valid())
        self.assertIn("email", serializer.errors)

    def test_invalid_email_too_long(self):
        email_local__part = "k"
        data = {
            "username": "TestUsername",
            "password": "jgkfdjkkJKJKjkgjfdkg546546jhjhHj",
            "re_password": "jgkfdjkkJKJKjkgjfdkg546546jhjhHj"
        }
        invalid_email = (email_local__part * 150) + "@gmail.com"
        data["email"] = invalid_email
        serializer = CustomUserCreateSerializer(data=data)

        self.assertFalse(serializer.is_valid())
        self.assertIn("email", serializer.errors)

    def test_invalid_email_too_short_local_part(self):
        email_local__part = "k"
        data = {
            "username": "TestUsername",
            "password": "jgkfdjkkJKJKjkgjfdkg546546jhjhHj",
            "re_password": "jgkfdjkkJKJKjkgjfdkg546546jhjhHj"
        }
        invalid_email = (email_local__part * 3) + "@gmail.com"
        data["email"] = invalid_email
        serializer = CustomUserCreateSerializer(data=data)

        self.assertFalse(serializer.is_valid())
        self.assertIn("email", serializer.errors)

    def test_invalid_email_too_short_domain_part(self):
        email_local_part = "testEmailUser"
        email_domain_part = "@.com"
        data = {
            "username": "TestUsername",
            "password": "jgkfdjkkJKJKjkgjfdkg546546jhjhHj",
            "re_password": "jgkfdjkkJKJKjkgjfdkg546546jhjhHj"
        }
        invalid_email = email_local_part + email_domain_part
        data["email"] = invalid_email
        serializer = CustomUserCreateSerializer(data=data)

        self.assertFalse(serializer.is_valid())
        self.assertIn("email", serializer.errors)

    def test_invalid_email_invalid_structure(self):
        data = {
            "username": "TestUsername",
            "password": "jgkfdjkkJKJKjkgjfdkg546546jhjhHj",
            "re_password": "jgkfdjkkJKJKjkgjfdkg546546jhjhHj"
        }
        invalid_email = "notEmailFormat"
        data["email"] = invalid_email
        serializer = CustomUserCreateSerializer(data=data)

        self.assertFalse(serializer.is_valid())
        self.assertIn("email", serializer.errors)

    def test_invalid_password_contain_space(self):
        data = {
            "username": "TestUsername",
            "email": "krugonovskiy@gmail.com",
            "re_password": "jgkfdjkkJKJKjkgjfdkg546546jhjhHj"
        }
        invalid_password = "test password"
        data["password"] = invalid_password
        serializer = CustomUserCreateSerializer(data=data)

        self.assertFalse(serializer.is_valid())
        self.assertIn("password", serializer.errors)

    def test_invalid_password_too_short(self):
        data = {
            "username": "TestUsername",
            "email": "krugonovskiy@gmail.com",
            "re_password": "jgkfdjkkJKJKjkgjfdkg546546jhjhHj"
        }
        invalid_password = "test"
        data["password"] = invalid_password
        serializer = CustomUserCreateSerializer(data=data)

        self.assertFalse(serializer.is_valid())
        self.assertIn("password", serializer.errors)

    def test_invalid_password_too_long(self):
        data = {
            "username": "TestUsername",
            "email": "krugonovskiy@gmail.com",
            "re_password": "jgkfdjkkJKJKjkgjfdkg546546jhjhHj"
        }
        invalid_password = "t" * 151
        data["password"] = invalid_password
        serializer = CustomUserCreateSerializer(data=data)

        self.assertFalse(serializer.is_valid())
        self.assertIn("password", serializer.errors)

    def test_invalid_password_contain_at_least_one_upper_character(self):
        data = {
            "username": "TestUsername",
            "email": "krugonovskiy@gmail.com",
            "re_password": "jgkfdjkkJKJKjkgjfdkg546546jhjhHj"
        }
        invalid_password = "test_password"
        data["password"] = invalid_password
        serializer = CustomUserCreateSerializer(data=data)

        self.assertFalse(serializer.is_valid())
        self.assertIn("password", serializer.errors)

    def test_invalid_password_contain_at_least_one_digit_character(self):
        data = {
            "username": "TestUsername",
            "email": "krugonovskiy@gmail.com",
            "re_password": "jgkfdjkkJKJKjkgjfdkg546546jhjhHj"
        }
        invalid_password = "testPassword"
        data["password"] = invalid_password
        serializer = CustomUserCreateSerializer(data=data)

        self.assertFalse(serializer.is_valid())
        self.assertIn("password", serializer.errors)

    def test_invalid_password_contain_cyrillic_character(self):
        data = {
            "username": "TestUsername",
            "email": "krugonovskiy@gmail.com",
            "re_password": "jgkfdjkkJKJKjkgjfdkg546546jhjhHj"
        }
        invalid_password = "тестовийПароль123"
        data["password"] = invalid_password
        serializer = CustomUserCreateSerializer(data=data)

        self.assertFalse(serializer.is_valid())
        self.assertIn("password", serializer.errors)
