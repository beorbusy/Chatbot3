from flask import Flask
import os
from responses import get_hello_response  # Import the function

app = Flask(__name__)

port = int(os.getenv('PORT', 4000))

@app.route('/')
def hello():
    return get_hello_response()  # Call the function to get the response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
