from flask import Flask
import os
from responses import get_hello_response  # Import the function from responses.py
from one import get_message               # Import the function from one.py

app = Flask(__name__)

port = int(os.getenv('PORT', 4000))

@app.route('/')
def hello():
    message = get_message()  # Call the function from one.py
    return f'{get_hello_response()} <br> {message}'  # Combine the HTML with the message

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)