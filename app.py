from flask import Blueprint, render_template, request

app = Blueprint('app', __name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        try:
            num1 = float(request.form.get('num1'))
            num2 = float(request.form.get('num2'))
            result = num1 - num2  # Change this line for subtraction
        except (TypeError, ValueError):
            result = 'Invalid input, please enter numbers.'
    
    return render_template('index.html', result=result)
