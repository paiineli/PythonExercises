import numpy as np

# activation function = step function

print(30 * "-")

def step_function(x):
  return 1 if x > 0 else 0

# perceptron (artificial neuron)
def perceptron(input_data, weights):
  # calculates the weighted sum of inputs and weights
  weighted_sum = np.dot(input_data, weights)
  # applies the activation function
  output = step_function(weighted_sum)
  return output

# synaptic weights (perceptron weights)
weights = np.array([0.5, 0.5]) # random initialization

# input data
input_data = np.array([0.2, 0.3])

# calculates the perceptron's output
output = perceptron(input_data, weights)

# displays the output
print("Perceptron output: ", output)

print(30 * "-")
