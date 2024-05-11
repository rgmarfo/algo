from sympy import symbols, lambdify, parse_expr

def bisection_method(equation_str, a, b, tol=1e-6, max_iter=1000):
    iterations = 0
    data = []
    intervals = []

    x = symbols('x')
    equation = equation_str.replace('exp', 'exp(x)')
    equation = parse_expr(equation)
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
