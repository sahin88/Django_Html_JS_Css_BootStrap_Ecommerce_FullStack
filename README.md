# DJango_Html_JS_Css_BootStrap_Ecommerce

## Live Demo [to see leve demo please click](https://ecommerce-webapp-sahin.herokuapp.com)


## Features
  -  Django 3.1.7
  -  PostgreSQL database support with psycopg2.
  -  Bootstrap static files included
  -  Procfile for easy deployments
  -  User registration, logging
  -  Custom User Model

## Uml 
![alt text](https://github.com/sahin88/DJango_Html_JS_Css_BootStrap_Ecommerce/blob/main/ecommerce_uml.png)


## Getting Started
First clone the repository from Github and switch to the new directory:
```
$ git clone git@github.com/sahin88/{{ project_name }}.git
$ cd {{ project_name }}
```
Activate the virtualenv for your project.
```
$ source vit/bin/activate

```
Install project dependencies:
```
$pip install -r requirements.txt

```

Then simply apply the migrations
```
$python manage.py migrate

```

You can now run the development server:
```
$ python manage.py runserver

```



## Heroku

```
$ heroku create
$ heroku addons:add heroku-postgresql: ecommerce
$ heroku buildpacks:set heroku/python
$heroku buildpacks:add --index 1 heroku/nodejs
$ heroku config:set AWS_SECRET_ACCESS_KEY
$ heroku config:set AWS_SECRET_ACCESS_KEY
$ heroku config:set AWS_STORAGE_BUCKET_NAME
$ heroku config:set EMAIL_HOST_USER
$ heroku config:set EMAIL_HOST_PASSWORD 
$ heroku config:set DEBUG
$ heroku config:set SECRET_KEY
```


## Licence
MIT

Copyright (c) 2019-2024 Sahin Murat Ogur

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, 
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
