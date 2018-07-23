launches a flask server on gcp appengine\
\
extends https://github.com/GoogleCloudPlatform/python-docs-samples/tree/master/appengine/standard/flask/hello_world

## App

main.py:
- flask app
- route binding

## Manifest

app.yaml:
- handlers section contains endpoint to function bindings
- libraries section contains standard env extension, i.e. flask lib

see https://cloud.google.com/appengine/docs/standard/python/config/appref for app manifest \
see https://cloud.google.com/appengine/docs/standard/python/configuration-files for queue, cron and other manifests

## Deploy

```
git clone https://github.com/redvg/flask-on-appengine 
cd flask-on-appengine
gcloud app deploy app.yaml
```

visible on http://project-id.appspot.com 


