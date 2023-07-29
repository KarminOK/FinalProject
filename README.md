# ITMD 513 FinalProject
### use a django website to display crime rate statics

## contributors:
Gengxin Li  
Qiyun Zhu

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
2. run web server:
```
python manage.py runserver
```
3. visit the site: http://127.0.0.1:8000/