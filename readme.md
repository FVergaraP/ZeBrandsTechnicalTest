# Starting Project

## Prerequisites

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
email: fco.vergara.pena@gmail.com
password: defaultadmin
```
This admin can't be deleted, because is protected has 'superadmin', you can create other user (admins) and deleted to.

## Running Project

The project is structured by microservice architecture, we have this microservice: 
* products
* users
* notifications

### Start microservices

Microservices are running by the same way, the only difference are the port used to run. You need stay in the main folder of each ms to run the project.

#### MS users
```bash
users % python -m uvicorn main:app --reload --port 8010
```
#### MS products
```bash
products % python -m uvicorn main:app --reload --port 8011
```

#### MS notifications
```bash
notifications % python -m uvicorn main:app --reload --port 8012
```

## Using Project

For use the project you can use the example postman given, or see the alternative documentation (openapi)
```
users
http://127.0.0.1:8010/docs

products
http://127.0.0.1:8011/docs

notifications
http://127.0.0.1:8012/docs
```

#### * Only two endpoints are available for all users. This are 'login', to get token and the other is [GET]'products'. For others endpoitns you need use the given token has header, like this:
```bash
x-token:<>value given in the login endpoint>
```

#### Considerations for notification services
```
You can use the credentials provided for AWS, but these are limited to SandBox mode for SES. You can use your own credentials, editing them in the variables of the notifications microservice.
SandBox mode (non-productive) limits mail sending to verified addresses only. If you want to send emails to new addresses, you must contact the owner of the repository (AWS credentials) or manage your own credentials.
```

*If you change ms users port, don't forget change this inside of env file in the products microservices.
## RoadMap

### Pending task and optional requirement to improve the project.

### Functionalities Requirements
1. Upgrade SES servie from SANDBOX mode to Production mode, with this we can send emails without email's verifications
2. Improve list of product through pagination, adding some filters has limit and page

### Technicals Requirements
1. Implement better authentication, maybe with 3rd party service as cognito. With this service, and the SDK of Amazon 'boto3', you can scale this to more robust solution.
2. Create some script, maybe a shell-script, to initialize and run all project (both ms) with only one command.
3. Install some package to retrieve the coverage of code, or some report about this. This can be a option https://coverage.readthedocs.io/
4. Add test to cover services, database, and config layers.
5. Move database to MySql or other robust database
5. Move the envs, specially the keys, to some cloud repository for better confidentiality, has vault
6. Implements docker or other system container, for microservice and database (Ref: https://fastapi.tiangolo.com/deployment/docker/).