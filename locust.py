from locust import HttpUser, task

input_data = {
   "CHAS":{
      "0":0
   },
   "RM":{
      "0":6.575
   },
   "TAX":{
      "0":296.0
   },
   "PTRATIO":{
      "0":15.3
   },
   "B":{
      "0":396.9
   },
   "LSTAT":{
      "0":4.98
   }
}

class LocustTaskSet(HttpUser):

	@task
	def get_site(self):
		self.client.get('/')

	@task
	def get_prediction(self):
		self.client.post('/predict', json=input_data)
