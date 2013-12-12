#all imports
import sqlite3
import string
import random
from flask import Flask, request, session, g, redirect, url_for,\
                  abort, render_template, flash
from contextlib import closing

#configuration
DATABASE = 'data_bitly.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'
app = Flask(__name__)
app.config.from_object(__name__)


def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('models.sql', mode = 'r') as f:
            db.cursor().executescript(f.read())
        db.commit()

def shorten_url(old_url):
    gen_url = [random.choice(string.ascii_letters + string.digits)\
    for x in xrange(4)]
    new_url = "".join(gen_url)
    return new_url

@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()

@app.route('/', methods= ['GET', 'POST'])
def index():
    if request.method == 'POST':
        old_url= request.form['url']
        new_url= shorten_url(old_url)
        return render_template('index.html', shorten_url = new_url)
    else:
        return render_template('index.html')

@app.route('/<new_url>')
def new_url(new_url):
    return redirect(url_for('/'))

if __name__ == '__main__':
#make externally visable-- Turn off degugger!
    #app.run(host='0.0.0.0')
#development mode
    init_db()
    app.run()

@app.route('/getaddress', methods = ['POST', 'GET'])
def getaddress():
    error = None
    if request.method == 'POST':
        if valid_address(request.form['web_address']):
            return log_address(request.form['web_address'])
        else:
            error = 'Valid web adress'
    return render_template('getaddress.html', error=error)
