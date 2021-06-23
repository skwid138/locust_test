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
