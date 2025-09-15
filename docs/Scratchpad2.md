Scratchpad

# About

This scratchpad exists as evidence for purposes of documenting the steps and processes of this work. Alot of ideas and information exists here.I choose to add it here for purposes of design, ideation and build of this project.It is possible parts of it to be missing, removed or changed from time to time for personal reasons by the [AUTHORS](#).

#### Build Structure

This project was build using the self contained(monolith) waterfall [Build Structure](./docs/buildstructure.md)

## Flow of Execution

#### Backend vs FrontEnd.

The fundamental way the frontend frameworks interact with the backend is by making HTTP calls via AJAX. The typical interface to the backend is a REST API

#### Database

PostgreSQL and SQLite are two relation databases, SQLAlchemy is an [ORM](##addlinkhere) which gives you a set of tools for accessing the data in the database.

While [SQLAlchemy](#addlinkhere) is the Python SQL toolkit and Object Relational Mapper that gives us the full power and flexibility of SQL, we will use [Beanie](#addlinkhere) as it works with [MONGODB](#addlinkhere),as it is the database we will use and is an Object Document Mapper that gives application developers the full power and flexibility of a NoSQL Database.

## Testing and Building

#### Testing

FastAPI is an API;that we use or create a tool that would simplify the API testing process. We will utilise [Postman](https://en.wikipedia.org/wiki/Postman_(software)) for testing the app, and all its functionality because Postman is an API platform for building and using APIs that simplifies each step of the API lifecycle.

all the run tests uploaded to the testing directory.

\[/coverage\]

## Production

\[/build\]

#### [Deployments](https://fastapi.tiangolo.com/deployment/)

To deploy an application means to perform the necessary steps to make it available to the users. For a web API, it normally involves putting it in a remote machine, with a server program that provides good performance, stability, etc, so that your users can access the application efficiently and without interruptions or problems. This is in contrast to the development stages, where we are constantly changing the code, breaking it and fixing it, stopping and restarting the development server, etc.

Deploying a FastAPI application is relatively easy.

#### Deployment Strategies

Depending on our specific use case and the tools that we use.when deploying a FastAPI application (although most of it applies to any other type of web application).

-   We could deploy a server ourselves(Local Deployment) using a combination of tools, or
-   We could use a [cloud service](#addlinkshere) and make a cloud deployment that does part of the work for us, or other possible options.

#### Cloud Deployment

Cloud Deployment with [linode-deploy-gunicorn-uvicorn-nginx](https://christophergs.com/tutorials/ultimate-fastapi-tutorial-pt-6b-linode-deploy-gunicorn-uvicorn-nginx/)

#### Local Deployment

-- Requirements for Local Deployment + [nginx-unit](https://unit.nginx.org/howto/fastapi/) : Nginx-unit is a Fast API + [VirtualBox](#) : Virtual Box is a tool that is used to setup a virtual workspace using images + [Vagrant](#addvagrantlinkshere) Vagrant is a tool for building and distributing development environments-

#### References

[Generate Gitignore Files](#addlinkhere)

[Build a FARM Stack](#addlinkhere).

[FASTAPI](#addlinkhere)

[API documentation](https://github.com/swagger-api/swagger-ui)

[Pydantic Utilised Models](https://docs.pydantic.dev/latest/concepts/models/)

[Swagger-UI](https://github.com/swagger-api/swagger-ui) \* Swagger UI is a collection of HTML, JavaScript, and CSS assets; \* That dynamically generate beautiful documentation from a Swagger-compliant API.

[Auth Login Page](https://dev.to/athulcajay/fastapi-auth-login-page-48po) [Micro Frontends](https://www.telerik.com/blogs/building-micro-frontends)

[FastApiUsers](https://fastapi-users.github.io/fastapi-users)

-   [Dash Framework for Python](http://www.dash.plotly.com)

-   [Getting-started](https://create-react-app.dev/docs/getting-started/)

-   [Create-React-App](https://github.com/facebook/create-react-app)

-   [Create React Front End](https://christophergs.com/tutorials/ultimate-fastapi-tutorial-pt-12-react-js-frontend/#theory)

#### [Provisioning]

-   [Automated](#)

-   [Manual](#)

#### [Deployments](https://fastapi.tiangolo.com/deployment/)

Deploying our FastAPI application is relatively easy.

#### Deployment Strategies

#### Cloud Deploy - Here we use a cloud service that does part of the deployment for us, or other possible options.

-   [Cloud Deploy using Linode](https://christophergs.com/tutorials/ultimate-fastapi-tutorial-pt-6b-linode-deploy-gunicorn-uvicorn-nginx/)

#### Local Deploy.

We deploy a server ourselves using a combination of tools)

Requirements + [vagrant](https://github.com/hashicorp/vagrant) + + [install vagrant](https://developer.hashicorp.com/vagrant/install) + + [nginx-unit](https://unit.nginx.org/howto/fastapi/) + + [VirtualBox](#)

#### Integrations

-   [Unit](https://unit.nginx.org/howto/integration/)

[Data Visualisation with dash](https://dash.plotly.com/)

#### Documentation

#### [Redoc API Documentation](https://github.com/Redocly/redoc)

#### [Pycharm Documentation](https://www.jetbrains.com/help/pycharm/set-up-a-git-repository.html)

#### [sqlalchemy](https://www.sqlalchemy.org/)