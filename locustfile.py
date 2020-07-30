from locust import HttpUser,task,between,TaskSet
import random

class QuickStart(HttpUser):
    wait_time = between(5,9)

    @task
    def home_page(self):
        self.client.get("/")

    @task(3)
    def view_pages(self):
        #item_id = random.randint(1,500)
        self.client.get("/backendsync")

    def on_start(self):
        self.client.get("sync")