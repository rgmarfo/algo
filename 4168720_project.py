import numpy as np


# Parameters for the iterative methods below
a, b = 2, 3
x0, x1 = 2.6, 2.742

# The equation whose root is being calculated
def f(x):
    return x**3 - 3*x**2 + x - 1


def bisection_method(a, b, tol=1e-6, max_iter=1000):
    iterations = 0
    data = []

    if f(a) * f(b) >= 0:
        raise ValueError("Bisection method fails.")

    while (b - a) / 2 > tol and iterations < max_iter:
        c = (a + b) / 2
        data.append((iterations, c, f(c)))
        if f(c) == 0:
            break
        if f(c) * f(a) < 0:
            b = c
        else:
            a = c
        iterations += 1

    return c, data

def secant_method(x0, x1, tol=1e-6, max_iter=1000):
    iterations = 0
    data = [(0, x0, f(x0)), (1, x1, f(x1))]

    if f(a) * f(b) >= 0:
        raise ValueError("Secant method fails.")

    while abs(x1 - x0) > tol and iterations < max_iter:
        x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        data.append((iterations + 2, x2, f(x2)))
        x0, x1 = x1, x2
        iterations += 1

    return x2, data

def newton_raphson_method(x0, tol=1e-6, max_iter=1000):
    iterations = 0
    data = [(0, x0, f(x0))]
    
    while abs(f(x0)) > tol and iterations < max_iter:
        x0 = x0 - f(x0) / (3 * x0**2 - 6 * x0 + 1)
        data.append((iterations + 1, x0, f(x0)))
        iterations += 1

    return x0, data

def fixed_point_iteration_method(x0, tol=1e-6, max_iter=100):
    iterations = 0
    data = [(0, x0, f(x0))]

    g = lambda x: (x**3 + x - 1) / 3

    while abs(f(x0)) > tol and iterations < max_iter:
        x0 = g(x0)
        data.append((iterations + 1, x0, f(x0)))
        iterations += 1

    return x0, data

# # Open the file only once
with open('./data.dat', 'w') as file:
    file.write("# Method, Iterations, f(x)\n")
    bisection_root, bisection_data = bisection_method(a, b)
    for row in bisection_data:
        file.write("Bisection, {}, {}\n".format(row[0], row[2]))
    
    secant_root, secant_data = secant_method(x0, x1)
    for row in secant_data:
        file.write("Secant, {}, {}\n".format(row[0], row[2]))

    newton_root, newton_data = newton_raphson_method(2.8)
    for row in newton_data:
        file.write("Newton-Raphson, {}, {}\n".format(row[0], row[2]))

    fixed_point_root, fixed_point_data = fixed_point_iteration_method(1)
    for row in fixed_point_data:
        file.write("Fixed-Point, {}, {}\n".format(row[0], row[2]))


print("Bisection method root:", bisection_root)
print("Secant method root:", secant_root)
print("Newton-Raphson method root:", newton_root)
print("Fixed-Point Iteration method root:", fixed_point_root)

