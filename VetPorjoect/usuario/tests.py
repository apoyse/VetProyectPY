from django.test import TestCase
from usuario.models import User
from unittest import TestCase 
class UsuarioTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser',
         password='12345'
         )

    def test_common_user_creation(self):
        self.assertEqual(self.user.is_active,True) 
        self.assertEqual(self.user.is_staff,False)
        self.assertEqual(self.user.is_superuser,False)
# Create your tests here.
