1. $ cd backend
2. $ virtualenv venv
3. $ venv\Scripts\activate
4. (venv) $ pip install -r requirements.txt
5. make .env file in /backend and paste the below:
```
    export FLASK_APP="api"
    export FLASK_ENV="development"
```
# List of APIs
get_categories - GET
get_twitter - POST
get_insta - POST
get_fb - POST
get_trends - POST