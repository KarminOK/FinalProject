# ITMD 513 FinalProject
### use a django website to display crime rate statics

## contributors:
Gengxin Li A20478998 
gli41@hawk.iit.edu


Qiyun Zhu A20479136 
qzhu20@hawk.iit.edu


### Main Functions:
Function of querying statistical charts of criminal records according to latitude and longitude
User login authentication, registration, management functions

### Technical Summary:
Use Django as a web service, use the auth module that comes with Django for user management. Use crispy and bootstrap4 for web development. Use Pandas and Matplotlib to generate statistical charts, the generated image data is not saved, and returned directly by http.

### how to run
1. install dependent packages:  
```
python -m pip install requests
python -m pip install pandas
python -m pip install matplotlib
python -m pip install django
python -m pip install django-crispy-forms
python -m pip install crispy-bootstrap4
```
Note: Before running these commands, make sure you have Python installed on your system.

2. run web server:
```
Note: To run the web server, navigate to the project directory using the command line, and then execute the following command:
python manage.py runserver
```

3. visit the site:
```
 http://127.0.0.1:8000/
```

4. test data:
```
 41.937378   -87.660078    41.931409   -87.651198
```