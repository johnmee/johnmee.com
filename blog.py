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
    pygmented_body = markdown.markdown(rendered_body, extensions=['codehilite', 'fenced_code'])
    return pygmented_body


app = Flask(__name__)

# override these settings (debug) by the presence of a settings file
try:
    app.config.from_pyfile('settings.ini')
except FileNotFoundError:
    app.config['DEBUG'] = False

app.config.update({
    'FLATPAGES_EXTENSION': ['.md', '.markdown'],
    'FLATPAGES_MARKDOWN_EXTENSIONS': ['codehilite', 'fenced_code'],
    'FLATPAGES_HTML_RENDERER': my_renderer
})
pages = FlatPages(app)


@app.route('/pygments.css')
def pygments_css():
    return pygments_style_defs('tango'), 200, {'Content-Type': 'text/css'}


@app.route('/robots.txt')
def robots():
    content = """User-agent: *
Disallow:
"""
    resp = make_response(content, 200, {'Content-Type': 'text/plain'})
    return resp


@app.route('/resume/')
@app.route('/resume/<path:path>')
def resume(path='index.html'):
    return send_from_directory('resume', path)


@app.route('/')
def home():
    articles = [p for p in pages if isinstance(p.meta.get('published', False), datetime.date)]
    articles.sort(reverse=True, key=lambda p: p.meta['published'])
    opinions, technicals = list(), list()
    for post in articles:
        tag = post.meta.get('tag', 'personal')
        if tag == 'personal':
            opinions.append(post)
        else:
            technicals.append(post)
    return render_template("index.html", technical_posts=technicals, opinion_posts=opinions)


@app.route('/<path:path>/')
def page(path):
    page = pages.get_or_404(path)
    return render_template('post.html', page=page)


@app.context_processor
def inject_debug():
    return dict(debug=app.debug)


if __name__ == '__main__':
    app.run(threaded=True)
