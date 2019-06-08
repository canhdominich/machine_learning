from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt

# height (cm), input data, each row is a data point
X = np.array([[147, 150, 153, 158, 163, 165, 168, 170, 173, 175, 178, 180, 183]]).T
# weight (kg)
y = np.array([ 49, 50, 51, 54, 58, 59, 60, 62, 63, 64, 66, 67, 68])


# Building Xbar
one = np.ones((X.shape[0], 1))
Xbar = np.concatenate((one, X), axis = 1) # each point is one row

# Calculating weights of the fitting line
A = np.dot(Xbar.T, Xbar)
b = np.dot(Xbar.T, y)
w = np.dot(np.linalg.pinv(A), b)

# (weight) = w_1 *(height) + w_0
w_0 = w[0]
w_1 = w[1]

def predict(height):
    return (w_0 + w_1*height)

#set test : 155cm - 52kg, 160cm = 56kg
print("Input : height = 155 cm thi thuc te weight =  52 kg. Du doan weight = ",predict(155))

print("Input : height = 160 cm thi thuc te weight =  56 kg. Du doan weight = ",predict(160))


