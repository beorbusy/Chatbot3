from flask import render_template

def get_hello_response():
    return render_template('index.html')  # Render the HTML template
