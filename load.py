from locust import HttpUser,task,between

class QuickstartUser(HttpUser):
    def __init__(self,parent):
        super(QuickstartUser,self).__init__(parent)
        self.token = None

    wait_time = between(1,2)

    def on_start(self):
        with self.client.post(url="/api/student/login",{{
            "email": "rajat.main06@gmail.com",
            "password": "dev"
        }}) as response:
            self.token = response.json["token"]

    @task
    def next_page(self):
        self.client.get(url="/api/club/profile",headers={"authorization":self.token})