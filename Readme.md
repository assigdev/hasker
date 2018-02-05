# Hasker

## For prodoction

clone repository:

    $ git clone https://github.com/assigdev/hasker
    
install docker and docker-compose for your OS.

Then up docker containers:
  
    $ cd hasker
    $ make prod
    
for configure (migrate, collectstatic and createsuperuser) in another terminal connection

    $ make configure
    

for update collectstatic and migrations

    $ make update

## For dev

clone repository:

    $ git clone https://github.com/assigdev/hasker
    
install docker and docker-compose for your OS.

Then up docker containers:

    $ cd hasker
    $ make dev b=1
    

For next up use

    $ make dev

    
for configure (migrate, collectstatic and createsuperuser) in another terminal connection

    $ make configure

## For dev with sqlite without docker containers

clone repository:

    $ git clone https://github.com/assigdev/hasker
    
Then up django dev server:

    $ cd hasker
    $ make dev_easy b=1
    
For next up use
    
    $ make dev_easy

other manage commands:

    $ pipenv run python manage.py *command*

    