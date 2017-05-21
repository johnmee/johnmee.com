# johnmee.com

## How to add pages

I vaguely recall I can just add new files to the `pages` directory and, depending on the yaml data at the top, it will decide whether to publish and what to call it.

## How to update the resume

I see there is a `pandoc.sh`, and in it is some stuff that looks like converting markdown into a word doc.  I reckon that might be useful (for agencies living in the past).

## How to deploy updates

There is a `rundeploy.sh` script.

```
$ cat redeploy.sh | ssh binlane
```

