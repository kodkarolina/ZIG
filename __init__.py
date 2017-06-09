from flask import Flask
app = Flask(__name__)

# app.secret_key = "sosecretkey"
# app.config.from_object('config')


# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:BazaDanychYolo94@localhost/rcp'

# from ZIG.models import db
# db.init_app(app)

import ZIG.routes