import json, re
import random
from flask import Flask, render_template, request, jsonify, redirect, url_for, flash
from sympy import symbols, lambdify, parse_expr, diff
import numpy as np

app = Flask(__name__)
app.secret_key = 'projectalgo2024'


with open('questions/questions.json') as f:
    bisection_questions = json.load(f)


with open('questions/fq.json') as fq:
    false_questions = json.load(fq)


with open('questions/nq.json') as nq:
    newton_questions = json.load(nq)


with open('questions/fxq.json') as fxq:
    fixed_questions = json.load(fxq)


with open('questions/sq.json') as sq:
    secant_questions = json.load(sq)


with open('questions/trq.json') as trq:
    trapezoidal_questions = json.load(trq)


with open('questions/fin.json') as fin:
    finite_questions = json.load(fin)


with open('questions/bw.json') as bw:
    backward_questions = json.load(bw)


with open('questions/fw.json') as fw:
    forward_questions = json.load(fw)

with open('questions/sim.json') as sim:
    simpson_questions = json.load(sim)


with open('questions/gu.json') as q:
    guassian_questions = json.load(q)


with open('questions/ja.json') as q:
    jacobi_questions = json.load(q)


with open('questions/lu.json') as q:
    lu_questions = json.load(q)



### landing page routes
@app.route('/')
def landing():
    return render_template('pages/landingpage.html')

### Main routes
@app.route('/homepage')
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
def false_position_background():
    return render_template('pages/bracketing/false/background.html')

@app.route('/bracketing/false/lecturenote')
def false_position_lecture_note():
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
def false_position_submit_answers():
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
    return jsonify({'score': score, 'results': results, 'total': len(user_answers)})


### Trapezoidal Rule
@app.route('/open/trapezoidalbackground')
def trapezoidal_background():
    return render_template('pages/open/trapezoidal/background.html')

@app.route('/open/trapezoidal/lecturenote')
def trapezoidal_lecturenote():
    return render_template('pages/open/trapezoidal/lecturenote.html')

@app.route('/open/trapezoidal/graph')
def trapezoidal_graph():
    return render_template('pages/open/trapezoidal/graph.html')

@app.route('/open/trapezoidal/example')
def trapezoidal_example():
    return render_template('pages/open/trapezoidal/example.html')

@app.route('/open/trapezoidal/solve')
def trapezoidal_solve():
    return render_template('pages/open/trapezoidal/solve.html')

@app.route('/open/trapezoidal/exercise')
def trapezoidal_exercise():
    return render_template('pages/open/trapezoidal/exercise.html')

@app.route('/open/trapezoidal/practice')
def trapezoidal_practice():
    # Randomly select a subset of questions
    num_questions = 5  # Change this number based on how many questions you want to display
    selected_questions = random.sample(trapezoidal_questions, num_questions)
    return render_template('pages/open/trapezoidal/practice.html', questions=selected_questions)

@app.route('/trapezoidal/submit_answers', methods=['POST'])
def trapezoidal_submit_answers():
    user_answers = request.json
    score = 0
    results = []

    # Validate answers
    for key in user_answers:
        q_index = int(key.replace('question', '')) - 1
        correct_answer = trapezoidal_questions[q_index]['correct']
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




### Simpson's Method
@app.route('/open/simpsonbackground')
def simpson_background():
    return render_template('pages/open/simpson/background.html')

@app.route('/open/simpson/lecturenote')
def simpson_lecture_note():
    return render_template('pages/open/simpson/lecturenote.html')

@app.route('/open/simpson/graph')
def simpson_graph():
    return render_template('pages/open/simpson/graph.html')

@app.route('/open/simpson/example')
def simpson_example():
    return render_template('pages/open/simpson/example.html')

@app.route('/open/simpson/solve')
def simpson_solve():
    return render_template('pages/open/simpson/solve.html')

@app.route('/open/simpson/exercise')
def simpson_exe():
    return render_template('pages/open/simpson/exercise.html')

@app.route('/open/simpson/practice')
def simpson_practice():
    # Randomly select a subset of questions
    num_questions = 5  # Change this number based on how many questions you want to display
    selected_questions = random.sample(simpson_questions, num_questions)
    return render_template('pages/open/simpson/practice.html', questions=selected_questions)

@app.route('/simpson/submit_answers', methods=['POST'])
def simpson_submit_answers():
    user_answers = request.json
    score = 0
    results = []

    # Validate answers
    for key in user_answers:
        q_index = int(key.replace('question', '')) - 1
        correct_answer = simpson_questions[q_index]['correct']
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

### Forward  Difference Methods
@app.route('/numerical calculus/forwardbackground')
def forward_background():
    return render_template('pages/numerical calculus/forward difference/background.html')

@app.route('/numerical calculus/forward difference/lecturenote')
def forward_lecture_note():
    return render_template('pages/numerical calculus/forward difference/lecturenote.html')

@app.route('/numerical calculus/forward difference/graph')
def forward_graph():
    return render_template('pages/numerical calculus/forward difference/graph.html')

@app.route('/numerical calculus/forward difference/example')
def forward_example():
    return render_template('pages/numerical calculus/forward difference/example.html')

@app.route('/numerical calculus/forward difference/solve')
def forward_solve():
    return render_template('pages/numerical calculus/forward difference/solve.html')

@app.route('/numerical calculus/forward difference/exercise')
def forward_exercise():
    return render_template('pages/numerical calculus/forward difference/exercise.html')

@app.route('/numerical calculus/forward difference/exercise')
def forward_practice():
    # Randomly select a subset of questions
    num_questions = 5  # Change this number based on how many questions you want to display
    selected_questions = random.sample(forward_questions, num_questions)
    return render_template('pages/open/simpson/practice.html', questions=selected_questions)


@app.route('/forward/submit_answers', methods=['POST'])
def forward_submit_answers():
    user_answers = request.json
    score = 0
    results = []

    # Validate answers
    for key in user_answers:
        q_index = int(key.replace('question', '')) - 1
        correct_answer = trapezoidal_questions[q_index]['correct']
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


### Backward  Difference Methods
@app.route('/numerical calculus/backwardbackground')
def backward_background():
    return render_template('pages/numerical calculus/backward difference/background.html')

@app.route('/numerical calculus/backward difference/lecturenote')
def backward_lecture_note():
    return render_template('pages/numerical calculus/backward difference/lecturenote.html')

@app.route('/numerical calculus/backward difference/graph')
def backward_graph():
    return render_template('pages/numerical calculus/backward difference/graph.html')

@app.route('/numerical calculus/backward difference/example')
def backward_example():
    return render_template('pages/numerical calculus/backward difference/example.html')

@app.route('/numerical calculus/backward difference/solve')
def backward_solve():
    return render_template('pages/numerical calculus/backward difference/solve.html')

@app.route('/numerical calculus/backward difference/exercise')
def backward_exercise():
    return render_template('pages/numerical calculus/backward difference/exercise.html')


@app.route('/numerical calculus/backward difference/practice')
def backward_practice():
    # Randomly select a subset of questions
    num_questions = 5  # Change this number based on how many questions you want to display
    selected_questions = random.sample(backward_questions, num_questions)
    return render_template('pages/numerical calculus/backward difference/practice.html', questions=selected_questions)

@app.route('/backward/submit_answers', methods=['POST'])
def backward_submit_answers():
    user_answers = request.json
    score = 0
    results = []

    # Validate answers
    for key in user_answers:
        q_index = int(key.replace('question', '')) - 1
        correct_answer = trapezoidal_questions[q_index]['correct']
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


### Linear systems(Gaussian Elimination)
@app.route('/linear systems/gaussianbackground')
def gaussian_background():
    return render_template('pages/linear systems/gaussian/background.html')

@app.route('/linear systems/gaussian/lecturenote')
def gaussian_lecture_note():
    return render_template('pages/linear systems/gaussian/lecturenote.html')

@app.route('/linear systems/gaussian/graph')
def gaussian_graph():
    return render_template('pages/linear systems/gaussian/graph.html')

@app.route('/linear systems/gaussian/example')
def gaussian_example():
    return render_template('pages/linear systems/gaussian/example.html')

@app.route('/linear systems/gaussian/solve')
def gaussian_solve():
    return render_template('pages/linear systems/gaussian/solve.html')

@app.route('/linear systems/gaussian/exercise')
def gaussian_exercise():
    return render_template('pages/linear systems/gaussian/exercise.html')

@app.route('/linear systems/gaussian/practice')
def gaussian_practice():
    # Randomly select a subset of questions
    num_questions = 5  # Change this number based on how many questions you want to display
    selected_questions = random.sample(guassian_questions, num_questions)
    return render_template('pages/linear systems/gaussian/practice.html', questions=selected_questions)


@app.route('/gaussian/submit_answers', methods=['POST'])
def gaussian_submit_answers():
    user_answers = request.json
    score = 0
    results = []

    # Validate answers
    for key in user_answers:
        q_index = int(key.replace('question', '')) - 1
        correct_answer = trapezoidal_questions[q_index]['correct']
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





### Linear systems(Jacobian Method)
@app.route('/linear systems/jacobibackground')
def jacobi_background():
    return render_template('pages/linear systems/jacobi/background.html')

@app.route('/linear systems/jacobi/lecturenote')
def jacobi_lecture_note():
    return render_template('pages/linear systems/jacobi/lecturenote.html')

@app.route('/linear systems/jacobi/graph')
def jacobi_graph():
    return render_template('pages/linear systems/jacobi/graph.html')

@app.route('/linear systems/jacobi/example')
def jacobi_example():
    return render_template('pages/linear systems/jacobi/example.html')

@app.route('/linear systems/jacobi/solve')
def jacobi_solve():
    return render_template('pages/linear systems/jacobi/solve.html')

@app.route('/linear systems/jacobi/exercise')
def jacobi_exercise():
    return render_template('pages/linear systems/jacobi/exercise.html')
 

@app.route('/linear systems/jacobi/practice')
def jacobi_practice():
    # Randomly select a subset of questions
    num_questions = 5  # Change this number based on how many questions you want to display
    selected_questions = random.sample(jacobi_questions, num_questions)
    return render_template('pages/linear systems/jacobi/practice.html', questions=selected_questions)

@app.route('/jacobi/submit_answers', methods=['POST'])
def jacobi_submit_answers():
    user_answers = request.json
    score = 0
    results = []

    # Validate answers
    for key in user_answers:
        q_index = int(key.replace('question', '')) - 1
        correct_answer = trapezoidal_questions[q_index]['correct']
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


### Linear systems(LU Decomposition Method)
@app.route('/linear systems/ludecompbackground')
def lu_background():
    return render_template('pages/linear systems/lu decomp/background.html')

@app.route('/linear systems/lu decomp/lecturenote')
def lu_lecture_note():
    return render_template('pages/linear systems/lu decomp/lecturenote.html')

@app.route('/linear systems/lu decomp/graph')
def lu_graph():
    return render_template('pages/linear systems/lu decomp/graph.html')

@app.route('/linear systems/lu decomp/example')
def lu_example():
    return render_template('pages/linear systems/lu decomp/example.html')

@app.route('/linear systems/lu decomp/solve')
def lu_solve():
    return render_template('pages/linear systems/lu decomp/solve.html')

@app.route('/linear systems/lu decomp/exercise')
def lu_exercise():
    return render_template('pages/linear systems/lu decomp/exercise.html')


@app.route('/linear systems/lu decomp/practice')
def lupractice():
    # Randomly select a subset of questions
    num_questions = 5  # Change this number based on how many questions you want to display
    selected_questions = random.sample(lu_questions, num_questions)
    return render_template('pages/linear systems/lu decomp/practice.html', questions=selected_questions)


@app.route('/lu/submit_answers', methods=['POST'])
def lu_submit_answers():
    user_answers = request.json
    score = 0
    results = []

    # Validate answers
    for key in user_answers:
        q_index = int(key.replace('question', '')) - 1
        correct_answer = trapezoidal_questions[q_index]['correct']
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
 

### Logic endpoints for bisection
def bisection_method(equation_str, a, b, tol=1e-6, max_iter=1000):
    iterations = 0
    data = []
    intervals = []

    x = symbols('x')
    equation = parse_expr(equation_str)
    equation = lambdify(x, equation)

    if equation(a) * equation(b) >= 0:
        raise ValueError("Bisection method fails.")

    while (b - a) / 2 > tol and iterations < max_iter:
        c = (a + b) / 2
        root_estimate = (a + b) / 2
        func_value = equation(root_estimate)
        data.append((iterations, root_estimate, func_value))
        
        # Save the current interval
        intervals.append((a, b))
        
        if func_value == 0:
            break
        if equation(c) * equation(a) < 0:
            b = root_estimate
        else:
            a = root_estimate
        iterations += 1

    return root_estimate, data, intervals
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

def secant_method(x0, x1, tol=1e-6, max_iter=1000):
    iterations = 0
    data = [(0, x0, f(x0)), (1, x1, f(x1))]

    while abs(x1 - x0) > tol and iterations < max_iter:
        x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        data.append((iterations + 2, x2, f(x2)))
        x0, x1 = x1, x2
        iterations += 1

    return x2, data
@app.route('/calculate_secant', methods=['POST'])
def calculate_secant():
    equation_str = request.form['equation']
    x0 = float(request.form['x0'])
    x1 = float(request.form['x1'])

    try:
        # Parse the equation string
        x = symbols('x')
        f_expr = parse_expr(equation_str)
        global f  # Make f accessible within secant_method
        f = lambdify(x, f_expr)
        
        # Ensure the secant method can be applied
        if f(x0) * f(x1) >= 0:
            raise ValueError("Secant method fails. The function values at x0 and x1 must have opposite signs.")
        
        # Run the secant method
        root, data = secant_method(x0, x1)
        
        # Generate the steps HTML for the first 5 steps
        steps_html = f"<p> Showing the first 5 steps </p>\n <p>The function f(x) = {equation_str}</p>\n<br/><br/>"
        for iteration, root_estimate, func_value in data[:5]:
            steps_html += f"<div class='step'>\n"
            steps_html += f"<h4>Iteration {iteration+1}:</h4>\n"
            steps_html += f"<p>X_{iteration} = {root_estimate}</p>\n"
            steps_html += f"<p>f(X_{iteration}) = {func_value}</p>\n"
            steps_html += "</div>\n<br/><br/>"

        # Generate table for the first 10 iterations
        table_html = '<table><tr><th>Iteration</th><th>Root Estimate</th><th>Function Value at Root Estimate</th></tr>'
        for iteration, root_estimate, func_value in data[:10]:
            table_html += f'<tr><td>{iteration+1}</td><td>{root_estimate}</td><td>{func_value}</td></tr>'
        table_html += '</table>'

        return jsonify({
            'root': root,
            'steps_html': steps_html,
            'table_html': table_html,
        })
    except ValueError as e:
        print(e)
        return jsonify({'error': str(e)})
    
    
def false_position(f, x0, x1, tol=1e-6, max_iter=1000):
    if f(x0) * f(x1) >= 0:
        raise ValueError("The function must have opposite signs at x0 and x1.")
    
    data = []
    for iteration in range(max_iter):
        # Calculate the point using the False Position formula
        x2 = x1 - (f(x1) * (x1 - x0)) / (f(x1) - f(x0))
        data.append((iteration + 1, x2, f(x2)))
        
        # Check if the root is found within tolerance
        if abs(f(x2)) < tol:
            return x2, data
        
        # Update the bracket
        if f(x0) * f(x2) < 0:
            x1 = x2
        else:
            x0 = x2
    
    # If no root is found within the maximum iterations, return the last estimate
    return x2, data
@app.route('/calculate_false_position', methods=['POST'])
def calculate_false_position():
    equation_str = request.form['equation']
    x0 = float(request.form['x0'])
    x1 = float(request.form['x1'])

    try:
        # Parse the equation string
        x = symbols('x')
        f_expr = parse_expr(equation_str)
        f = lambdify(x, f_expr)

        # Run the False Position method
        root, data = false_position(f, x0, x1)
        
        # Generate the steps HTML for the first 5 steps
        steps_html = f"<p> Showing the first 5 steps </p>\n <p>The function f(x) = {equation_str}</p>\n<br/><br/>"
        for iteration, root_estimate, func_value in data[:5]:
            steps_html += f"<div class='step'>\n"
            steps_html += f"<h4>Iteration {iteration}:</h4>\n"
            steps_html += f"<p>X_{iteration} = {root_estimate}</p>\n"
            steps_html += f"<p>f(X_{iteration}) = {func_value}</p>\n"
            steps_html += "</div>\n<br/><br/>"

        # Generate table for the first 10 iterations
        table_html = '<table><tr><th>Iteration</th><th>Root Estimate</th><th>Function Value at Root Estimate</th></tr>'
        for iteration, root_estimate, func_value in data[:10]:
            table_html += f'<tr><td>{iteration}</td><td>{root_estimate}</td><td>{func_value}</td></tr>'
        table_html += '</table>'

        return jsonify({
            'root': root,
            'steps_html': steps_html,
            'table_html': table_html,
        })
    except ValueError as e:
        print(e)
        return jsonify({'error': str(e)})


def newton_raphson(f, df, x0, tol=1e-6, max_iter=1000):
    data = []
    for iteration in range(max_iter):
        # Calculate the next approximation
        x1 = x0 - f(x0) / df(x0)
        data.append((iteration + 1, x1, f(x1)))
        
        # Check if the root is found within tolerance
        if abs(f(x1)) < tol:
            return x1, data
        
        x0 = x1  # Update the current approximation
    
    return x1, data  # Return the last estimate if max_iter is reached
@app.route('/calculate_newton_raphson', methods=['POST'])
def calculate_newton_raphson():
    equation_str = request.form['equation']
    x0 = float(request.form['x0'])
    try:
        # Parse the equation string
        x = symbols('x')
        f_expr = parse_expr(equation_str)
        f = lambdify(x, f_expr)
        df_expr = diff(f_expr, x)  # Differentiate the function
        df = lambdify(x, df_expr)
        
        # Run the Newton-Raphson method
        root, data = newton_raphson(f, df, x0)
        
        # Generate the steps HTML for the first 5 steps
        steps_html = f"<p> Showing the first 5 steps </p>\n <p>The function f(x) = {equation_str}</p>\n<br/><br/>"
        for iteration, root_estimate, func_value in data[:5]:
            steps_html += f"<div class='step'>\n"
            steps_html += f"<h4>Iteration {iteration}:</h4>\n"
            steps_html += f"<p>X_{iteration} = {root_estimate}</p>\n"
            steps_html += f"<p>f(X_{iteration}) = {func_value}</p>\n"
            steps_html += "</div>\n<br/><br/>"

        # Generate table for the first 10 iterations
        table_html = '<table><tr><th>Iteration</th><th>Root Estimate</th><th>Function Value at Root Estimate</th></tr>'
        for iteration, root_estimate, func_value in data[:10]:
            table_html += f'<tr><td>{iteration}</td><td>{root_estimate}</td><td>{func_value}</td></tr>'
        table_html += '</table>'

        return jsonify({
            'root': root,
            'steps_html': steps_html,
            'table_html': table_html,
        })
    except ValueError as e:
        print(e)
        return jsonify({'error': str(e)})


def fixed_point_iteration(g, x0, tol=1e-6, max_iter=1000):
    data = []
    for iteration in range(max_iter):
        x1 = g(x0)
        data.append((iteration + 1, x1, x1 - x0))
        
        # Check if the result is within tolerance
        if abs(x1 - x0) < tol:
            return x1, data
        
        x0 = x1  # Update the current approximation
    
    return x1, data  # Return the last estimate if max_iter is reached
@app.route('/calculate_fixed_point', methods=['POST'])
def calculate_fixed_point():
    function_str = request.form['equation']
    x0 = float(request.form['x0'])

    try:
        # Parse the function string
        x = symbols('x')
        g_expr = parse_expr(function_str)
        g = lambdify(x, g_expr)
        
        # Run the Fixed Point Iteration method
        root, data = fixed_point_iteration(g, x0)
        
        # Generate the steps HTML for the first 5 steps
        steps_html = f"<p> Showing the first 5 steps </p>\n <p>The function g(x) = {function_str}</p>\n<br/><br/>"
        for iteration, x_estimate, difference in data[:5]:
            steps_html += f"<div class='step'>\n"
            steps_html += f"<h4>Iteration {iteration}:</h4>\n"
            steps_html += f"<p>X_{iteration} = {x_estimate}</p>\n"
            steps_html += f"<p>Difference from previous estimate = {difference}</p>\n"
            steps_html += "</div>\n<br/><br/>"

        # Generate table for the first 10 iterations
        table_html = '<table><tr><th>Iteration</th><th>Root Estimate</th><th>Difference from Previous Estimate</th></tr>'
        for iteration, x_estimate, difference in data[:10]:
            table_html += f'<tr><td>{iteration}</td><td>{x_estimate}</td><td>{difference}</td></tr>'
        table_html += '</table>'

        return jsonify({
            'root': root,
            'steps_html': steps_html,
            'table_html': table_html,
        })
    except Exception as e:
        print(e)
        return jsonify({'error': str(e)})
    
    
def finite_difference(f, x, h=1e-5):
    """Approximate the derivative of f at point x using the forward difference method."""
    return (f(x + h) - f(x)) / h
@app.route('/calculate_finite_difference', methods=['POST'])
def calculate_finite_difference():
    equation_str = request.form['equation']
    x = float(request.form['x0'])
    s = float(request.form['s'])

    try:
        # Parse the equation string
        x_symbol = symbols('x')
        f_expr = parse_expr(equation_str)
        f = lambdify(x_symbol, f_expr)

        # Compute finite difference
        derivative_approx = finite_difference(f, x, s)

        # Generate the response HTML
        response_html = f"<p>Approximate derivative of f(x) = {equation_str} at x = {x}:</p>\n"
        response_html += f"<p>f'({x}) ≈ {derivative_approx}</p>\n"
        response_html += f"<p>Step size h = {s}</p>\n"

        return jsonify({
            'root': derivative_approx,
            'table_html': response_html,
        })
    except Exception as e:
        print(e)
        return jsonify({'error': str(e)})


def extract_limits(equation_str):
    """Extract the limits a and b from the equation string."""
    # Assuming the format of the equation string is something like 'f(x) = x^2 from 0 to 1'
    match = re.search(r'from\s*(-?\d+\.?\d*)\s*to\s*(-?\d+\.?\d*)', equation_str)
    if match:
        a = float(match.group(1))
        b = float(match.group(2))
        return a, b
    else:
        raise ValueError("The equation must include 'from a to b'.")
def trapezoidal_rule(f, a, b, n=10):
    """Approximate the integral of f from a to b using the Trapezoidal Rule with n intervals."""
    h = (b - a) / n
    integral = (f(a) + f(b)) / 2
    steps = [(a, f(a))]  # Store the first point

    for i in range(1, n):
        x_i = a + i * h
        fx_i = f(x_i)
        integral += fx_i
        steps.append((x_i, fx_i))  # Store each step

    integral *= h
    steps.append((b, f(b)))  # Store the last point
    return integral, steps
@app.route('/calculate_trapezoidal_rule', methods=['POST'])
def calculate_trapezoidal_rule():
    equation_str = request.form['equation']
    n = int(request.form.get('a', 10))  # Number of intervals

    try:
        # Extract the limits a and b from the equation string
        a, b = extract_limits(equation_str)

        # Parse the equation string to isolate the function
        equation_str = equation_str.split("from")[0].strip().replace("f(x) =", "")
        x = symbols('x')
        f_expr = parse_expr(equation_str)
        f = lambdify(x, f_expr)

        # Compute the integral using the Trapezoidal Rule
        integral_value, steps = trapezoidal_rule(f, a, b, n)

        # Generate the response HTML
        response_html = f"<p>Approximate integral of f(x) = {equation_str} from a = {a} to b = {b} using the Trapezoidal Rule:</p>\n"
        response_html += f"<p>Integral ≈ {integral_value}</p>\n"
        response_html += f"<p>Number of intervals n = {n}</p>\n"
        
        response_html += "<h3>Steps:</h3>\n<ul>\n"
        for x_i, fx_i in steps:
            response_html += f"<li>x = {x_i}, f(x) = {fx_i}</li>\n"
        response_html += "</ul>\n"

        return jsonify({
            'integral': integral_value,
            'steps': steps,
            'response_html': response_html,
        })
    except ValueError as e:
        print(e)
        return jsonify({'error': str(e)})
    except Exception as e:
        print(e)
        return jsonify({'error': 'An unexpected error occurred.'})
    

def simpsons_rule(f, a, b, n=10):
    """Approximate the integral of f from a to b using Simpson's Rule with n intervals."""
    if n % 2 != 0:
        raise ValueError("The number of intervals n must be even.")
    
    h = (b - a) / n
    integral = f(a) + f(b)
    steps = [(a, f(a))]  # Store the first point
    
    for i in range(1, n, 2):
        x_i = a + i * h
        fx_i = f(x_i)
        integral += 4 * fx_i
        steps.append((x_i, fx_i))  # Store the odd steps
    
    for i in range(2, n, 2):
        x_i = a + i * h
        fx_i = f(x_i)
        integral += 2 * fx_i
        steps.append((x_i, fx_i))  # Store the even steps
    
    integral *= h / 3
    steps.append((b, f(b)))  # Store the last point
    return integral, steps
@app.route('/calculate_simpsons_rule', methods=['POST'])
def calculate_simpsons_rule():
    equation_str = request.form['equation']
    n = int(request.form.get('n', 10))  # Number of intervals

    try:
        # Extract the limits a and b from the equation string
        a, b = extract_limits(equation_str)

        # Parse the equation string to isolate the function
        equation_str = equation_str.split("from")[0].strip().replace("f(x) =", "")
        x = symbols('x')
        f_expr = parse_expr(equation_str)
        f = lambdify(x, f_expr)

        # Compute the integral using Simpson's Rule
        integral_value, steps = simpsons_rule(f, a, b, n)

        # Generate the response HTML
        response_html = f"<p>Approximate integral of f(x) = {equation_str} from a = {a} to b = {b} using Simpson's Rule:</p>\n"
        response_html += f"<p>Integral ≈ {integral_value}</p>\n"
        response_html += f"<p>Number of intervals n = {n}</p>\n"
        
        response_html += "<h3>Steps:</h3>\n<ul>\n"
        for x_i, fx_i in steps:
            response_html += f"<li>x = {x_i}, f(x) = {fx_i}</li>\n"
        response_html += "</ul>\n"

        return jsonify({
            'integral': integral_value,
            'steps': steps,
            'response_html': response_html,
        })
    except ValueError as e:
        print(e)
        return jsonify({'error': str(e)})
    except Exception as e:
        print(e)
        return jsonify({'error': 'An unexpected error occurred.'})


def lu_decomposition(A):
    """Perform LU decomposition on matrix A."""
    A = np.array(A, dtype=float)
    n = len(A)
    L = np.zeros((n, n))
    U = np.zeros((n, n))

    for i in range(n):
        # Upper triangular matrix U
        for k in range(i, n):
            U[i, k] = A[i, k] - np.sum(L[i, :i] * U[:i, k])
        
        # Lower triangular matrix L
        for k in range(i, n):
            if U[i, i] == 0:
                raise ValueError("Matrix is singular.")
            L[k, i] = (A[k, i] - np.sum(L[k, :i] * U[:i, i])) / U[i, i]

    return L, U

@app.route('/calculate_lu', methods=['POST'])
def lu_endpoint():
    try:
        # Get the input data from the form
        A_str = request.form['A']
        
        # Convert the string input to a Python list
        A = json.loads(A_str)
        
        # Ensure that A is a list of lists
        if not isinstance(A, list) or not all(isinstance(row, list) for row in A):
            raise ValueError("Matrix A must be a list of lists.")
        
        # Perform LU decomposition
        L, U = lu_decomposition(A)
        
        return jsonify({
            'L': L.tolist(),
            'U': U.tolist()
        })
    
    except ValueError as e:
        return jsonify({'error': str(e)})
    except json.JSONDecodeError:
        return jsonify({'error': 'Invalid JSON format.'})
    except Exception as e:
        return jsonify({'error': 'An unexpected error occurred.'})




def gaussian_elimination(A, b):
    """Solve the system of linear equations Ax = b using Gaussian elimination."""
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)
    n = len(A)
    
    # Forward elimination
    for i in range(n):
        # Find the maximum element in the column
        max_row = np.argmax(np.abs(A[i:, i])) + i
        if i != max_row:
            # Swap rows
            A[[i, max_row]] = A[[max_row, i]]
            b[[i, max_row]] = b[[max_row, i]]
        
        # Eliminate entries below the pivot
        for j in range(i + 1, n):
            ratio = A[j, i] / A[i, i]
            A[j, i:] -= ratio * A[i, i:]
            b[j] -= ratio * b[i]
    
    # Back substitution
    x = np.zeros(n)
    for i in reversed(range(n)):
        x[i] = (b[i] - np.dot(A[i, i + 1:], x[i + 1:])) / A[i, i]
    
    return x

@app.route('/calculate_gaussian', methods=['POST'])
def gaussian_endpoint():
    try:
        # Get the input data from the form
        A_str = request.form['A']
        b_str = request.form['b']
        
        # Convert the string inputs to Python lists
        A = json.loads(A_str)
        b = json.loads(b_str)
        
        # Ensure that A and b are lists
        if not isinstance(A, list) or not isinstance(b, list):
            raise ValueError("Input data must be lists.")
        
        # Ensure A is a 2D list and b is a 1D list
        if not all(isinstance(row, list) for row in A) or not all(isinstance(x, (int, float)) for x in b):
            raise ValueError("Matrix A must be a list of lists and b must be a list of numbers.")
        
        # Solve using Gaussian Elimination
        x = gaussian_elimination(A, b)
        return jsonify({'solution': x.tolist()})
    
    except ValueError as e:
        return jsonify({'error': str(e)})
    
    except json.JSONDecodeError:
        return jsonify({'error': 'Invalid JSON format.'})
    
    except Exception as e:
        return jsonify({'error': 'An unexpected error occurred.'})

if __name__ == '__main__':
    app.run(debug=True, port=3000)
