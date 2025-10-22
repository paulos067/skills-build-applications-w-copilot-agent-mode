from rest_framework.test import APITestCase
from django.urls import reverse

class APIRootTest(APITestCase):
	def test_api_root(self):
		url = reverse('api-root')
		response = self.client.get(url)
		self.assertEqual(response.status_code, 200)
		self.assertIn('users', response.data)
		self.assertIn('teams', response.data)
		self.assertIn('activities', response.data)
		self.assertIn('leaderboard', response.data)
		self.assertIn('workouts', response.data)

class UserAPITest(APITestCase):
	def test_list_users(self):
		url = reverse('user-list')
		response = self.client.get(url)
		self.assertEqual(response.status_code, 200)

class TeamAPITest(APITestCase):
	def test_list_teams(self):
		url = reverse('team-list')
		response = self.client.get(url)
		self.assertEqual(response.status_code, 200)

class ActivityAPITest(APITestCase):
	def test_list_activities(self):
		url = reverse('activity-list')
		response = self.client.get(url)
		self.assertEqual(response.status_code, 200)

class LeaderboardAPITest(APITestCase):
	def test_list_leaderboard(self):
		url = reverse('leaderboard-list')
		response = self.client.get(url)
		self.assertEqual(response.status_code, 200)

class WorkoutAPITest(APITestCase):
	def test_list_workouts(self):
		url = reverse('workout-list')
		response = self.client.get(url)
		self.assertEqual(response.status_code, 200)
