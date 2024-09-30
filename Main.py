from flask import Flask
import os

app = Flask(__name__)

# Bind to the PORT environment variable or default to 4000
port = int(os.getenv('PORT', 4000))

@app.route('/')
def hello():
    return 'Hello World!'

if __name__ == '__main__':
    # Bind to 0.0.0.0 to allow external connections
    app.run(host='0.0.0.0', port=port)
