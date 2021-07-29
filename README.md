# Portfolio Site
Django based single page portfolio site

## Features
Github project links, Download Resume

## Requirements
Django==3.2<br/>
Mysql==8.0.25 (or any other relational database of your choice)<br/>
mysqlclient==2.0.3 (python database connector of your respective relational database)
Pillow==8.3.1

## Installation
```javascript
git clone https://github.com/him4lik/Portfolio
```
### Initial Setup
#### Database settings(portfolio/settings.py)
Replace values of ENGINE, NAME, USER, PASSWORD according to your database
```javascript
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'database_name',
        'USER': 'database_user',
        'PASSWORD': 'database_user_password',
    }
}
```
After this makemigrations and migrate them
```javascript
python manage.py makemigrations
python manage.py migrate
```
#### Database data insertion
Run Server, Go to '/admin/' and create 'Infos' and 'Project' models


## In Action
![him7](https://user-images.githubusercontent.com/75934883/127551050-84167222-b26d-4046-9d21-384ff0808f1b.gif)

