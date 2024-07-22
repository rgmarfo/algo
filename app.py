import json
import random
from flask import Flask, render_template, request, jsonify, redirect, url_for, flash
from sympy import symbols, lambdify, parse_expr
from bisection import bisection_method

app = Flask(__name__)
app.secret_key = 'projectalgo2024'



with open('questions.json') as f:
    bisection_questions = json.load(f)
with open('questions.json') as f:
    false_questions = json.load(f)
with open('questions.json') as f:
    newton_questions = json.load(f)
with open('questions.json') as f:
    fixed_questions = json.load(f)
with open('questions.json') as f:
    secant_questions = json.load(f)




### Main routes
@app.route('/')
def index():
    return render_template('pages/homepage.html')
    
@app.route('/feedback')
def feedback():
    return render_template('pages/feedback.html')

@app.route('/speed')
def speed():
    return render_template('pages/speed.html')

@app.route('/forum')
def forum():
    return render_template('pages/forum.html')


### Bisection Method
@app.route('/bracketing/bisectionbackground')
def bisection_background():
    return render_template('pages/bracketing/bisection/background.html')

@app.route('/bracketing/bisection/lecturenote')
def bisection_lecture_note():
    return render_template('pages/bracketing/bisection/lecturenote.html')

@app.route('/bracketing/bisection/graph')
def bisection_graph():
    return render_template('pages/bracketing/bisection/graph.html')

@app.route('/bracketing/bisection/example')
def bisection_example():
    return render_template('pages/bracketing/bisection/example.html')

@app.route('/bracketing/bisection/solve')
def bisection_solve():
    return render_template('pages/bracketing/bisection/solve.html')

@app.route('/bracketing/bisection/exercise')
def bisection_exe():
    return render_template('pages/bracketing/bisection/exercise.html')

@app.route('/bracketing/bisection/practice')
def bisection_practice():
    # Randomly select a subset of questions
    num_questions = 5  # Change this number based on how many questions you want to display
    selected_questions = random.sample(bisection_questions, num_questions)
    return render_template('pages/bracketing/bisection/practice.html', questions=selected_questions)
    
@app.route('/bisection/submit_answers', methods=['POST'])
def bisection_submit_answers():
    user_answers = request.json
    score = 0
    results = []

    # Validate answers
    for key in user_answers:
        q_index = int(key.replace('question', '')) - 1
        correct_answer = bisection_questions[q_index]['correct']
        is_correct = user_answers[key] == correct_answer
        if is_correct:
            score += 1
        results.append({
            'question_id': q_index + 1,
            'user_answer': user_answers[key],
            'correct_answer': correct_answer,
            'is_correct': is_correct
        })

    return jsonify({'score': score, 'results': results, 'total': len(user_answers)})



### False Position Method
@app.route('/bracketing/falsepositionbackground')
def false_positon_background():
    return render_template('pages/bracketing/false/background.html')

@app.route('/bracketing/false/lecturenote')
def false_position_lecturenote():
    return render_template('pages/bracketing/false/lecturenote.html')

@app.route('/bracketing/false/graph')
def false_position_graph():
    return render_template('pages/bracketing/false/graph.html')

@app.route('/bracketing/false/example')
def false_position_example():
    return render_template('pages/bracketing/false/example.html')

@app.route('/bracketing/false/solve')
def false_position_solve():
    return render_template('pages/bracketing/false/solve.html')

@app.route('/bracketing/false/exercise')
def false_position_exercise():
    return render_template('pages/bracketing/false/exercise.html')

@app.route('/bracketing/false/practice')
def false_position_practice():
    # Randomly select a subset of questions
    num_questions = 5  # Change this number based on how many questions you want to display
    selected_questions = random.sample(false_questions, num_questions)
    return render_template('pages/bracketing/false/practice.html', questions=selected_questions)

@app.route('/false/submit_answers', methods=['POST'])
def false_positin_submit_answers():
    user_answers = request.json
    score = 0
    results = []

    # Validate answers
    for key in user_answers:
        q_index = int(key.replace('question', '')) - 1
        correct_answer = false_questions[q_index]['correct']
        is_correct = user_answers[key] == correct_answer
        if is_correct:
            score += 1
        results.append({
            'question_id': q_index + 1,
            'user_answer': user_answers[key],
            'correct_answer': correct_answer,
            'is_correct': is_correct
        })

    return jsonify({'score': score, 'results': results, 'total': len(user_answers)})



### Newton Methods
@app.route('/open/newtonbackground')
def newton_background():
    return render_template('pages/open/newton/background.html')

@app.route('/open/newton/lecturenote')
def newton_lecture_note():
    return render_template('pages/open/newton/lecturenote.html')

@app.route('/open/newton/graph')
def newton_graph():
    return render_template('pages/open/newton/graph.html')

@app.route('/open/newton/example')
def newton_example():
    return render_template('pages/open/newton/example.html')

@app.route('/open/newton/solve')
def newton_solve():
    return render_template('pages/open/newton/solve.html')

@app.route('/open/newton/exercise')
def newton_exercise():
    return render_template('pages/open/newton/exercise.html')

@app.route('/open/newton/practice')
def newton_practice():
    # Randomly select a subset of questions
    num_questions = 5  # Change this number based on how many questions you want to display
    selected_questions = random.sample(newton_questions, num_questions)
    return render_template('pages/open/newton/practice.html', questions=selected_questions)

@app.route('/newton/submit_answers', methods=['POST'])
def newton_submit_answers():
    user_answers = request.json
    score = 0
    results = []

    # Validate answers
    for key in user_answers:
        q_index = int(key.replace('question', '')) - 1
        correct_answer = newton_questions[q_index]['correct']
        is_correct = user_answers[key] == correct_answer
        if is_correct:
            score += 1
        results.append({
            'question_id': q_index + 1,
            'user_answer': user_answers[key],
            'correct_answer': correct_answer,
            'is_correct': is_correct
        })

    return jsonify({'score': score, 'results': results, 'total': len(user_answers)})




### Secant Methods
@app.route('/open/secantbackground')
def secant_background():
    return render_template('pages/open/secant/background.html')

@app.route('/open/secant/lecturenote')
def secant_lecture_note():
    return render_template('pages/open/secant/lecturenote.html')

@app.route('/open/secant/graph')
def secant_graph():
    return render_template('pages/open/secant/graph.html')

@app.route('/open/secant/example')
def secant_example():
    return render_template('pages/open/secant/example.html')

@app.route('/open/secant/solve')
def secant_solve():
    return render_template('pages/open/secant/solve.html')

@app.route('/open/secant/exercise')
def secant_exercise():
    return render_template('pages/open/secant/exercise.html')

@app.route('/open/secant/practice')
def secant_practice():
    # Randomly select a subset of questions
    num_questions = 5  # Change this number based on how many questions you want to display
    selected_questions = random.sample(secant_questions, num_questions)
    return render_template('pages/open/secant/practice.html', questions=selected_questions)
    
@app.route('/secant/submit_answers', methods=['POST'])
def secant_submit_answers():
    user_answers = request.json
    score = 0
    results = []

    # Validate answers
    for key in user_answers:
        q_index = int(key.replace('question', '')) - 1
        correct_answer = secant_questions[q_index]['correct']
        is_correct = user_answers[key] == correct_answer
        if is_correct:
            score += 1
        results.append({
            'question_id': q_index + 1,
            'user_answer': user_answers[key],
            'correct_answer': correct_answer,
            'is_correct': is_correct
        })

    return jsonify({'score': score, 'results': results, 'total': len(user_answers)})
    
    
### Fixed Methods
@app.route('/open/fixedbackground')
def fixed_background():
    return render_template('pages/open/fixed/background.html')

@app.route('/open/fixed/lecturenote')
def fixed_lecture_note():
    return render_template('pages/open/fixed/lecturenote.html')

@app.route('/open/fixed/graph')
def fixed_graph():
    return render_template('pages/open/fixed/graph.html')

@app.route('/open/fixed/example')
def fixed_example():
    return render_template('pages/open/fixed/example.html')

@app.route('/open/fixed/solve')
def fixed_solve():
    return render_template('pages/open/fixed/solve.html')

@app.route('/open/fixed/exercise')
def fixed_exercise():
    return render_template('pages/open/fixed/exercise.html')

@app.route('/open/fixed/practice')
def fixed_practice():
    # Randomly select a subset of questions
    num_questions = 5  # Change this number based on how many questions you want to display
    selected_questions = random.sample(fixed_questions, num_questions)
    return render_template('pages/open/fixed/practice.html', questions=selected_questions)
    
@app.route('/fixed/submit_answers', methods=['POST'])
def fixed_submit_answers():
    user_answers = request.json
    score = 0
    results = []

    # Validate answers
    for key in user_answers:
        q_index = int(key.replace('question', '')) - 1
        correct_answer = fixed_questions[q_index]['correct']
        is_correct = user_answers[key] == correct_answer
        if is_correct:
            score += 1
        results.append({
            'question_id': q_index + 1,
            'user_answer': user_answers[key],
            'correct_answer': correct_answer,
            'is_correct': is_correct
        })

    return jsonify({'score': score, 'results': results, 'total': len(user_answers)})


### Finite Difference Methods
@app.route('/open/finitebackground')
def finite_background():
    return render_template('pages/open/finite/background.html')

@app.route('/open/finite/lecturenote')
def finite_lecture_note():
    return render_template('pages/open/finite/lecturenote.html')

@app.route('/open/finite/graph')
def finite_graph():
    return render_template('pages/open/finite/graph.html')

@app.route('/open/finite/example')
def finite_example():
    return render_template('pages/open/finite/example.html')

@app.route('/open/finite/solve')
def finite_solve():
    return render_template('pages/open/finite/solve.html')

@app.route('/open/finite/exercise')
def finite_exercise():
    return render_template('pages/open/finite/exercise.html')

@app.route('/open/finite/practice')
def finite_practice():
    # Randomly select a subset of questions
    num_questions = 5  # Change this number based on how many questions you want to display
    selected_questions = random.sample(finite_questions, num_questions)
    return render_template('pages/open/finite/practice.html', questions=selected_questions)
    
@app.route('/finite/submit_answers', methods=['POST'])
def finite_submit_answers():
    user_answers = request.json
    score = 0
    results = []

    # Validate answers
    for key in user_answers:
        q_index = int(key.replace('question', '')) - 1
        correct_answer = finite_questions[q_index]['correct']
        is_correct = user_answers[key] == correct_answer
        if is_correct:
            score += 1
        results.append({
            'question_id': q_index + 1,
            'user_answer': user_answers[key],
            'correct_answer': correct_answer,
            'is_correct': is_correct
        })

 

### Logic endpoints
@app.route('/calculate', methods=['POST'])
def calculate():
    equation_str = request.form['equation']
    a = float(request.form['a'])
    b = float(request.form['b'])
    try:
        root, data, intervals = bisection_method(equation_str, a, b)

        # Initialize steps_html
        steps_html = f"<p> Showing the first 5 steps </p>\n <p>The function f(x) = {equation_str}</p>\n<br/><br/>"
        for iteration, root_estimate, func_value in data[:5]:
            # Replace 'exp' with 'exp(x)' and evaluate the function
            x = symbols('x')
            f_expr = parse_expr(equation_str)
            f = lambdify(x, f_expr)

            # Generate steps HTML
            steps_html += f"<div class='step'>\n"
            steps_html += f"<h4>Iteration {iteration+1}:</h4>\n"
            steps_html += '<br/>'
            steps_html += f"<p>Here, f({intervals[iteration][0]}) = {f(intervals[iteration][0])} > 0 and f({intervals[iteration][1]})={f(intervals[iteration][1])} < 0</p>\n"
            steps_html += '<br/>'
            steps_html += f"<p>∴ Now, Root lies between {intervals[iteration][0]} and {intervals[iteration][1]}</p>\n"
            steps_html += '<br/>'
            steps_html += f"<p>X_0 = ({intervals[iteration][0]}+{intervals[iteration][1]})/2 = {root_estimate}<br/></p>\n"
            steps_html += '<br/>'
            steps_html += f"<p>f(X_0) = f({root_estimate}) = {func_value} > 0</p>\n"
            steps_html += '<br/>'
            steps_html += "</div>\n"
            steps_html += '<br/>'
            steps_html += '<br/>'

        steps_html += "</div>\n"

        # Generate table for the first 10 iterations
        table_html = '<table><tr><th>Iteration</th><th>Root Estimate</th><th>Function Value at Root Estimate</th></tr>'
        for i, (iteration, root_estimate, func_value) in enumerate(data[:10]):
            table_html += f'<tr><td>{iteration+1}</td><td>{root_estimate}</td><td>{func_value}</td></tr>'
        table_html += '</table>'

        return jsonify({
            'root': root,
            'steps_html': steps_html,
            'table_html': table_html,
            'intervals': intervals
        })
    except ValueError as e:
        print(e)
        return jsonify({'error': str(e)})




if __name__ == '__main__':
    app.run(debug=True, port=3000)
