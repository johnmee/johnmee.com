# johnmee.com

## How to develop

```
$ FLASK_APP=blog.py FLASK_ENV=development FLASK_DEBUG=1 flask run
```

## How to add pages

I vaguely recall I can just add new files to the `pages` directory and, depending on the yaml data at the 
top, it will decide whether to publish and what to call it.

## How to update the resume

I see there is a `pandoc.sh`, and in it is some stuff that looks like converting markdown into a word doc.

## How to deploy updates

There is a `rundeploy.sh` script.

```
$ cat redeploy.sh | ssh binlane
```
