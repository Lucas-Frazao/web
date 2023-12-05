# Repository for a web app that will track service hours for clubs at my school. 

## Below is an explanation for each of the files in this web app and what their intended purposes are:

## App
   Templates
   -->This folder will hold html templates that will define the look and feel for each individual web page that is displayed. 
   
   __init__.py
   -->The first file that is called in the entire application. It servers to import the other files and to initialize the application
   
   Forms.py
   -->Define the online forms that will be queued to collect information from a user. (Example: Registration form).
   
   Models.py
   -->Serves to define the database models, or the structure of what the database has to hold
   
   Routes.py
   -->Serves to route the entire application and to set pointers for the URLs
   
## Config.py
Serves to define the secret key that the application uses when communicating. It uses a class to store configuration variables.

## Web.py 
Python script at the top level that defines the Flask application instance. 
