# Setup

## Django

create virtual environment `venv` and activate it

    virtualnev venv
    source venv/bin/activate

Create file `config.ini` inside `venv` with following structure

    [django]
    SECRET_KEY:<long random string>
    HOST:blog.mukulsingh.in

Create directory for static files

    mkdir static

Initiate django

    ./manage.py migrate
    ./manage.py collectstatic

Install sass and run
```
sass --watch generaltech/scss:generaltech/static/css --style compressed
```

Run server
```
python manage.py runserver --settings=generaltech.settings_dev
```