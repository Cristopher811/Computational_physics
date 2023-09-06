from sympy import *


#M = Matrix([(0, 2 - 3*1j, 4 - 5*1j), (2 + 3*1j, 1, 6 - 7*1j), (4 + 5*1j, 6 + 7*1j, 2)])
#poly = M.charpoly('t').as_expr()
#print(poly)
#roots = solve(poly,'t')
#print(roots)
a = symbols('a') #0.0218223
b = symbols('b') #0.5155
c = symbols('c') #0.912576
d = symbols('d') #0.826651
e = symbols('e') #0.623182
f = symbols('f') #0.956454
g = symbols('g') #0.0969188
h = symbols('h') #0.687078
i = symbols('i') #0.263188
j = symbols('j') #0.703272
k = symbols('k') #0.588884
l = symbols('l') #0.594529
m = symbols('m') #0.744659
n = symbols('n') #0.740852
o = symbols('o') #0.0227753
p = symbols('p') #0.322981
q = symbols('q') #0.439351
r = symbols('r') #0.718962
s = symbols('s') #0.639898
t = symbols('t') #0.493646
u = symbols('u') #0.818529
v = symbols('v') #0.0790925
x = symbols('x') #0.193402
y = symbols('y') #0.300335
z = symbols('z') #0.71027
a1 = symbols('a1') #0.100481
b1 = symbols('b1') #0.438632
c1 = symbols('c1') #0.693687
d1 = symbols('d1') 
e1 = symbols('e1')
f1 = symbols('f1')
g1 = symbols('g1')
h1 = symbols('h1')
i1 = symbols('i1')
j1 = symbols('j1')
k1 = symbols('k1')
l1 = symbols('l1')
m1 = symbols('m1')
n1 = symbols('n1')
o1 = symbols('o1')
p1 = symbols('p1')
q1 = symbols('q1')
r1 = symbols('r1')
s1 = symbols('s1')
t1 = symbols('t1')
u1 = symbols('u1')
v1 = symbols('v1')
x1 = symbols('x1')
y1 = symbols('y1')
z1 = symbols('z1')
a2 = symbols('a2')
b2 = symbols('b2')
c2 = symbols('c2')
d2 = symbols('d2')
e2 = symbols('e2')
f2 = symbols('f2')
g2 = symbols('g2')
h2 = symbols('h2')
i2 = symbols('i2')
j2 = symbols('j2')
k2 = symbols('k2')
l2 = symbols('l2')
m2 = symbols('m2')
n2 = symbols('n2')
o2 = symbols('o2')
p2 = symbols('p2')
q2 = symbols('q2')
r2 = symbols('r2')
s2 = symbols('s2')
t2 = symbols('t2')
u2 = symbols('u2')
v2 = symbols('v2')
x2 = symbols('x2')
y2 = symbols('y2')
z2 = symbols('z2')
a3 = symbols('a3')
b3 = symbols('b3')
c3 = symbols('c3')
d3 = symbols('d3')
e3 = symbols('e3')
f3 = symbols('f3')
g3 = symbols('g3')
h3 = symbols('h3')
i3 = symbols('i3')
j3 = symbols('j3')
k3 = symbols('k3')
l3 = symbols('l3')
m3 = symbols('m3')
n3 = symbols('n3')
o3 = symbols('o3')
p3 = symbols('p3')
q3 = symbols('q3')
r3 = symbols('r3')
s3 = symbols('s3')
t3 = symbols('t3')
u3 = symbols('u3')
v3 = symbols('v3')
x3 = symbols('x3')
y3 = symbols('y3')
z3 = symbols('z3')
a4 = symbols('a4')




M = Matrix([(a, b + c*1j, d + e*1j, 
  f + g*1j, h + i*1j, 
  j + k*1j, l + m*1j, 
  n + o*1j, p + q*1j, 
  r + s*1j), (b - c*1j, t, 
  u + v*1j, x + y*1j, z + a1*1j,
  b1 + c1*1j, d1 + e1*1j, 
  f1 + g1*1j, h1 + i1*1j, 
  j1 + k1*1j), (d - e*1j, 
  u - v*1j, l1, m1 + n1*1j, 
  o1 + p1*1j, q1 + r1*1j, s1 + t1*1j, 
  v1 + x1*1j, y1 + z1*1j, 
  a2 + b2*1j), (f - g*1j, 
  x - y*1j, m1 - n1*1j, c2, 
  d2 + e2*1j, f2 + g2*1j, 
  h2 + i2*1j, j2 + k2*1j, 
  l2 + m2*1j, 
  n2 + o2*1j), (h - i*1j, 
  z - a1*1j, o1 - p1*1j, d2 - e2*1j, 
  p2, q2 + r2*1j, s2 + t2*1j, 
  u2 + v2*1j, x2 + y2*1j, 
  z2 + a3*1j), (j - k*1j, 
  b1 - c1*1j, q1 - r1*1j, f2 - g2*1j,
  q2 - r2*1j, b3, c3 + d3*1j, 
  e3 + f3*1j, g3 + h3*1j, 
  i3 + j3*1j), (l - m*1j, 
  d1 - e1*1j, s1 - t1*1j, 
  h2 - i2*1j, s2 - t2*1j, c3 - d3*1j,
  k3, l3 + m3*1j, n3 + o3*1j, 
  p3 + q3*1j), (n - o*1j, 
  f1 - g1*1j, v1 - x1*1j, j2 - k2*1j,
  u2 - v2*1j, e3 - f3*1j, 
  l3 - m3*1j, r3, s3 + t3*1j, 
  u3 + v3*1j), (p - q*1j, 
  h1 - i1*1j, y1 - z1*1j, l2 - m2*1j,
  x2 - y2*1j, g3 - h3*1j, 
  n3 - o3*1j, s3 - t3*1j, x3, 
  y3 + z3*1j), (r - s*1j, 
  j1 - k1*1j, a2 - b2*1j, 
  n2 - o2*1j, z2 - a3*1j, 
  i3 - j3*1j, p3 - q3*1j, 
  u3 - v3*1j, y3 - z3*1j, a4)])

#M = Matrix([(0.0218223, 0.5155 + 0.912576*1j, 0.826651 + 0.623182*1j, 
#  0.956454 + 0.0969188*1j, 0.687078 + 0.263188*1j, 
#  0.703272 + 0.588884*1j, 0.594529 + 0.744659*1j, 
#  0.740852 + 0.0227753*1j, 0.322981 + 0.439351*1j, 
#  0.718962 + 0.639898*1j), (0.5155 - 0.912576*1j, 0.493646, 
#  0.818529 + 0.0790925*1j, 0.193402 + 0.300335*1j, 0.71027 + 0.100481*1j,
#   0.438632 + 0.693687*1j, 0.469004 + 0.147506*1j, 
#  0.0391713 + 0.416985*1j, 0.950953 + 0.479195*1j, 
#  0.206296 + 0.471403*1j), (0.826651 - 0.623182*1j, 
#  0.818529 - 0.0790925*1j, 0.247069, 0.70106 + 0.235976*1j, 
#  0.296243 + 0.82543*1j, 0.269689 + 0.193637*1j, 0.352129 + 0.397277*1j, 
#  0.359598 + 0.82502*1j, 0.335125 + 0.653082*1j, 
#  0.616255 + 0.739524*1j), (0.956454 - 0.0969188*1j, 
#  0.193402 - 0.300335*1j, 0.70106 - 0.235976*1j, 0.496152, 
#  0.910764 + 0.0192807*1j, 0.714587 + 0.272796*1j, 
#  0.0172226 + 0.789958*1j, 0.173434 + 0.702186*1j, 
#  0.816804 + 0.394997*1j, 
#  0.544215 + 0.0222391*1j), (0.687078 - 0.263188*1j, 
#  0.71027 - 0.100481*1j, 0.296243 - 0.82543*1j, 0.910764 - 0.0192807*1j, 
#  0.560873, 0.393243 + 0.456964*1j, 0.203853 + 0.36579*1j, 
#  0.928525 + 0.720979*1j, 0.862977 + 0.271044*1j, 
#  0.956085 + 0.483294*1j), (0.703272 - 0.588884*1j, 
#  0.438632 - 0.693687*1j, 0.269689 - 0.193637*1j, 0.714587 - 0.272796*1j,
#   0.393243 - 0.456964*1j, 0.42305, 0.583194 + 0.885582*1j, 
#  0.716655 + 0.508044*1j, 0.976432 + 0.187657*1j, 
#  0.599583 + 0.695341*1j), (0.594529 - 0.744659*1j, 
#  0.469004 - 0.147506*1j, 0.352129 - 0.397277*1j, 
#  0.0172226 - 0.789958*1j, 0.203853 - 0.36579*1j, 0.583194 - 0.885582*1j,
#   0.0826443, 0.417235 + 0.429801*1j, 0.773897 + 0.724955*1j, 
#  0.0861904 + 0.676794*1j), (0.740852 - 0.0227753*1j, 
#  0.0391713 - 0.416985*1j, 0.359598 - 0.82502*1j, 0.173434 - 0.702186*1j,
#   0.928525 - 0.720979*1j, 0.716655 - 0.508044*1j, 
#  0.417235 - 0.429801*1j, 0.767398, 0.548094 + 0.32195*1j, 
#  0.464068 + 0.345542*1j), (0.322981 - 0.439351*1j, 
#  0.950953 - 0.479195*1j, 0.335125 - 0.653082*1j, 0.816804 - 0.394997*1j,
#   0.862977 - 0.271044*1j, 0.976432 - 0.187657*1j, 
#  0.773897 - 0.724955*1j, 0.548094 - 0.32195*1j, 0.983154, 
#  0.236963 + 0.318349*1j), (0.718962 - 0.639898*1j, 
#  0.206296 - 0.471403*1j, 0.616255 - 0.739524*1j, 
#  0.544215 - 0.0222391*1j, 0.956085 - 0.483294*1j, 
#  0.599583 - 0.695341*1j, 0.0861904 - 0.676794*1j, 
#  0.464068 - 0.345542*1j, 0.236963 - 0.318349*1j, 0.174793)])

poly = M.charpoly('t').as_expr()
print(poly)
#roots = solve(poly,'t')
#print(roots)

