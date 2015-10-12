title: How this website works
published: 2015-10-15
tag: technical


[python]: https://www.python.org/ "Python"
[flask]: http://flask.pocoo.org/ "Flask"
[jinja2]: http://jinja.pocoo.org/docs/ "Jinja2"
[markdown]: http://daringfireball.net/projects/markdown/ "Markdown"
[skeleton]: http://getskeleton.com "Skeleton"
[pygments]: http://pygments.org/ "Pygments"
[yaml]: http://yaml.org/spec/1.1/ "YAML"

# How I built this simple blogging site

This site was hand-built using the [Python programming language][python]:

* the pages are assembled by the microframework [Flask] and templating language [Jinja2]
* the content is composed in prose friendly [Markdown]
* and the code snippets rendered with [Pygments]
* the responsive layout (CSS) is based on [Skeleton]
* there is no database involved&mdash;relational, noSQL, NewSQL, or otherwise
* the webservice stack is [UWSGI](https://uwsgi-docs.readthedocs.org/) and [nginx](http://nginx.org) on an [Ubuntu](http://www.ubuntu.com/) server
* it is hosted on a VPS at [Binary Lane](http://binarylane.com.au/)
* it draws on [disqus](https://disqus.com/) for the commenting
* it draws on [Google Analytics](http://www.google.com.au/analytics/) just in case I bother to check if anyone is reading
* it is committed to [git](https://git-scm.com/) and [github](https://github.com/johnmee/johnmee.com/), 
   usually by commandline but often using [sourcetree](https://www.sourcetreeapp.com/)
* it is developed mostly with [Pycharm](https://www.jetbrains.com/pycharm/), 
   but also [vi](https://en.wikipedia.org/wiki/Vi), and [sublimetext](http://www.sublimetext.com/).
* my desktop is usually [OS X](http://www.apple.com/au/osx/)

## Background Ramble/Requirements

This "vanity" website has gone through more rebuilds than I dare to count.  In some respects it feels like a 
corporate home page the way my interests play tug-of-war over it.  Initially it was, of course, just HTML, then
after various rewrites I _drank the coolaid_ and used WordPress, which was fairly successful in getting me
to post stuff, but thoroughly unportable and unsatifactory for my requirements.

**In some respects it is a CV:**  
My job is, not exclusively but mostly, about building websites (or web `applications` as I prefer to distinguish) and
failing to have a personal website could reflect poorly on my ability, even to those who appreciate how low your
own website can fall on the TODO list.  So the site needs to show I can knock up a working website that looks reasonably
current, can carry a resum&eacute; simple enough for the technically challenged recruitment agents to work with, 
yet blingy enough to impress the potential employers that they lead to it.

With each technical problem I solve, as a good netizen, I usually try to ensure some record of the solution can
be found somewhere on the interwebs for other poor sods to uncover.  But that usually has them scattered amid
the four winds.  My site should attempt to collect a few of those together into one safe, reflective, and attributable
 spot online.

**But also this is a personal website:**
Where else would I put stuff that carries my personal life, opinions, embarrassments—and triumphs—if not my own
namesake website?!  Where better to have an entirely Politically (IN)correct rant, to host holiday snaps
 and all the random crap I do for friends, family, and
(too often) relative strangers; all safe from the commercial interests of facebook et al?  Right here of course!

Whatsmore I'm often told I can string a few words together and encouraged to do more of that.  But what's the point 
if there is no place for that to be published?  What better place than my own corner of the Internet?! 
This site needs to encourage me to write and publish new content and make it available to all who have interest.

So in this we have two core requirements:

1. to demonstrate some competancy, and
2. to present personal _stuff_

Considering debate whether these are competing interests: I'm inclined toward arguing that they are 
because often there are personal issues and opinions which are improper in the workplace.

Nonetheless.  There's the background.  I need a website that works.  And this is a custom build...


## Python

I'm on the latest python in development, but my production host is typically one dot point behind.
It's not a big enough site to worry about the risk from different versions as downtime on a personal site is crazy cheap.
Python is awesome because I know it.
And I stick with it because
 it is fast (to code), popular, elegant, common, and wildly broad and flexible. The
only reason I can see for it not being more prominent in the corporate psyche is that there is no single big
commercial company vested enough to throw lots of dollars into marketing it.

Like any good python developer I use [Virtualenv](https://virtualenv.pypa.io/en/latest/) to isolate my myriad simultaneous projects.
Although I've tried and discarded [Virtualenvwrapper](https://virtualenvwrapper.readthedocs.org/en/latest/) as obsfucating sugar.

So the python stack (`requirements.txt` or `pip freeze`) for this thing looks something like:

```{.python}
Flask
Flask-FlatPages
itsdangerous
Jinja2
Markdown
MarkupSafe
Pygments
PyYAML
```

### Flask, Jinja Markdown and YAML


[Flask] provides the basic framework of turning requests into responses.
The core is simply this:

```{.python}
app = Flask(__name__)
pages = FlatPages(app)

@app.route('/<path:path>/')
def page(path):
    page = pages.get_or_404(path)
    return render_template('post.html', page=page)
```

Either there is a markdown page with the requested name in my posts directory, or there is not.
To add a post I just add a file to the directory and start writing.

There is a little contortion to feed the yaml-plus-markdown into [jinja2] and pygment it
so we can get these funky code highlighting bits.  I've reused some old code by Simon Sapin
called 'FlatPages' which neatly turns the yaml+markdown into a convenient python object.

```{.python}
app.config.update({
    'FLATPAGES_EXTENSION': ['.md', '.markdown'],
    'FLATPAGES_MARKDOWN_EXTENSIONS': ['codehilite', 'fenced_code'],
    'FLATPAGES_HTML_RENDERER': my_renderer
})

def my_renderer(text):
    """Inject the markdown rendering into the jinga template"""
    rendered_body = render_template_string(text)
    pygmented_body = markdown.markdown(rendered_body, extensions=['codehilite', 'fenced_code'])
    return pygmented_body
```

> <i class="fa fa-exclamation-triangle"></i> The code highlighting didn't work at all until I used the [`fenced_code` extension](https://pythonhosted.org/Markdown/extensions/fenced_code_blocks.html)

So now I'm free to dream up metadata and stick at the head of the post in YAML format (Name <colon> value).
Flatpages adds that
to the page object so now I can do meta operations on self-selected pages in the python;
like create an index, or filter by tag, or hold back publication.  For example:

```{.yaml}
title: How this blogging platform was built
published: 2015-10-15
tag: technical
```

```{.python}
# give me all the published articles
articles = [p for p in pages if isinstance(p.meta.get('published', False), datetime.date)]
```


## NGINX

During development it is trivial to serve the site from the command-line with nothing more complicated than `python blog.py`.
But for production we should probably do something a bit more robust; like [nginx] to talk to the world, and [uwsgi]
to mediate between nginx and the application.

The nginx config isn't too complex:


```{.python hl_lines="15"}
server {
    server_name johnmee.com;

    listen 80 default_server;
    listen [::]:80 default_server ipv6only=on;

    access_log /var/log/nginx/access.log;
    error_log /var/log/nginx/error.log;

    rewrite /2008/10/aeron-or-leap-chair-review /2008-10-30-aeron-or-leap-chair-review/ permanent;
    rewrite /1992/12/haole-hits-hawaii /1992-travel-letters/ permanent;
    rewrite /travel/beautiful-bali /1992-travel-letters/ permanent;

    location / {
        uwsgi_pass unix:///tmp/uwsgi.sock;
        include uwsgi_params;
    }
}
```

The highlighted line `uwsgi_pass` is where the action happens, passing off the the work of creating a response
to a unix socket which, hopefully, has a uwsgi process at the other end of it.

I've included the `rewrite` lines so you can see how to map deprecated URLs that are still getting hits to their
new locations.


## UWSGI

Because the webserver only really cares about serving remote connections really quickly and steers clear of getting
its hands dirtied by any specific programming language, we need UWSGI to connect nginx to the python code.

The config file looks like:

```{. hl_lines="5"}
[uwsgi]
vhost=true
virtualenv = /home/john/johnmee.com/venv/
plugin = python3
socket = /tmp/uwsgi.sock
wsgi-file = /home/john/johnmee.com/www/blog.py
callable = app
master = true
chdir = /home/john/johnmee.com/www/
uid = john
gid = www-data
chmod = 666
```

I've highlighted the connection between the two (nginx and uwsgi) at the `socket` parameter.  All of this you'll
find explained in the documentation.  But I hit a big snag which took some time to figure out; mostly because
you're running fairly blind&mdash;the only source of cryptic clues as to why it "doesn't work" are found in your
systems `/var/log/` log files.  Additionally the error messages all look the same so it can be tricky to spot
when you make a change that actually does something new.  At the end of that stretch I established that you must:

> <i class="fa fa-exclamation-triangle"></i> Pay close attention to file Owners and Permissions! 

The webserver (nginx) is typically running as a dedicated non-root user, and your files may belong to you and
your group personally and do not grant permission to the webserver user.  On Ubuntu that user is `www-data:www-data`
but my files are all `john:john` and, to add some more complexity, you can tell uwsgi which user and group to work as.

I've wound up setting all my files to `john:www-data` giving them `755` permissions, and telling uwsgi to use `john:www-data`.

