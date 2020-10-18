from random import randint
from math import exp, sqrt
import numpy as np


def map(f,mat):
    arr = np.asarray_chkfinite(mat)

    for i in range(len(arr)):
        for k in range(len(arr[0])):
            arr[i][k] = f(arr[i][k])

    mat = np.asmatrix(arr)

    return mat

def sigmoid(z):

    return 1/(1 + exp(-z))

def sign(z):

    if z > 0:
        return 1

    else:
        return 0


class NeuralNetwork:

    def __init__(self,num_inputs,num_hiddens,num_outputs):

        self.num_inputs = num_inputs
        self.num_hiddens = num_hiddens
        self.num_outputs = num_outputs

    def initiate_weights(self):

        self.weights_ih = np.zeros((self.num_hiddens,self.num_inputs))
        for i in range(self.num_hiddens):
            for j in range(self.num_inputs):
                self.weights_ih[i][j] = randint(-1,1)
                if self.weights_ih >= 0:
                    self.weights_ih += 50
                else:
                    self.weights_ih -= 50
        self.weights_ih = np.asmatrix(self.weights_ih)

        self.weights_ho = np.zeros((self.num_outputs,self.num_hiddens))
        for i in range(self.num_outputs):
            for j in range(self.num_hiddens):
                self.weights_ho[i][j] = randint(-1,1)
                if self.weights_ho >= 0:
                    self.weights_ho += 50
                else:
                    self.weights_ho -= 50
        self.weights_ho = np.asmatrix(self.weights_ho)

    def initiate_bias(self):

        self.bias_h = []
        self.bias_o = []

        for i in range(self.num_hiddens):
            self.bias_h.append(randint(-5,6))
        
        self.bias_h = np.asmatrix(self.bias_h)
        self.bias_h = np.reshape(self.bias_h,(self.num_hiddens,1))

        for i in range(self.num_hiddens):
            self.bias_o.append(randint(-5,6))
        
        self.bias_o = np.asmatrix(self.bias_h)
        self.bias_o = np.reshape(self.bias_o,(self.num_outputs,1))


    def guess(self,inputs):
        
        inputs_matrix = np.asmatrix(inputs)
        inputs_matrix = np.reshape(inputs_matrix,(self.num_inputs,1))
        
        self.weighted_h = np.matmul(self.weights_ih,inputs_matrix)

        self.activations_h = map(sigmoid,self.weighted_h)

        self.activations_h = self.activations_h + self.bias_h

        self.weighted_o = np.matmul(self.weights_ho,self.activations_h)

        self.outputs = map(sigmoid,self.weighted_o)

        self.outputs = self.outputs + self.bias_o

        return self.outputs

    def train(self,inputs,target):
        #backprop here
        pass
