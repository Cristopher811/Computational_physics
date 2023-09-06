import numpy as np
from numpy.linalg import det
from numpy.linalg import eig

a = np.array([(0.0218223, 0.5155 + 0.912576*1j, 0.826651 + 0.623182*1j, 
  0.956454 + 0.0969188*1j, 0.687078 + 0.263188*1j, 
  0.703272 + 0.588884*1j, 0.594529 + 0.744659*1j, 
  0.740852 + 0.0227753*1j, 0.322981 + 0.439351*1j, 
  0.718962 + 0.639898*1j), (0.5155 - 0.912576*1j, 0.493646, 
  0.818529 + 0.0790925*1j, 0.193402 + 0.300335*1j, 0.71027 + 0.100481*1j,
   0.438632 + 0.693687*1j, 0.469004 + 0.147506*1j, 
  0.0391713 + 0.416985*1j, 0.950953 + 0.479195*1j, 
  0.206296 + 0.471403*1j), (0.826651 - 0.623182*1j, 
  0.818529 - 0.0790925*1j, 0.247069, 0.70106 + 0.235976*1j, 
  0.296243 + 0.82543*1j, 0.269689 + 0.193637*1j, 0.352129 + 0.397277*1j, 
  0.359598 + 0.82502*1j, 0.335125 + 0.653082*1j, 
  0.616255 + 0.739524*1j), (0.956454 - 0.0969188*1j, 
  0.193402 - 0.300335*1j, 0.70106 - 0.235976*1j, 0.496152, 
  0.910764 + 0.0192807*1j, 0.714587 + 0.272796*1j, 
  0.0172226 + 0.789958*1j, 0.173434 + 0.702186*1j, 
  0.816804 + 0.394997*1j, 
  0.544215 + 0.0222391*1j), (0.687078 - 0.263188*1j, 
  0.71027 - 0.100481*1j, 0.296243 - 0.82543*1j, 0.910764 - 0.0192807*1j, 
  0.560873, 0.393243 + 0.456964*1j, 0.203853 + 0.36579*1j, 
  0.928525 + 0.720979*1j, 0.862977 + 0.271044*1j, 
  0.956085 + 0.483294*1j), (0.703272 - 0.588884*1j, 
  0.438632 - 0.693687*1j, 0.269689 - 0.193637*1j, 0.714587 - 0.272796*1j,
   0.393243 - 0.456964*1j, 0.42305, 0.583194 + 0.885582*1j, 
  0.716655 + 0.508044*1j, 0.976432 + 0.187657*1j, 
  0.599583 + 0.695341*1j), (0.594529 - 0.744659*1j, 
  0.469004 - 0.147506*1j, 0.352129 - 0.397277*1j, 
  0.0172226 - 0.789958*1j, 0.203853 - 0.36579*1j, 0.583194 - 0.885582*1j,
   0.0826443, 0.417235 + 0.429801*1j, 0.773897 + 0.724955*1j, 
  0.0861904 + 0.676794*1j), (0.740852 - 0.0227753*1j, 
  0.0391713 - 0.416985*1j, 0.359598 - 0.82502*1j, 0.173434 - 0.702186*1j,
   0.928525 - 0.720979*1j, 0.716655 - 0.508044*1j, 
  0.417235 - 0.429801*1j, 0.767398, 0.548094 + 0.32195*1j, 
  0.464068 + 0.345542*1j), (0.322981 - 0.439351*1j, 
  0.950953 - 0.479195*1j, 0.335125 - 0.653082*1j, 0.816804 - 0.394997*1j,
   0.862977 - 0.271044*1j, 0.976432 - 0.187657*1j, 
  0.773897 - 0.724955*1j, 0.548094 - 0.32195*1j, 0.983154, 
  0.236963 + 0.318349*1j), (0.718962 - 0.639898*1j, 
  0.206296 - 0.471403*1j, 0.616255 - 0.739524*1j, 
  0.544215 - 0.0222391*1j, 0.956085 - 0.483294*1j, 
  0.599583 - 0.695341*1j, 0.0861904 - 0.676794*1j, 
  0.464068 - 0.345542*1j, 0.236963 - 0.318349*1j, 0.174793)])

w,v = eig(a)

print("Eigenvalue: " ,w)
print("Eigenvector: ",v)

