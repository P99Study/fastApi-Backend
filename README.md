# DEPLOYMENT

## INSTALLATION

```commandline
pip install -r requirements.txt
```

## SERVICE STARTUP

```commandline
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

## SWAGGER URL

```commandline

http://localhost:8000/docs

OR

http://<server ip or domain name>:8000/docs

```


