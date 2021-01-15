import numpy as np



A = np.array([1,2,0,-1,3,4,3,-4,0])
A = np.reshape(A,(3,3))
Y = np.array([2 , -2 , 4])

# A_inv = np.linalg.inv(A)
# X = A_inv.dot(Y)
X = np.linalg.solve(A, Y)
print("\n")
print("solution [a , b , c] = " , X)
print("\n")

Adet = np.linalg.det(A)
print("Det (A) = " , format(Adet,'.2f') , Adet)
print("\n")

