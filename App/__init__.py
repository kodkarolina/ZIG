from flask import Flask
app = Flask(__name__)

import os
app.secret_key = os.urandom(12)

import App.routes