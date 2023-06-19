# timezync
Worklog management tool written in python


# Guide
* https://www.digitalocean.com/community/tutorials/how-to-structure-a-large-flask-application-with-flask-blueprints-and-flask-sqlalchemy

## Reference
* [Flask](https://flask.palletsprojects.com/en/2.3.x/)
* [REST](https://flask-restful.readthedocs.io/en/latest/)
* [Migration](https://flask-migrate.readthedocs.io/en/latest/)
* [Flask Marshmellow](https://www.google.com/search?q=flask+marshmallow&oq=flask+mar&aqs=chrome.0.0i512j69i57j0i512l5j69i65.1551j0j4&sourceid=chrome&ie=UTF-8)



## Migration Limitations
We are using Alembic for the database migtations via flask-migrate plugin. Alembic is not always able to detect every change you make to your models. In particular, Alembic is currently unable to detect 
* table name changes
* column name changes
* anonymously named constraints


[A detailed summary of limitations can be found here](https://alembic.sqlalchemy.org/en/latest/autogenerate.html#what-does-autogenerate-detect-and-what-does-it-not-detect)



## Migrations

init migrations with 
```
flask db init
```

You can then generate an initial migration:
```
flask db migrate -m "Initial migration."
```

Each time the database models change, repeat the migrate and upgrade commands.
```
 flask db upgrade
```
