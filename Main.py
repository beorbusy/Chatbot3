from flask import Flask, render_template, request
import os

app = Flask(__name__)

port = int(os.getenv('PORT', 4000))

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        try:
            # Get the two numbers from the form
            num1 = float(request.form.get('num1'))
            num2 = float(request.form.get('num2'))
            # Perform addition
            result = num1 + num2
        except (TypeError, ValueError):
            result = 'Invalid input, please enter numbers.'
    
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
