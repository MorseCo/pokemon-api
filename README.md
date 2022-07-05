## Initial Setup
There are 3 versions of the Pokemon API.
 1. pokemonAPI.py - The base application, which has no security measures in place
 2. pokemonAPI-auth.py - The version of the application that requires a user to be authenticated in order to hit the endpoints
 3. pokemonAPI-limited.py - The final version of the application. This version has authentication enabled, and request limiting enabled.

 To run the applications, you should have python installed, and a fresh virtual environment set up. You can then run: 

 ```
 pip install -r requirements.txt
 ```

 After this installs, you will need to tell Flask which application you would like to run. If you want to run the first app, then run this command:

 ```
 export FLASK_APP=pokemonAPI.py
 ```

 You can then run `flask run` to start your application. You can use a postman, or the UI to interact with it.


## Filling the local monogdb

If you would like to run this locally I have included a file called `pokeScraper.py` that will allow you scrape the PokeAPI, and fill your local mongo database. If you have mongoDB running locally, you can run this script and it will automatically fill your database with necessary data for the Pokemon API.

## DOS Attack

I have included this file so you can perform a DOS attack against the locally hosted application. It's a simple for loop that will count the number of successful and failed responses that the API has returned. You can modify the `requestCount` variable to change the amount of iterations of the loop.

