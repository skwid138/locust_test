# Setup

* Install Python 3.6 or later
  * `brew install python` This will install python 3.9.*
  * Update $PATH to avoid using macOS python 2.7.* 
    * Add the following to ~/.bashrc or ~/.bash_profile or ~/.zashrc etc.
    ```
    ## Make brew managed Python override the system default 2.7.*  ##
    export PATH="/usr/local/opt/python/libexec/bin:$PATH"
    ```
* Install Locust `pip3 install locust`
* Confirm Locust installed `locust -v`, this should output the currently installed locust version

# Use

* In terminal navigate to the repo root where locustfile.py resides
* Run locust with the config `locust`
  * Alternativly you may specify the config location with `locust -f locust_files/my_locust_file.py`
* In a browser navigate to [http://127.0.0.1:8089](http://127.0.0.1:8089) or [http://localhost:8089/](http://localhost:8089/)
* Input the Number of users to sim as well as how many users to spawn per second
* Input the host to run on (the config here is specifically designed for a unique host)
* Click `Start swarming`

## Swarm

A single instance seems to be fairly limitied in it's capacity so using multiple instances chained together appears to be best.

- Start a single mastert instance `locust --master --expect-workers=[number of workers here]`
- In a new terminal run `locust --worker --master-host=localhost` 
  - If the host is not localhose update to use the appropriate IP

Notes: 

I noticed that 1 master and 27 workers seemed to be enough to handle 8k users with 50/sec spawn rate, but when I tried 15k with 50/sec it had problems

# Resources

- [Locust Docs](https://docs.locust.io/en/stable/index.html)
- [Most useful for what I was attempting](https://blog.mirumee.com/application-performance-testing-9e6af4439da)
- [ML based, but had decent info](https://www.analyticsvidhya.com/blog/2021/06/performance-testing-ml-serving-apis-with-locust/)
- [This was an entire ecosystem with Locust](https://www.blazemeter.com/blog/locust-monitoring-with-grafana-in-just-fifteen-minutes)
- [Locust Docker](https://hub.docker.com/r/locustio/locust)