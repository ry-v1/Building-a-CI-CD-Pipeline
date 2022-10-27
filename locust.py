from locust import HttpUser, task
from data_test import input_data

class LocustTaskSet(HttpUser):

	@task
	def get_site(self):
		self.client.get('/')

	@task
	def get_prediction(self):
		self.client.post('/predict', json=input_data)
