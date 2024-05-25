from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/calc', methods=['GET', 'POST'])
def calc():
    result = None
    if request.method == 'POST':
        try:
            num1 = float(request.form['num1'])
            num2 = float(request.form['num2'])
            addition = num1 + num2
            subtraction = num1 - num2
            multiplication = num1 * num2
            division = num1 / num2 if num2 != 0 else 'Undefined (division by zero)'
            result = {
                'addition': addition,
                'subtraction': subtraction,
                'multiplication': multiplication,
                'division': division
            }
        except ValueError:
            result = 'Invalid input. Please enter numerical values.'

    return render_template_string('''
        <form method="post">
            <input type="number" name="num1" step="any" required>
            <input type="number" name="num2" step="any" required>
            <button type="submit">Calculate</button>
        </form>
        {% if result %}
            <ul>
                {% if result == 'Invalid input. Please enter numerical values.' %}
                    <li>{{ result }}</li>
                {% else %}
                    <li>Addition: {{ result.addition }}</li>
                    <li>Subtraction: {{ result.subtraction }}</li>
                    <li>Multiplication: {{ result.multiplication }}</li>
                    <li>Division: {{ result.division }}</li>
                {% endif %}
            </ul>
        {% endif %}
    ''', result=result)

if __name__ == '__main__':
    app.run(debug=True)
