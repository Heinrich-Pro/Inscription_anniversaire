from django.test import TestCase
from django.urls import reverse
from inscriptions.models import Participant

class InscriptionViewTests(TestCase):
    def test_inscription_view_get(self):
        response = self.client.get(reverse('inscription'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'inscription.html')

    def test_inscription_view_post_valid(self):
        data = {
            'nom': 'Dupont',
            'email': 'dupont@example.com',
            'message': 'Je souhaite participer à la fête !'
        }
        response = self.client.post(reverse('inscription'), data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('confirmation'))
        self.assertTrue(Participant.objects.filter(nom='Dupont', email='dupont@example.com').exists())
