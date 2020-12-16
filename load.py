import json
from locust import HttpUser,task,between

class QuickstartUser(HttpUser):
    def __init__(self,parent):
        super(QuickstartUser,self).__init__(parent)
        self.token = None

    wait_time = between(1,2)

    #def on_start(self):
    #    self.token = self.login()
    #    print(self.token)
        
    def login(self):
        json_data = {
            "email": "rajat.main06@gmail.com",
            "password": "dev"
        }
        response = self.client.post(url="/api/student/login",data = json_data)

        return json.loads(response._content)['token']


    @task
    def server_check(self):
        self.client.get(url="checkServer")
    
    @task
    def check_club_profile(self):
        self.client.get(url="api/club/details?clubId=5fc8e1d5ca0c7edf35ac2e3c")

    @task
    def get_student_details(self):
        self.client.get(url="api/student/details?studentId=5fc927fbf3c0b412006b7db4")

    
    