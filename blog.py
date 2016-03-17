import os
import markdown
import datetime

from flask import Flask
from flask import make_response
from flask import render_template
from flask import render_template_string
from flask import send_from_directory

from flask_flatpages import FlatPages
from flask_flatpages import pygments_style_defs



def my_renderer(text):
    """Inject the markdown rendering into the jinga template"""
    rendered_body = render_template_string(text)
    pygmented_body = markdown.markdown(rendered_body, extensions=['codehilite', 'fenced_code', 'tables'])
    return pygmented_body


app = Flask(__name__)
app.config['DEBUG'] = False

app.config.update({
    'FLATPAGES_EXTENSION': ['.md', '.markdown'],
    'FLATPAGES_MARKDOWN_EXTENSIONS': ['codehilite', 'fenced_code'],
    'FLATPAGES_HTML_RENDERER': my_renderer
})
pages = FlatPages(app)


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico',
                               mimetype='image/vnd.microsoft.icon')


@app.route('/pygments.css')
def pygments_css():
    return pygments_style_defs('tango'), 200, {'Content-Type': 'text/css'}


@app.route('/googleac8131d70b9df19d.html')
def googlewebmastertools():
    content = """google-site-verification: googleac8131d70b9df19d.html"""
    resp = make_response(content, 200, {'Content-Type': 'text/plain'})
    return resp


@app.route('/robots.txt')
def robots():
    content = """User-agent: *
Disallow: /static/
"""
    resp = make_response(content, 200, {'Content-Type': 'text/plain'})
    return resp


@app.route('/meejinnz/')
@app.route('/meejinnz/<path:path>')
def meejinnz(path='index.html'):
    return send_from_directory('meejinnz', path)


@app.route('/')
def home():
    # sort the posts to reverse date order
    posts = [p for p in pages if p.meta.get('tag', 'noindex')]
    posts.sort(reverse=True, key=lambda p: p.meta.get('published', datetime.date(1970, 1, 1)))

    # split them into technical and personal, omit those that aren't tagged
    opinions, technicals = list(), list()
    for post in posts:
        tag = post.meta.get('tag', 'noindex')
        if tag == 'noindex':
            continue
        elif tag == 'technical':
            technicals.append(post)
        else:
            opinions.append(post)

    return render_template("index.html", technical_posts=technicals, opinion_posts=opinions)


@app.route('/<path:path>')
def page(path):
    page = pages.get_or_404(path)
    return render_template('post.html', page=page)


@app.context_processor
def inject_debug():
    return dict(debug=app.debug)


if __name__ == '__main__':
    # if running as a raw script assume this is a development instance and try to run livereload
    app.config['DEBUG'] = True
    try:
        from livereload import Server
        server = Server(app.wsgi_app)
        server.serve()
    except ImportError:
        app.run(threaded=True)
