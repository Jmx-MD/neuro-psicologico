from django.test import TestCase, Client
from django.urls import reverse
import json
from .models import User

class UserApiTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_create_user_via_submit_form(self):
        data = {
            'nome': 'Teste',
            'email': 'teste@example.com',
            'data_nascimento': '1990-01-01',
            'senha': 'securepassword',
            'sexo': 'M'
        }
        response = self.client.post('/api/users/', data=json.dumps(data), content_type='application/json')
        self.assertIn(response.status_code, (200,201, 302, 201))
        # verify user in DB
        exists = User.objects.filter(email='teste@example.com').exists()
        self.assertTrue(exists)
