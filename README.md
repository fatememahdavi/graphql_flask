# GraphQl in Flask
sample Project | Python | Flask | GraphQl

## Requirements
- Python3
- PostgreSQL/Sqlite/...
- Pipenv

## Install
```
- pip install pipenv
- pipenv install
- pipenv shell
```

## Usage
- Create .env file, and copy the below configuration.

```
FLASK_DEBUG=1
FLASK_APP=app.py
SECRET_KEY=<YOURSECRETKEY>
LOG_LEVEL = DEBUG
LOG_FILE = project.log
SQLALCHEMY_DATABASE_URI = <SQLALCHEMY_DATABASE_URI>
SQLALCHEMY_COMMIT_ON_TEARDOWN = True
SQLALCHEMY_TRACK_MODIFICATIONS = True
```

- Set Secret_Key,SQLALCHEMY_DATABASE_URI, ... according to your system

 - To run the app:
```
 python app.py
```
 - To view and create queries in the Graphql Apis interface:
```
 {BaseUrl}/graphql-api
```
## Example

