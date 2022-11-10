# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import os

from flask import Flask, jsonify, request, flash, url_for
from werkzeug.utils import secure_filename, redirect

import main

app = Flask(__name__)
app.config['DEBAG'] = True


@app.route('/ddd')
def index():
        return 'Hello World'


UPLOAD_FOLDER = '/Users/ihaup/Downloads/'
ALLOWED_EXTENSIONS = {'m4a'}


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/upload', methods = ['POST'])
def upload_file():
        f = request.files['wav']
        f.save(secure_filename(f.filename))
        return 'file uploaded successfully'


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5001",  debug=True)