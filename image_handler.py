import requests
from PIL import Image
import ipdb
from flask import Flask, request, session, g, redirect, url_for,\
                  abort, render_template, flash, json

import pickMove

DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)

last_card = ''

def save_image(img):
    f = open("current_hand.jpg", "wb")
    f.write(img)
    f.close

@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':
        #ipdb.set_trace()
        card_image = request.get_data()
        image_file = save_image(card_image)
        poss_move = pickMove.game_main()
        return poss_move
    else:

        return last_card

if __name__ == '__main__':
    app.run(host= '0.0.0.0')
