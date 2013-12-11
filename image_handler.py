import SimpleHTTPServer
import SocketServer
from flask import Flask, request, session, g, redirect, url_for,\
                  abort, render_template, flash

app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':
        card_image  = request.files['image']
        return render_template('index.html', attachment = card_image)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(host= '0.0.0.0')
