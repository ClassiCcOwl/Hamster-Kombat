# Hamster Kombat API

This is a non-official api for getting hamster kombats cards information. For testing this out check [Hamster Kombat API](https://api.boardingle.ir/) 

## A restful API for Hamster Kombat

- get categories list
- get cards list
- get cards levels information


## Instalation for testing


Clone the project. This will download the GitHub respository files onto your local machine.

```Shell
git clone https://github.com/ClassiCcOwl/Hamster-Kombat.git
```

installing virtual enviroment and activating:

```Shell
pip install virtualenv
```
Windows setup:

```Shell
#creating the enviroment
python -m venv venv

#activating the enviroment
venv\Scripts\activate

#deactivating enviroment
deactivate
```
Linux and Mac setup:
```Shell
#creating the enviroment
python -m venv venv

#activating the enviroment
source venv/bin/activate

#deactivating enviroment
deactivate
```


then installing the requirements:

```Shell
pip install -r requirements_local.txt
```
rename .env.example file into .env and set required fileds

run migrations

```Shell
python manage.py makemigrations
python manage.py migrate
```

default and development settings
```Shell
python manage.py runserver 
```

## TODO

- [x] Create custom user
- [x] Create category model
- [x] Create card model
- [x] Create level model
- [x] Create apis
- [X] Insert data
- [X] Create card crwaler
- [X] Create level crwaler
- [X] Add daily combos
- [X] Add category ordering
- [X] Add cards order
- [X] Add auth
- [X] Add cards with level to profile
- [ ] Add level up and level down apo
- [ ] Add ranking
- [ ] Handel bad / failed requests for adding cards or update level
- [ ] Add cache
- [ ] Add morse code daily
- [ ] Run crawlers in perodic time with celery