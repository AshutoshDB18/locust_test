from locust import User, task, between, HttpUser
import subprocess


class MyHttpUser(HttpUser):
    wait_time = between(1, 5)

    weight = 3

    @task
    def get_req(self):
        response = self.client.get("/api/users")
        if response.status_code == 200:
            print("GET request successful")

    @task
    def post_req(self):
        response = self.client.post("/api/users", params={"name":"netcore","job":"ADMIN"})
        if response.status_code == 200:
            print("POST request successful")




class MyScritp(User):
    wait_time = between(1, 5)

    weight = 2

    @task
    def run_hello_script(self):
        result = subprocess.run(["bash", "hello.sh"], check=True)
        if result.returncode != 0:
            print("Error executing script. Stopping execution.")
            return
