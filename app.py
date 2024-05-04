from flask import Flask, render_template, request
from sympy import symbols, lambdify
from bisection import bisection_method


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("pages/index.html")

@app.route('/calculate', methods=['POST'])
def calculate():
    equation_str = request.form['equation']
    a = float(request.form['a'])
    b = float(request.form['b'])
    try:
        root, data = bisection_method(equation_str,a, b,)

        # Generate the step
        steps_html = f"<h3> Showing the first 5 steps </h3>\n <h3>The function f(x) = {equation_str}</h3>\n<br/><br/>"
        for iteration, root_estimate, func_value in data[:5]:
            steps_html += f"Iteration {iteration+1}: <br>"
            steps_html += f"Function Value at Root Estimate = f({root_estimate}) = {func_value}<br>"
            steps_html += f"---<br>"
        
        # Generate table for the first 10 iterations
        table_html = '<table><tr><th>Iteration</th><th>Root Estimate</th><th>Function Value at Root Estimate</th></tr>'
        for iteration, root_estimate, func_value in data[:10]:
            table_html += f'<tr><td>{iteration+1}</td><td>{root_estimate}</td><td>{func_value}</td></tr>'
        table_html += '</table>'
        
        return f"<h3>The root of the equation: {root}</h3><h3>Steps:</h3>{steps_html}<h3>First 10 iterations:</h3>{table_html}"
    except ValueError as e:
        return str(e)

@app.route("/feedback", methods=['GET'])
def bisection():
    return render_template("pages/feedback.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)