from flask import Flask, render_template, request, jsonify
from sympy import symbols, lambdify, parse_expr
from bisection import bisection_method

app = Flask(__name__)

### Page routes
@app.route('/')
def index():
    return render_template('pages/homepage.html')







### Bracketing Method
@app.route('/bracketing')
def bracketing():
    return render_template('pages/bracketing/bracketing.html')

@app.route('/bracketing/lecturenote')
def lecturenote():
    return render_template('pages/bracketing/lecturenote.html')

@app.route('/bracketing/graph')
def graph():
    return render_template('pages/bracketing/graph.html')

@app.route('/bracketing/example')
def example():
    return render_template('pages/bracketing/example.html')





### Bisection Method
@app.route('/bracketing/bisectionbackground')
def bisectionbackground():
    return render_template('pages/bracketing/bisection/bisectionbackground.html')

@app.route('/bracketing/bisection/lecturenote')
def bisectionlecturenote():
    return render_template('pages/bracketing/bisection/lecturenote.html')

@app.route('/bracketing/bisection/graph')
def bisectiongraph():
    return render_template('pages/bracketing/bisection/graph.html')

@app.route('/bracketing/bisection/example')
def bisectionexample():
    return render_template('pages/bracketing/bisection/example.html')

@app.route('/bracketing/bisection/solve')
def bisectionsolve():
    return render_template('pages/bracketing/bisection/solve.html')





### False Position Method
@app.route('/bracketing/falsepositionbackground')
def falsepositonbackground():
    return render_template('pages/bracketing/false/falsepositionbackground.html')

@app.route('/bracketing/false/lecturenote')
def falsepositionlecturenote():
    return render_template('pages/bracketing/false/lecturenote.html')

@app.route('/bracketing/false/graph')
def falsepositiongraph():
    return render_template('pages/bracketing/false/graph.html')

@app.route('/bracketing/false/example')
def falsepositionexample():
    return render_template('pages/bracketing/false/example.html')

@app.route('/bracketing/false/solve')
def falsepositionsolve():
    return render_template('pages/bracketing/false/solve.html')






#### Endpoint Routes
@app.route('/calculate', methods=['POST'])
def calculate():
    equation_str = request.form['equation']
    a = float(request.form['a'])
    b = float(request.form['b'])
    try:
        root, data = bisection_method(equation_str, a, b)

        # Initialize steps_html and updated intervals
        steps_html = f"<h3> Showing the first 5 steps </h3>\n <h3>The function f(x) = {equation_str}</h3>\n<br/><br/>"
        updated_intervals = []
        for iteration, root_estimate, func_value in data[:5]:
            # Replace 'exp' with 'exp(x)' and evaluate the function
            x = symbols('x')
            f_expr = equation_str.replace('exp', 'exp(x)')
            f_expr = parse_expr(f_expr)
            f = lambdify(x, f_expr)
            
            # Determine the new intervals based on function values
            if f(a) * f(root_estimate) < 0:
                updated_intervals.append((a, root_estimate))
            else:
                updated_intervals.append((root_estimate, b))
            
            # Generate steps HTML
            steps_html += f"Iteration {iteration+1}: <br />"
            steps_html += f"Here, f({a})={f(a)} > 0 and f({b})={f(b)} < 0 <br/>"
            steps_html += f"∴ Now, Root lies between {a} and {b}<br/>"
            steps_html += f"X_0 = ({a}+{b})/2 = {root_estimate}<br/>"
            steps_html += f"f(X_0) = f({root_estimate}) = {func_value} > 0 <br/>"
            steps_html += f"---<br/>"
        
        # Generate table for the first 10 iterations
        table_html = '<table><tr><th>Iteration</th><th>Root Estimate</th><th>Function Value at Root Estimate</th></tr>'
        for i, (iteration, root_estimate, func_value) in enumerate(data[:10]):
            table_html += f'<tr><td>{iteration+1}</td><td>{root_estimate}</td><td>{func_value}</td></tr>'
        table_html += '</table>'

        return jsonify({
            'root': root,
            'steps_html': steps_html,
            'table_html': table_html,
            'updated_intervals': updated_intervals
        })
    except ValueError as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True, port=3000)
