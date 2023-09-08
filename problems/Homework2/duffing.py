import sympy as sp

t = sp.Symbol('t')
x = sp.Function('x')(t)
omega = sp.Symbol('omega')
gamma = sp.Symbol('gamma')
alpha = sp.Symbol('alpha')
epsilon = sp.Symbol('epsilon')

# Define the equation and initial conditions
equation = sp.Eq(x.diff(t, t) + 2 * gamma * x.diff(t) + omega**2 * x + alpha * x**3, 0)
initial_conditions = [x.subs(t, 0), x.diff(t).subs(t, 0)]

# Perform variable substitution
x_solution = sp.Symbol('x0')
for i in range(1, 4):
    x_solution += epsilon**i * sp.Symbol(f'x{i}')
    equation = equation.subs(x.diff(t, i), sp.diff(x_solution, t, i))

# Expand the equation series and solve recursively
equation = equation.series(epsilon, 0, 1).removeO().as_poly(x_solution)
leading_coeff = equation.LC()
equation = equation / leading_coeff

for i in range(1, 4):
    equation = equation.coeff_monomial(epsilon**i).as_poly()
    solutions = sp.solve(equation, sp.Symbol(f'x{i}'))
    x_solution = x_solution.subs(solutions)

# Substitute the initial conditions
x_solution = x_solution.subs(sp.Symbol('x0'), initial_conditions[0])
x_solution = x_solution.subs(sp.Symbol('x1'), initial_conditions[1])

# Print the final solution
print(x_solution)

