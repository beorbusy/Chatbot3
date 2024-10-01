from flask import Flask
import os
from one import get_message  # Importing get_message() from one.py

app = Flask(__name__)

port = int(os.getenv('PORT', 4000))

@app.route('/')
def hello():
    message = get_message()  # Calling the function from one.py
    return message  # Return the message to the browser

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)