from locust import HttpLocust, TaskSet, task
from requests.auth import HTTPBasicAuth
 
def http_basic_auth(self,uri)
        self.client.post(uri,auth=HTTPBasicAuth("username", "Password"))
 
class UserDefinedTask(TaskSet):
    def on_start(self):
        """ call when locust start i.e before exection of tasks"""
 
    @task(2)
    def home(self):
        self.client.get("/")
 
    @task(1)
    def about(self):
 """load testing on page containing http_basic_authentication"""
        http_basic_auth(self,”/about/”)
 
class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait=5000
    max_wait=9000