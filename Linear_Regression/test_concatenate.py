import numpy as np

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6]])

c = np.concatenate((a, b), axis=0)
print("Check 1 : ")
print(c)

d = np.concatenate((a, b), axis=None)
print("Check 2 : ")
print(d)

e = np.concatenate((a, b.T), axis=1)
print("Check 3 : ")
print(e)

f = np.concatenate((a.T, b.T), axis=1)
print("Check 4 : ")
print(f)

# failure
# g = np.concatenate((a, b.T), axis=1)
# print("Check 5 : ")
# print(g)

