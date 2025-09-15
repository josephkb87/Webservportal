### WebServicesPortal

#### Disclaimer
``This project was built in the Open using Open Source Software tools.
``
``The code, examples and materials and software tools in this project are solely for purposes of my academic Thesis.``

### Problem Statement
Citizens of Cameroon are moving from an analogue systems and services provision to a new digital services and systems provisioning system.
In order to have a streamlined means of services provision from the government, there is a requirement for a WebServices Portal, 
where the citizens can utilise the services and the government administrators  using the new digital services provisioning system.

This project is a simple web services portal that aims to serve that purpose.

### Project Description
This web services portal is a ```government web services portal``` for citizen access to services of the different government entities and ministries.
````It consists of an login and administrative dashboard where government administrators and citizens can access services of the different government Ministries````

 ### Project Name
This ´´[WebServicesPortal](#addlinkher)`` work is apart of [Thesis](../profile?tab=projects).

### Stack

* This Project was build using the [F.A.R.M](https://www.freecodecamp.org/news/learn-the-farm-stack-fastapi-reactjs-mongodb/) Stack.
``The FARM stack is FastAPI, React, and MongoDB. F.A.R.M stands for -The FastAPI, ASGI,React,MongoDB``
- [web framework](#) - FastAPI for the back end.
- [Web Server](#) - ASGI for the Web Server
- [User admin and Registration](#) - React for the front end.
- [User admin and Registration](#) - FastAPI_Users for the Back end.
- [Backend Database](#)- MongoDB.

### Requirements
We will require the following for;
#### Development
** Backend
 - [Web Framework](FastAPI).
[Web Framework](addlinkhere) :We will use  FastAPI as both our backend and also our Webframework to build the webservportal app.
   ``FastAPI is a modern, fast (high-pe)rformance), web framework for building APIs with Python 3.7+ based on standard Python-type hints. One of the key features of FastAPI is its ability to use the latest Python features, such as async/await, without requiring developers to write boilerplate code.``
 - [ASGI](#addlinkhere) :Asynchronous Server Gateway Interface.
  ``Asynchronous Server Gateway Interface,is a standard interface between web servers and Python web applications or frameworks``

 - [User Login & Authentication](https://fastapi-users.github.io/fastapi-users) - [FastApiUser](#): We will use FastApiUser for login authentication and management because it also provides us OAuth2 authentication.FastAPI Users also allows you to plug in several authentication methods.FastAPI also allows us to have a customizable database backend, where SQLAlchemy ORM async included
     and MongoDB with Beanie ODM also included.This helps us to customize our database backend if we have them.
     ``FastAPIUsers is a highly secure and open-source users management registration and authentication system for Implementing registration, login, social auth.``

** Frontend
- [Node.js](#) + [React](#)  

** Database
- For user registration and authentication database - [Mongodb](#)

#### Build
For Building our app - [Cmake](#)

#### Testing 
For testing - Postman

#### Deployments
-- NginxUnit - To run our web apps. 

## Manual Setup

````
$ mkdir FARMStack
$ cd FARMStack
$ mkdir webservportal
$ code .
$ git init
$ yarn create react-app frontend --template typescript
$ cd webservportal
$ git init
$ touch requirements.txt main.py model.py database.py
````
## Flow of Execution
For the Stack to work accordingly, we must first have a working/Provisioned 
Backend so that the frontend is implemented.
This is because the frontend depends on the backend to implement the whole stack.

#### Backend vs FrontEnd.
The fundamental way the frontend frameworks interact with the backend is by making HTTP calls via AJAX.
The typical interface to the backend is a REST API.


### Project Status

- [ ] Design
- [ ] MockUps
- [x] Development
+ Backend Design  & build (FastAPI + ASGI)
  - Login and Authentication
  - MongoDB Integrations
  
+ Frontend Design  & build(React + FastAPI Users)
  - App Testing

- [x] Unit Testing

- [x] QA

- [ ] Stage

- [ ] Beta Testing

- [ ] Production

* [Documentation](#addlinkhere) We will use [Sphinx](#),and [Redoc](#) AND [FAST API Docs](#) will For source documentation including our API, we will use :

### Documentation
Documentation for the project is [found here](../readthedocs).

### References/Literature
Reference literature is found in the [references](../docs/references.md)

### Privacy
[Privacy Policy](../docs/privacy.md)

### Attribution(s)
This project utilises open and closed source tools.
This work would not exist without the following [Attribution(s)](../docs/attributions.md)

### LICENSE(s)
Licenses are in the [LICENSE(s)](../docs/LICENSE) directory.

### [Contribute](..docs/Contributing.md)

Feel free to  tell me  if you liked this project or 
how it helped you out! [here](#addlinkhere/)

### 