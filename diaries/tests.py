from datetime import date
from django.test import TestCase, Client
from rest_framework import status
from .models import EmotionalState


class EmotionalStateAPITestCase(TestCase):
    def setUp(self):
        self.client = Client()

    payload = {
        'name': 'Joy',
        'date': date.today(),
        'energy': 0.8,
        'intensity': 0.8,
        'triggers': 'Music, Spending time with loved ones',
        'coping_mechanisms': 'Deep breathing, Positive affirmation'
    }

    apiEndpoint = '/api/emotional-states'

    def test_create_emotional_state(self):
        response = self.client.post(f'{self.apiEndpoint}/', data=self.payload)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(EmotionalState.objects.count(), 1)

        emotional_state = EmotionalState.objects.first()
        self.assertEqual(emotional_state.name, self.payload['name'])
        self.assertEqual(emotional_state.date, self.payload['date'])
        self.assertEqual(emotional_state.energy, self.payload['energy'])
        self.assertEqual(emotional_state.intensity, self.payload['intensity'])
        self.assertEqual(emotional_state.triggers, self.payload['triggers'])
        self.assertEqual(emotional_state.coping_mechanisms,
                         self.payload['coping_mechanisms'])

    def test_retrieve_emotional_state(self):
        emotional_state = EmotionalState.objects.create(**self.payload)

        response = self.client.get(
            f'{self.apiEndpoint}/{emotional_state.id}/', follow=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_emotional_state(self):
        emotional_state = EmotionalState.objects.create(**self.payload)

        payload = {
            'name': 'Happiness',
            'intensity': 0.9,
            'triggers': 'Music, Nature'
        }

        response = self.client.patch(
            f'{self.apiEndpoint}/{emotional_state.id}/', data=payload, content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        updated_emotional_state = EmotionalState.objects.get(
            id=emotional_state.id)

        self.assertEqual(updated_emotional_state.name, payload['name'])
        self.assertEqual(updated_emotional_state.intensity,
                         payload['intensity'])
        self.assertEqual(updated_emotional_state.triggers, payload['triggers'])

    def test_delete_emotional_state(self):
        emotional_state = EmotionalState.objects.create(**self.payload)

        response = self.client.delete(
            f'{self.apiEndpoint}/{emotional_state.id}/')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
