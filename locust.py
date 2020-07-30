from locust import HttpLocust, TaskSet, task
#from requests.auth import HTTPBasicAuth
 

 
class UserDefinedTask(TaskSet):
    def on_start(self):
        """ call when locust start i.e before exection of tasks"""
        self.login()
 
    @task(2)
    def home(self):
        self.client.get("/")
 
    @task(1)
    def about(self):
        """load testing on page containing http_basic_authentication"""
        self.client.get("/index.html")
 
class WebsiteUser(HttpLocust):
    task_set = UserDefinedTask
    min_wait=5000
    max_wait=9000