"""
A simple perceptron class using numpy
Uses very archaic training and activation functions
Sign class is not accurate, just made the perceptron easier to code.
"""

import numpy as np
from math import exp
from random import randint

# sigmoid class for activation function
def sigmoid(z):
    return (1/(1 + exp(-z)))


# sign class for activation function
def sign(z):
    if z >= 0: return 1
    else: return 0



class Perceptron:

    def __init__(self,num_inputs):

        # Set a variabel for number of input neurons
        self.num_inputs = num_inputs
        # Create an "empty" weights matrix
        self.weights = np.zeros((1,self.num_inputs))

        # Initialize weights randomly as an array
        for i in range(len(self.weights)):
            for k in range(len(self.weights[i])):
                self.weights[i][k] = randint(-10,10)
    
    def setWeights(self):

        # Convert weights to matrix format
        self.weights_matrix = np.asmatrix(self.weights)

    def guess(self, inputs):
        
        # Set inputs array as a matrix
        inputs_matrix = np.reshape(np.asmatrix(inputs),(self.num_inputs,1))

        #calculate and return weighted sums as matrix
        weighted_sum = np.matmul(self.weights,inputs_matrix)

        #activate weighted sum
        output = sign(weighted_sum)


        return output

    def train(self, inputs, target):

        # make an initial guess to train off of
        first = self.guess(inputs)

        #calulate error
        error = target - first

        #adjust weights based of off error
        for i in range(len(self.weights[0])):
            # optional leraning rate
            delta_w = error * inputs[i] # * 0.001
            self.weights[0][i] += delta_w







