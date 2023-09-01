![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![Makefile](https://img.shields.io/badge/Makefile-FF0033?style=for-the-badge&logo=gnu%20make&)
![Flake8](https://img.shields.io/badge/Flake8-FFA500?style=for-the-badge&logo=python&logoColor=white)
![pre-commit](https://img.shields.io/badge/pre--commit-FAB040?style=for-the-badge&logo=pre-commit&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-232F3E?style=for-the-badge&logo=amazon-aws&logoColor=white)


## To run the project

#### Create and feel the .env file
```
DB_ENGINE=<...> # specify that we work with postgresql data base
DB_NAME=<...> # data base name
DB_USER=<...> # login for connecting to data base
DB_PASSWORD=<...> # password for connection to data base (create your own)
DB_HOST=<...> # name of the servise (container)
DB_PORT=<...> # port for conection to data base
SECRET_KEY=<...> # set up SECRET_KEY for django project
TEST_DB_NAME=<..> # specify that we work with postgresql test data base
```

#### To run project
```commandline
make run
```
#### To stop and delete all data in container
```commandline
make down
```

## Server will be available at address: http://localhost:8000/