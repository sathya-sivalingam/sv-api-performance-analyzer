from locust import HttpUser, task, between

class APIUser(HttpUser):
    wait_time = between(1, 2)

    @task(3)
    def test_endpoint(self):
        self.client.get("/test")

    @task(1)
    def heavy_endpoint(self):
        self.client.get("/heavy")
