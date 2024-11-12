from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to T2S!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

import logging
from logging.handlers import RotatingFileHandler

handler = RotatingFileHandler('/app/logs/flask_app.log', maxBytes=10000, backupCount=3)
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
handler.setFormatter(formatter)
app.logger.addHandler(handler)

@app.route('/')
def home():
    app.logger.info("Homepage accessed")
    return "Welcome to T2S!"
