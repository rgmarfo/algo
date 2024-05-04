from sympy import symbols, lambdify

def bisection_method(equation_str, a, b, tol=1e-6, max_iter=1000):
    iterations = 0
    data = []

    x = symbols('x')
    equation = lambdify(x, equation_str)

    if equation(a) * equation(b) >= 0:
        raise ValueError("Bisection method fails.")

    while (b - a) / 2 > tol and iterations < max_iter:
        c = (a + b) / 2
        root_estimate = (a + b) / 2
        func_value = equation(root_estimate)
        data.append((iterations, root_estimate, func_value))
        
        if func_value == 0:
            break
        if equation(c) * equation(a) < 0:
            b = root_estimate
        else:
            a = root_estimate
        iterations += 1

    return root_estimate, data
