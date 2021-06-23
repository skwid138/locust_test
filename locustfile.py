import time
from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    # Wait between 1 - 2.5 seconds after each task
    wait_time = between(1, 2.5)

    # Home
    @task
    def home(self):
        self.client.get("/")

    # TODO: Add weights maybe based of GA?

    # Cats
    @task
    def cats(self):
        paths = ['employment-law', 'people-management', 'workplace-communication', 'office-administration']
        for path in paths:
            # Group all of these under the same name
            self.client.get(f"/{path}/", name="/\%categories\%/")
            time.sleep(1)

    # Products
    @task
    def free_products(self):
        self.client.get("/free-products/")

    @task
    def pro_products(self):
        self.client.get("/pro-products/")
    
    @task
    def subscribe(self):
        self.client.get("/subscribe/")

    @task
    def articles(self):
        self.client.get("/articles/")

    @task
    def sponsorships(self):
        self.client.get("/sponsorships/")

    @task
    def about_us(self):
        self.client.get("/about-us/")

    @task
    def posts(self):
        paths = ['/63461/test-post-ian/', '/63470/test-terminations-making-a-difficult-conversation-easier/', '/63235/summer-dress-codes-inclusive-policies-for-warm-weather/']
        for path in paths:
            # Group all of these under the same name
            self.client.get(f"/{path}/", name="/\%post_id\%/\%post_title\%/")
            time.sleep(1)

    @task
    def post_pdfs(self):
        paths = ['/63461/test-post-ian/pdf/', '/63470/test-terminations-making-a-difficult-conversation-easier/pdf/', '/63235/summer-dress-codes-inclusive-policies-for-warm-weather/pdf/']
        for path in paths:
            # Group all of these under the same name
            self.client.get(f"/{path}/", name="/\%post_id\%/\%post_title\%/pdf/")
            time.sleep(1)


    # This task has a weight assidnged to it, making it (in this case) 3 times more likley to be called than the task without a weight 
    #@task(3)
    #def view_items(self):
        #for item_id in range(10):
            # Even though this will make 10 different requests the name param below will group all of them under "/item"
            #self.client.get(f"/item?id={item_id}", name="/item")
            #time.sleep(1)

    # This method does not have the @task decorator so it will not be randomly picked to execute by locust
    # on_start will run for each simulated user when they start
    #def on_start(self):
        #self.client.post("/login", json={"username":"foo", "password":"bar"})
