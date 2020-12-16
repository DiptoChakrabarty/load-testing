from locust import HttpUser,task,between

class QuickstartUser(HttpUser):
    def __init__(self,parent):
        super(QuickstartUser,self).__init__(parent)
        self.token = None

    wait_time = between(1,2)

    def on_start(self):
        self.login()

    def login(self):
        self.client.post("/api/student/login",
        {
        "email": "rajat.main06@gmail.com",
        "password": "dev"
    })       

    @task
    def get_clubs(self):
        self.client.get(url="/api/club/profile",headers={"authorization":self.token})