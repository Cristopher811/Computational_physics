from sympy import *

M = Matrix([(0, 2 - 3*1j, 4 - 5*1j), (2 + 3*1j, 1, 6 - 7*1j), (4 + 5*1j, 6 + 7*1j, 2)])
poly = M.charpoly('t').as_expr()
print(poly)
roots = solve(poly,'t')
print(roots)

