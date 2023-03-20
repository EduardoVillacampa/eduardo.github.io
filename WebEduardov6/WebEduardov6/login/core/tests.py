from django.test import TestCase

# Create your tests here.
from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse

# Create your tests here.
#Prueba que  muestra la página de inicio sin ser necesario estar logueado
class TestCase1(TestCase):
   def test_view(self):
       response = self.client.get(reverse('inicio'))
       self.assertEqual(response.status_code, 200)
#Prueba para probar login (crea un usuario y accede mediante este)
class TestLogin(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user('test', 'test@test.com', 'password')
    def test_login(self):
        self.client.login(username='test', password='password')
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code,200)
#Prueba para comprobar que no se puede acceder a la página 'products' sin estar logueado
class TestCase2(TestCase):
   def test_view(self):
       response = self.client.get(reverse('products'))
       self.assertEqual(response.status_code, 302)
#prueba que no puede acceder al área cliente sin estar logueado
class TestCase3(TestCase):
   def test_view(self):
       response = self.client.get(reverse('formulario'))
       self.assertEqual(response.status_code, 302)
#Prueba para comprobar que funciona el log (sin crear usuario)
class TestCase4  (TestCase):
    def test_view(self):
        self.client.login(username='eduardo', password='vivaespaña')
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
#Prueba para comprobar que se puede acceder a area clientes si se está logueado
