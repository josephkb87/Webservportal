# F.A.R.M Stack WebPortal 

Disclaimer:
1. `` This README file is susceptible to repetitions/misinterpretations and incorrect syntax or semantics in code and flow of execution. It is the aim of this work that you try where you can, make corrections. If you are reading or working with this. Please clean it up.`` 

2. `` This project was built using Open Source Software tools.The code, examples and materials and software tools in this project are solely for purposes of my academic Thesis.``

This is the original README.md of the Webservportal [README.md](/Webservportalproject/docs/README.md).

## Problem Statement

Citizens of Country A are moving from an analogue systems and services provision to a new digital services and systems provisioning system.
In order to have a streamlined means of services provision from the government, there is a requirement for a WebServices Portal, 
where the citizens can utilise the services and the government administrators  using the new digital services provisioning system.

This project is a simple web services portal that aims to serve that purpose.

### Project Description
This web services portal is a ```government web services portal``` for citizen access to services of the different government entities and ministries.
````It consists of an login and administrative dashboard where government administrators and citizens can access services of the different government Ministries````

 ### WebServicesPortal
This ´´[WebServicesPortal Project](#addlinkhere)`` work is apart of [Thesis](../yourprofile?tab=projects?tab=Thesis).

### Stack

* This Project was build using the [F.A.R.M](https://www.freecodecamp.org/news/learn-the-farm-stack-fastapi-reactjs-mongodb/) 
`` The FARM stack is FastAPI, React, and MongoDB. F.A.R.M stands for -The FastAPI, ASGI,React,MongoDB ``
- [web framework](#) - FastAPI for the back end.
- [Web Server](#) - ASGI for the Web Server
- [User admin and Registration](#) - React for the front end.
- [User admin and Registration](#) - FastAPI_Users for the Back end.
- [Backend Database](#)- NoSQL[MongoDB](#) VS [SQL](#) Databases.
- [Beanie ODM for Mongodb Backend Database](#) -  or [SQLAlchemy for SQLBackend Database](#)


## Setup
WebServicePortal [README.md](./Webservportalproject/docs/README.md)

SetUp / Install

#### Manual Setup

````
$ mkdir FARMStack
$ cd FARMStack
$ mkdir webservportal
$ cd webservportal
$ mkdir backEnd
$ mkdir frontend
cd frontend
$ code .
$ git init
$ yarn create react-app frontend --template react-bootstrap
$ cd backEnd
$ git init
$ touch requirements.txt main.py model.py database.py
````

#### Flow of Execution
For the Stack to work accordingly, the order in which statements are executed,we must first have a working/Provisioned .Backend so that the frontend is implemented.
This is because the frontend depends on the backend to implement the whole stack.


### Setup Requirements
We will requireThe following ;
* [VSCode/Pycharm/IDE](./requirements.txt")
* [Python](./requirements.txt")
* [Mongodb Server](./requirements.txt")
* [dependencies](./requirements.txt") are required.


#### BackEnds

#### Mongodb BackEnds

#### Database Setup
Create database and add data documents
* Download from Mongodb 
  - Community Monogodb Setup 
  - MOngodbAtlas Connector
* Login to mongodbaccount
* Connect Your Mongodb account + MOngodbAtlas Connector to localhost

#### Insert Data Documents
We will utilise MongoDB documentation to [Insert Data into the database](https://www.mongodb.com/docs/compass/current/documents/insert/)

#### What does it Do?
* The backend authenticates and users to the database.
* This is done by connecting the app backends to the database.
This FARM Stack Implementation of a government services portal.For citizens and officials for service provision.

#### How does it work?
* Consists of login & Registration Portal for Government Officials and Citizens where each serves a function or purpose for service delivery.
Officials have access to a services portal and citizens also.
Once logged in each user has a dashboard.

## Parts
* Database Setup
* Customizable database backend because we are using MongoDB DB and NOT SQLAlchemy, we will use MongoDB with Beanie ODM included and not ORM async included.
* JWT Authentication


#### Development
* Backend

 - [Web Framework](#addlinkhere).

- [Web Framework](#addlinkhere) :We will use  FastAPI as both our backend and also our Webframework to build the webservportal app.
``FastAPI is a modern, fast (high-pe)rformance), web framework for building APIs with Python 3.7+ based on standard Python-type hints. One of the key features of FastAPI is its ability to use the latest Python features, such as async/await, without requiring developers to write boilerplate code.``

- [ASGI](#addlinkhere) :Asynchronous Server Gateway Interface.
  ``Asynchronous Server Gateway Interface,is a standard interface between web servers and Python web applications or frameworks``

 - [User Login & Authentication](https://fastapi-users.github.io/fastapi-users) - [FastApiUser](#): We will use FastApiUser for login authentication and management because it also provides us OAuth2 authentication.FastAPI Users also allows you to plug in several authentication methods.FastAPI also allows us to have a customizable database backend, where SQLAlchemy ORM async included
     and MongoDB with Beanie ODM also included.This helps us to customize our database backend if we have them.
``FastAPIUsers is a highly secure and open-source users management registration and authentication system for Implementing registration, login, social auth.``

* Frontend

- [Node.js](#) + [React](https://create-react-app.dev/docs/getting-started/)  
We will utilise the [react-create template](https://create-react-app.dev/docs/getting-started/) to instatiate our frontend.

#### Why React for FrontEnd?
Create React App is an officially supported way to create single-page React applications.
It offers a modern build setup with no configuration.


####  Building, Testing, and Deployment
[Gradle](https://docs.gradle.org/current/userguide/gradle_basics.html) automates building, testing, and deployment of software from information in build scripts.

#### Build


For Building our app - [Cmake](#)

## Testing


#### API Testing 
For our API Testing, we will use Postman for API testing of our API. 

#### Deployments
-- NginxUnit - To run our web apps. 

#### Backend


#### FrontEnd.
The fundamental way the frontend frameworks interact with the backend is by making [HTTP calls](##) via [AJAX](##).
The typical interface to the backend is a REST API.


#### Project Status
- [ ] Design

- [ ] MockUps

- [x] Development

+ Backend Design  & build(React + FastAPI Users)
  - Login and Authentication
  - MongoDB Integrations
  
+ Frontend Design  & build(React + FastAPI Users)
  - App Testing

- [x] Unit Testing

- [x] QA

- [ ] Stage

- [ ] Beta Testing

- [ ] Production

#### Documentation

For source [Documentation](.../docs/sphinxdocs/docs/build) including our API,
[Sphinx](#), [Redoc](#), [FAST API Docs](#) were utilised.

* [README.md](...docs/README.md) .
* [Changelog](.../docs/CHANGELOG.md) .
* [Documentation] (.../docs/sphinxdocs/docs/build)
* [Documentation Build] (...D:/FARMStack/Webservportalproject/docs/sphinxdocs/)


#### References
 Reference Literature is in the [References.md](./docs/References.md)


#### Links

** [BuildStructure.md](./docs/buildstructure.md)  for the project utilised the self contained waterfall structure.[Build Structure](...docs/buildStructure.md) is NOT the [Project Structure](...docs/ProjectStructure.md)

** [Project Structure](...docs/ProjectStructure.md)

** [Flow of Execution](...docs/flowofexecution.md)

**[Build Structure](...docs/buildStructure.md)


#### Privacy
[Privacy Policy](../docs/privacy.md)

#### Attribution(s)
This project utilises open and closed source tools.
This work would not exist without the following [Attribution(s)](../docs/attributions.md)

#### LICENSE(s)
Licenses are in the [LICENSE(s)](../docs/LICENSE) directory.

#### [Contribute](..docs/Contributing.md)

Feel free to  tell me  if you liked this project or 
how it helped you out! [here](#addlinkhere/)



Made with :[heart][heart] [Sphinx docs](https://www.sphinx-doc.org/)

