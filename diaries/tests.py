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
        # Simulate a POST request to the API endpoint
        response = self.client.post(f'{self.apiEndpoint}/', data=self.payload)

        # Assert the expected response status code
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Assert taht the emotional state was created in the database
        self.assertEqual(EmotionalState.objects.count(), 1)

        # Assert the values of the created emotional state
        emotional_state = EmotionalState.objects.first()
        self.assertEqual(emotional_state.name, self.payload['name'])
        self.assertEqual(emotional_state.date, self.payload['date'])
        self.assertEqual(emotional_state.energy, self.payload['energy'])
        self.assertEqual(emotional_state.intensity, self.payload['intensity'])
        self.assertEqual(emotional_state.triggers, self.payload['triggers'])
        self.assertEqual(emotional_state.coping_mechanisms,
                         self.payload['coping_mechanisms'])

    def test_retrieve_emotional_state(self):
        # Create an instance of EmotionalState
        emotional_state = EmotionalState.objects.create(**self.payload)

        # Simulate a GET request to the API endpoint
        response = self.client.get(
            f'{self.apiEndpoint}/{emotional_state.id}/', follow=True)

        # Asssert expected response status code
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_emotional_state(self):
        # Create and instance of EmotionalState
        emotional_state = EmotionalState.objects.create(**self.payload)

        payload = {
            'name': 'Happiness',
            'intensity': 0.9,
            'triggers': 'Music, Nature'
        }

        # Simulate a PATCH request to the API endpoint
        response = self.client.patch(
            f'{self.apiEndpoint}/{emotional_state.id}/', data=payload, content_type='application/json')

        # Assert expected response status code
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Retrieve the updated emotional state object
        updated_emotional_state = EmotionalState.objects.get(
            id=emotional_state.id)

        # Check that the fields were updated correctly
        self.assertEqual(updated_emotional_state.name, payload['name'])
        self.assertEqual(updated_emotional_state.intensity,
                         payload['intensity'])
        self.assertEqual(updated_emotional_state.triggers, payload['triggers'])
