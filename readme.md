Starting Project

Prerequisites [TODO]

    - Python 3.11
    - Sqlite
    - add requirement
    -

## Installation
### Project

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install requirement.txt
```

### Database

Use the given script, init.sql to create database and populate with first admin. For this admin the credential will be:
```
email: TODO
password: TODO
```
If you want change password, do it with hash password [TODO] link to hash online maybe

```bash
sqlite3 db_zebrands < init.sql
```

## RoadMap
### TODO
* Implement better authentication, maybe with 3rd party service as cognito
* send env to env file
* make script to run all microservice
* make postman with documentation, better than swagger
* update databse with new field "superadmin" and init script
* implement tests