Starting Project

Prerequisites

    - Python 3.11.8
    - pip 24.0
    - virtualenv (optional)
    

## Installation

### Enviroment (optional)

For the python project we recommend use a virtual environment, to keep necessary package under this environment and not under computer environment.
For this, you can create new one on the project folder (ZeBrandsTechnicalTest) and then activate this.

```bash
virtualenv env_name
source env_name/bin/activate
```
### Necessary Packages

To get all package for project, you can run the next command. The requirement.txt file contains all package used.

```bash
pip install -r requirement.txt
```

### Database

Use the given script in the main folder (ZeBrandsTechnicalTest), init.sql to create database and populate with first admin. This command will create db_zebrands in main folder.

```bash
sqlite3 db_zebrands < init.sql
```

For this admin the credential will be:
```
email: tpogacar@giro.it
password: defaultadmin
```
This admin can't be deleted, because is protected has 'superadmin', you can create other user (admins) and deleted to.

## Running Project

The project is structured by microservice architecture, we have to microservice: 
* products
* users

### Start microservices

Both microservices are running by the same way, the only difference are the port used to run. You need stay in the main folder of each ms to run the project.

#### MS users
```bash
users % python -m uvicorn main:app --reload --port 8010
```
#### MS products
```bash
products % python -m uvicorn main:app --reload --port 8011
```

## Using Project

For use the project you can use the example postman given, or see the alternative documentation (openapi)
```
users
http://127.0.0.1:8010/docs

products
http://127.0.0.1:8011/docs
```

#### * Only two endpoints are available for all users. This are 'login', to get token and the other is [GET]'products'. For others endpoitns you need use the given token has header, like this:
```bash
x-token:<>value given in the login endpoint>
```


*If you change ms users port, don't forget change this inside of env file in the products microservices.
## RoadMap
For the given challenge not all the requirement were covered. The CRUD for users and product are in state DONE. About the notifications to other admins, is in state PENDING. 

### TODO - Pending task and optional requirement to improve the project.

### Functionalities Requirements
1. Implements the notification to other user, when we change product data. For this, is recommended create other microservice for this logic. 
In this ms whe can use some 3rd party has gmail, SES or Salesforce for example.
2. Improve list of product through pagination, adding some filters has limit and page

### Technicals Requirements
1. Implement better authentication, maybe with 3rd party service as cognito. With this service, and the SDK of Amazon 'boto3', you can scale this to more robust solution.
2. Create some script, maybe a shell-script, to initialize and run all project (both ms) with only one command.
3. Install some package to retrieve the coverage of code, or some report about this. This can be a option https://coverage.readthedocs.io/
4. Add test to cover services, database, and config layers.
5. Move the envs, specially the keys, to some cloud repository for better confidentiality