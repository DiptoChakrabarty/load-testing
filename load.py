import json
from locust import HttpUser,task,between

class QuickstartUser(HttpUser):
    def __init__(self,parent):
        super(QuickstartUser,self).__init__(parent)
        self.token = None

    wait_time = between(1,2)

    def on_start(self):
        self.token = self.login()
        print(self.token)
        
    def login(self):
        json_data = {
            "email": "rajat.main06@gmail.com",
            "password": "dev"
        }
        response = self.client.post(url="/api/student/login",data = json_data)

        return json.loads(response._content)['token']


    @task
    def profile_page(self):
        self.client.get(url="/api/club/profile",headers={"authorization":self.token})

    
    @task
    def all_featured_clubs(self):
       self.client.get(url="/api/club/allFeatured",headers={"authorization":self.token})