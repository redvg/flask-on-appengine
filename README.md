launches a flask server on gcp appengine\
\
extends https://github.com/GoogleCloudPlatform/python-docs-samples/tree/master/appengine/standard/flask/hello_world

## App

main.py:
- flask app

views folder:
- route bindings in respective modules

## Manifest

app.yaml:
- handlers section contains endpoint to script (wsgi or cgi) bindings
- libraries section contains standard env extension, i.e. flask lib

see https://cloud.google.com/appengine/docs/standard/python/config/appref for app manifest \
see https://cloud.google.com/appengine/docs/standard/python/configuration-files for queue, cron and other manifests

## Deploy/Update

```
git clone https://github.com/redvg/flask-on-appengine 
cd flask-on-appengine
gcloud app deploy app.yaml
gcloud app versions list
gcloud app services list
```

visible on http://project-id.appspot.com \
update creates new version

## Test

```
dev_appserver.py ./
```

open 'web preview' \
change or git pull in anoher terminal, development server will detect changes automatically

## Tear down resources

gcp does not support removing the app engine. current solution is to stop the app, disable it and set usage quota to 0. \
this will leave the latest version artifact though. to completely remove it the only solution is to delete the project \

stopping the app: current manifest has autoscaling ON by def, which would yield \
ERROR: (gcloud.app.versions.stop) INVALID_ARGUMENT: serving status cannot be changed for Automatic Scaling versions \
\
to be able to stop alter the manifest for manual scaling
```
manual_scaling:
  instances: 1
```

see https://cloud.google.com/appengine/docs/standard/python/config/appref#scaling_elements \

then update and stop 

```
git pull
gcloud app deploy
gcloud app versions list
gcloud app versions stop
``
