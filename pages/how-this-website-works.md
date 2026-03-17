title: How this website works
published: 2015-10-15
tag: technical
disqus: http://johnmee.com/how-this-website-works


[python]: https://www.python.org/ "Python"
[flask]: http://flask.pocoo.org/ "Flask"
[jinja2]: http://jinja.pocoo.org/docs/ "Jinja2"
[markdown]: http://daringfireball.net/projects/markdown/ "Markdown"
[skeleton]: http://getskeleton.com "Skeleton"
[pygments]: http://pygments.org/ "Pygments"
[yaml]: http://yaml.org/spec/1.1/ "YAML"
[meejinnz]: /meejinnz/ "Mee, John: In NZ"
[git]: https://git-scm.com/ "git"
[github]: http://github.com/johnmee/johnmee.com/ "GitHub"
[nginx]: http://nginx.org   "Nginx"


# How I built this simple blogging site

This site was hand-built using the [Python programming language][python]:

* the pages are assembled by the microframework [Flask] and templating language [Jinja2]
* the content is composed in prose friendly [Markdown]
* and the code snippets rendered with [Pygments]
* the responsive layout (CSS) is based on [Skeleton]
* there is no database involved&mdash;relational, noSQL, NewSQL, or otherwise
* the webservice stack is [UWSGI](https://uwsgi-docs.readthedocs.org/) and [nginx] on an [Ubuntu](http://www.ubuntu.com/) server
* it is hosted on a VPS at [Binary Lane](http://binarylane.com.au/)
* it draws on [disqus](https://disqus.com/) for the commenting
* it draws on [Google Analytics](http://www.google.com.au/analytics/) just in case I bother to check if anyone is reading
* it is committed to [git] and [github], 
   usually by commandline but often using [sourcetree](https://www.sourcetreeapp.com/)
* it is edited mostly with [Pycharm](https://www.jetbrains.com/pycharm/), 
   but also [vi](https://en.wikipedia.org/wiki/Vi), and [sublimetext](http://www.sublimetext.com/).
* my desktop is usually [OS X](http://www.apple.com/au/osx/)

## Background Ramble/Requirements

This "vanity" website has gone through more rebuilds than I dare to count.  In some respects it feels like a 
corporate home page the way my interests play tug-of-war over it.  Initially it was, of course just HTML, then
after various rewrites, I _drank the coolaid_ and used WordPress. That was fairly successful in getting me
to post stuff, but thoroughly unportable, somewhat inflexible, and was mildly repugnant for no greater offense than
 lack of geekness.

**In some respects this site is a CV:** 
My job is, not exclusively but mostly, about building websites&mdash;or web `applications` as I like to distinguish&mdash;and
failing to have a respectable personal website could reflect poorly on my credibility, even to those who appreciate 
just how low your own website can fall on the TODO list.  So the site needs to show I can knock up a working website 
that looks reasonably current and carry a resum&eacute;, simple enough for the technically challenged recruitment agents to work with, 
yet blingy enough to impress the potential employers that follow.

**A consolidation of contributions:**
With each technical problem I solve, as a good netizen, I usually try to ensure some record of the solution can
be found somewhere on the interwebs for other poor sods to uncover.  But that sees them scattered amid
the four winds.  This site attempts to gather the better ones back into the fold: a safe, reflective, and attributable
 resource online.

**Yet also a personal website:**
I'm often told I can string a few words together and often encouraged to do more of that.  But what's the point 
if there is no place for that to be published?  What better place than my own corner of the Internet?! 

Everyone has bandwagons and opinions which they want to show the light of day, right?  We can spread them
to the winds, like above, as anonymous trolls, or we can take responsibility and own them.
Where else should one put the glory, and embarrassment, that embodies a personal life—if not their own
namesaked website?!  Rather than adorn, or burden, other interests with my rants, holiday snaps
 and all the random crap I do for friends, family, and relative strangers, let's keep it all in
  the safety of my own corner of the Internet.

So perhaps you see the tension.  I need to:

1. to demonstrate professional competancy and yet
2. present entirely personal _stuff_

Hopefully the former audience can ignore the latter, and vice versa.

I'm agreeable that personal issues and opinions are improper in the workplace, but I tried
running separate sites and, depending on where the pendulum swung, one always walked in the shadow of the other.

So this site is a custom build and needs to be as flexible as life is in accomodating tension.

Enough&mdash;let's get our geek on!


## Python

I'm on the latest python in development, but my production host is typically one dot point behind.
It's not a big enough site to worry about the risk from different versions as downtime on a personal site is not expensive.
Python is awesome because I know it.
And I stick with it because
 it is fast (to code), popular, elegant, common, and wildly broad and flexible. The
only reason I can see for it not being more prominent in the corporate psyche is that there is no single big
commercial company vested enough to throw lots of dollars into marketing it as the answer to everything.

Like any good python developer I use [Virtualenv](https://virtualenv.pypa.io/en/latest/) to isolate my myriad simultaneous projects.
Although I've tried and discarded [Virtualenvwrapper](https://virtualenvwrapper.readthedocs.org/en/latest/) as 
mere obsfucating syntactic sugar.

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


[Flask] provides the basic framework of turning requests into responses and the core is simply this:

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

    rewrite /2008/10/aeron-or-leap-chair-review /2008-10-30-aeron-or-leap-chair-review permanent;
    rewrite /1992/12/haole-hits-hawaii /1992-travel-letters permanent;
    rewrite /travel/beautiful-bali /1992-travel-letters permanent;

    location / {
        uwsgi_pass unix:///tmp/uwsgi.sock;
        include uwsgi_params;
    }
}
```

The highlighted line `uwsgi_pass` is where the action happens, passing off the the work of creating a response
to a unix socket which, hopefully, has a uwsgi process at the other end of it.

I've included the `rewrite` lines so you can see how to throw deprecated URLs that are still getting hits to their
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
when you make a change that actually does something new.  At the end of that stretch I established my problem:

> <i class="fa fa-exclamation-triangle"></i> Pay close attention to file Owners and Permissions! 

The webserver (nginx) is typically running as a dedicated non-root user, and your files may belong to you and
your group personally and do not grant permission to the webserver user.  On Ubuntu that user is `www-data:www-data`
but my files are all `john:john` and, to add some more complexity, you can tell uwsgi which user and group to work as.

I've wound up setting all my files to `john:www-data` giving them `755` permissions, and telling uwsgi to use `john:www-data`.

## Disqus

For engagement there needs to be some kind of feedback mechanism, but there are so many options!  Disqus was very early on the scene
and I accumulated some comments early which would be sad to abandon.

So given no compelling reason to change, I've opted for it again.  The threads are keyed by URL but, fortunately,
the 'URL' is just the default ID, so we can move the page location and retain the comments by feeding their API the
original URL.  I do this via the YAML metadata at the top of the markdown page.  If I don't mention disqus it
defaults to turning comments off.  Most of the technical posts will appear somewhere on StackOverflow and it's more
appropriate to react to them there.


In the markdown I can switch on/off the comments by setting a `disqus` metavalue with the disqus ID:

```{.yaml}
disqus: http://johnmee.com/1992-travel-letters
```

In the template I have the disqus boilerplate with my variables.  Note that disqus have this silly
`shortname` id for the site which I must have set to `sydneyboy` years ago and now I'm stuck with:

```{.html hl_lines="1 4 5"}{% raw %}
{% if page.disqus %}
    <div id="disqus_thread"></div>
    <script type="text/javascript">
        var disqus_shortname = 'sydneyboy';
        var disqus_url = {{ page.disqus }};
    
        (function () {
            var dsq = document.createElement('script');
            dsq.type = 'text/javascript';
            dsq.async = true;
            dsq.src = '//' + disqus_shortname + '.disqus.com/embed.js';
            (document.getElementsByTagName('head')[0] || document.getElementsByTagName('body')[0]).appendChild(dsq);
        })();
    </script>
{% endif %}{% endraw %}
```

I found the disqus website UI quite clumsy for identifying which threads were valuable/popular. Ultimately I
 found the best, most authoritative, way was to `export` everything and sift through the XML file.  Thus I could
 see both the comments and their thread ID/URL in the one place.


## Analytics

There is nothing special about the google analytics inclusion template.  It is included exactly as per the boilerplate
they provide, excepting that in the template I include a switch to ~not~ include it when in `DEBUG` mode. Thus,
I make sure the stats don't get messed up by development and testing.


## Legacy HTML content

I have random bits of content like [meejinnz] which I knocked up as pure HTML a while back.  Now who could be
 bothered to rework that into markdown? So, fortunately, I can integrate it into the flask reconfigurement
 fairly trivially:

```{.python}
@app.route('/meejinnz/')
@app.route('/meejinnz/<path:path>')
def meejinnz(path='index.html'):
    return send_from_directory('meejinnz', path)
```

The html and images are placed into a directory on their own then this incantation will default to serving the
index file and also serve any specific file in the path there.  Awesome.

## Deployment, Git, and Github

For source control I use [git] and (unnecessarily) keep a remote copy of the repo at [github](https://github.com/johnmee/johnmee.com/).
To deploy changes I don't bother with github eventhooks; it is just as easy to feed a script into ssh myself:

`redeploy.sh` looks like this:

```{.bash}
cd /home/john/johnmee.com/www
git pull
sudo service uwsgi reload
sudo service nginx reload
```

And simply piping this local file into ssh is enough to effect an update:

```{. hl_lines="1"}
Johns-iMac:latest johnmee$ cat redeploy.sh | ssh binlane
Pseudo-terminal will not be allocated because stdin is not a terminal.
Linux binarylane 3.14-1-amd64 #1 SMP Debian 3.14.4-1 (2014-05-13) x86_64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
From https://github.com/johnmee/johnmee.com
Updating 9fb23af..059547d
Fast-forward
 ...-website-works.md => how-this-website-works.md} | 121 ++++++++++++++++++++-
 redeploy.sh                                        |   4 +
 2 files changed, 122 insertions(+), 6 deletions(-)
Reloading app server(s): uwsgi -> . done.
Reloading nginx configuration: nginx.
Johns-iMac:latest johnmee$
```

Famous last words, but I think this approach should be relatively secure compared to spreading keys around and
opening up holes.


There you have it.  That's how this website works.  If you want to point out a weakness, strength, or clarify or
expand on some part, by all means, please leave a comment...

