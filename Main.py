from flask import Flask
import os
from app import app as calculator_app

main_app = Flask(__name__)

port = int(os.getenv('PORT', 4000))

@main_app.route('/', methods=['GET', 'POST'])
def index():
    return calculator_app()

if __name__ == '__main__':
    main_app.run(host='0.0.0.0', port=port)
