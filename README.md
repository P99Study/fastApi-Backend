# DEPLOYMENT

## INSTALLATION

1.
```commandline
pip install -r requirements.txt
```

## SERVICE STARTUP

1.
```commandline
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

## SWAGGER URL

1.
```commandline

http://localhost:8000/docs

OR

http://<server ip or domain name>:8000/docs

```


