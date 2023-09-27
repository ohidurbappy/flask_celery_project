

## Run the project with docker

```bash
docker-compose up
```

### Create the database

```python
def createMyDatabase():
    from project import db, create_app
    db.create_all(app,_=create_app())
```