# ITMD 513 Final Project
### Introduction
This is a Django web application that displays crime rate statistics. It allows users to query statistical charts of criminal records based on latitude and longitude. Additionally, the application provides user login authentication, registration, and management functions.
### Contributors
- Gengxin Li (A20478998) - gli41@hawk.iit.edu
- Qiyun Zhu (A20479136) - qzhu20@hawk.iit.edu
### Main Functions
1. Querying statistical charts of criminal records according to latitude and longitude
2. User login authentication, registration, and management functions
### Technical Summary
The web application is developed using Django as a web service, and it utilizes Django's built-in authentication module for user management. The front-end development is done using the crispy and bootstrap4 frameworks to create a user-friendly interface.
For generating statistical charts, Pandas and Matplotlib are used. The generated image data is not saved but is returned directly by http to display on the website.
### How to Run
1. Install dependent packages (Note: Before running these commands, make sure you have Python installed on your system):
```
python -m pip install requests
python -m pip install pandas
python -m pip install matplotlib
python -m pip install django
python -m pip install django-crispy-forms
python -m pip install crispy-bootstrap4
pip install nltk
pip install scikit-learn
```
2. To run the web server, navigate to the project directory using the command line, and then execute the following command:
```
python manage.py runserver
```
3. Visit the site:
```
http://127.0.0.1:8000/
```
4. Test Data:
Use the following latitude and longitude values for testing:
```
Latitude: 41.937378
Longitude: -87.660078
Latitude: 41.931409
Longitude: -87.651198
```