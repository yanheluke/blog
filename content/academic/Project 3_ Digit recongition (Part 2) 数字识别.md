---
title: "Project 3: Digit recongition (Part 2) 数字识别"
date: 2025-08-09
course: 6.86x
cover: "F0AF219D_image.png"
bear_pk: F0AF219D-6B23-484A-BA7F-79C78C5040DE
---

# **Project 3: Digit recongition (Part 2) 数字识别**

#Courses/MITx/6.86x
## 1. 用numpy写一个两层的前馈神经网络
### 模型结构：
![](../images/F0AF219D_image.png)
## 3. Activation Functions
The first step is to design the activation function for each neuron. In this problem, we will initialize the network weights to 1, use ReLU for the activation function of the hidden layers, and use an identity function for the output neuron. The hidden layer has a bias but the output layer does not. Complete the helper functions in neural_networks.py, including rectified_linear_unit and rectified_linear_unit_derivative, for you to use in the NeuralNetwork class, and implement them below.
## 4. Training the Network
Forward propagation is simply the summation of the previous layer's output multiplied by the weight of each wire, while back-propagation works by computing the partial derivatives of the cost function with respect to every weight or bias in the network. In back propagation, the network gets better at minimizing the error and predicting the output of the data being used for training by incrementally updating their weights and biases using stochastic gradient descent.
We are trying to estimate a continuous-valued function, thus we will use squared loss as our cost function and an identity function as the output activation function. f(x) is the activation function that is called on the input to our final layer output node, and is the predicted value, while is the actual value of the input. When you're done implementing the function train (below and in your local repository), run the script and see if the errors are decreasing. If your errors are all under 0.15 after the last training iteration then you have implemented the neural network training correctly.
$$ 
C =\frac{1}{2} * (y - \hat{a})^2
 $$
$$ 
f(x) = x 
$$
You'll notice that the train function inherits from NeuralNetworkBase in the codebox below; this is done for grading purposes. In your local code, you implement the function directly in your Neural Network class all in one file. The rest of the code in NeuralNetworkBase is the same as in the original NeuralNetwork class you have locally.
```python
import numpy as np
import math

"""
 ==================================
 Problem 3: Neural Network Basics
 ==================================
    Generates a neural network with the following architecture:
        Fully connected neural network.
        Input vector takes in two features.
        One hidden layer with three neurons whose activation function is ReLU.
        One output neuron whose activation function is the identity function.
"""

## 定义ReLu函数及其导数，注意都是标量形式
```python
def rectified_linear_unit(x):
    """ Returns the ReLU of x, or the maximum between 0 and x."""
    # TODO
    return(max(x,0))

def rectified_linear_unit_derivative(x):
    """ Returns the derivative of ReLU."""
    # TODO
    derivatives = 0
    if x>0:
        derivatives = 1
    else:
        derivatives = 0
    return(derivatives)

## 定义输出激活函数（恒等函数）及其导数，都是标量形式。
```python
def output_layer_activation(x):
    """ Linear function, returns input as is. """
    return x

def output_layer_activation_derivative(x):
    """ Returns the derivative of a linear function: 1. """
    return 1

class NeuralNetwork():
    """
        Contains the following functions:
            -train: tunes parameters of the neural network based on error obtained from forward propagation.
            -predict: predicts the label of a feature vector based on the class's parameters.
            -train_neural_network: trains a neural network over all the data points for the specified number of epochs during initialization of the class.
            -test_neural_network: uses the parameters specified at the time in order to test that the neural network classifies the points given in testing_points within a margin of error.
    """

    def __init__(self):

        # DO NOT CHANGE PARAMETERS (Initialized to floats instead of ints)
        self.input_to_hidden_weights = np.matrix('1. 1.; 1. 1.; 1. 1.')
        self.hidden_to_output_weights = np.matrix('1. 1. 1.')
        self.biases = np.matrix('0.; 0.; 0.')
        self.learning_rate = .001
        self.epochs_to_train = 10
        self.training_points = [((2,1), 10), ((3,3), 21), ((4,5), 32), ((6, 6), 42)]
        self.testing_points = [(1,1), (2,2), (3,3), (5,5), (10,10)]

    def train(self, x1, x2, y):

        ### Forward propagation ###
        input_values = np.matrix([[x1],[x2]]) # 2 by 1

        # Calculate the input and activation of the hidden layer
        ## 是否要添加biases? 根据题目的描述，hidden_layer有bias但output没有
        hidden_layer_weighted_input = self.input_to_hidden_weights @ input_values + self.biases # TODO (3 by 1 matrix)
        rectified_linear_unit_vec = np.vectorize(rectified_linear_unit)
        hidden_layer_activation = rectified_linear_unit_vec(hidden_layer_weighted_input)# TODO (3 by 1 matrix)

        output = self.hidden_to_output_weights @ hidden_layer_activation# TODO
        output_layer_activation_vec = np.vectorize(output_layer_activation)
        activated_output = output_layer_activation_vec(output) # TODO

        ### Backpropagation ###

        # Compute gradients
        ## output loss是平方损失函数，output_layer_error即为输出层误差
        output_layer_error = -(y - activated_output) # TODO
        ## 计算输出层激活函数的导数，虽然值恒为1，但代码要求完整写出来。
        output_derivative_vec = np.vectorize(output_layer_activation_derivative)
        output_layer_activation_derivative_vec = output_derivative_vec(output)
        out_layer_error = np.multiply(output_layer_error, output_layer_activation_derivative_vec)
        ## 隐藏层激活函数的导数
        rectified_linear_unit_derivative_vec = np.vectorize(rectified_linear_unit_derivative)
        ## 隐藏层误差是损失函数对隐藏层激活值的导数，具体计算等于hidden_to_out_weight的转置 * 输出层误差（因为这里只有一个隐藏层）⊙ 隐藏层激活函数的导数
        ## 反向传播误差 =  hidden_to_out_weight.T * 输出层误差
        ## 隐藏层误差 = 反向传播误差 ⊙ 隐藏层激活函数导数
        hidden_layer_error = np.multiply((self.hidden_to_output_weights.T @ output_layer_error),
                                         rectified_linear_unit_derivative_vec(hidden_layer_weighted_input))   # TODO (3 by 1 matrix)

        bias_gradients = hidden_layer_error # TODO
        hidden_to_output_weight_gradients = output_layer_error @ hidden_layer_activation.T # TODO
        input_to_hidden_weight_gradients = hidden_layer_error @ input_values.T# TODO

        # Use gradients to adjust weights and biases using gradient descent
        self.biases = self.biases - self.learning_rate*bias_gradients# TODO
        self.input_to_hidden_weights = self.input_to_hidden_weights - self.learning_rate*input_to_hidden_weight_gradients# TODO
        self.hidden_to_output_weights = self.hidden_to_output_weights - self.learning_rate*hidden_to_output_weight_gradients # TODO

    def predict(self, x1, x2):

        input_values = np.matrix([[x1],[x2]])

        # Compute output for a single input(should be same as the forward propagation in training)
        hidden_layer_weighted_input = self.input_to_hidden_weights @ input_values + self.biases # TODO
        relu_activation_vec = np.vectorize(rectified_linear_unit)
        hidden_layer_activation = relu_activation_vec(hidden_layer_weighted_input) # TODO
        output = self.hidden_to_output_weights @ hidden_layer_activation # TODO
        output_layer_activation_vec = np.vectorize(output_layer_activation)
        activated_output = output_layer_activation_vec(output)# TODO

        return activated_output.item()
    #
    # # Run this to train your neural network once you complete the train method
    def train_neural_network(self):

        for epoch in range(self.epochs_to_train):
            for x,y in self.training_points:
                self.train(x[0], x[1], y)
    #
    # # Run this to test your neural network implementation for correctness after it is trained
    def test_neural_network(self):

        for point in self.testing_points:
            print("Point,", point, "Prediction,", self.predict(point[0], point[1]))
            if abs(self.predict(point[0], point[1]) - 7*point[0]) < 0.1:
                print("Test Passed")
            else:
                print("Point ", point[0], point[1], " failed to be predicted correctly.")
                return

x = NeuralNetwork()

x.train_neural_network()


# UNCOMMENT THE LINE BELOW TO TEST YOUR NEURAL NETWORK
x.test_neural_network()
```

train()函数主要有以下两部分组成：
1. **前向传导**：
   1. hidden_layer_weighted_input（隐藏层加权输入）：```input_to_hidden_weights @ input_values + self.biases``` 。注意这里需要参数在前，特征在后
   2. 对隐藏层的激活函数ReLu向量化，用np.vectorize(func)实现
   3. 计算隐藏层的激活值：```hidden_layer_activation = rectified_linear_unit_vec(hidden_layer_weighted_input)```
   4. 计算```output: hidden_to_output_weights @ hidden_layer_activation``` 同样是权重参数在前，特征在后
   5. 对输出层激活函数向量化后计算输出层激活值：```activated_output = output_layer_activation_vec(output)```

总的来说前向传导是比较简单的，按部就班计算

2. **反向传播** 
这部分比较复杂 

3. **计算输出层的误差error**
   1. ```output_layer_error = -(y - activated_output)```。完整的写法应该是```out_layer_error = np.multiply(output_layer_error, output_layer_activation_derivative_vec)```,计算输出层对activated_output求导的结果再与输出层激活函数偏导逐元素相乘。

````python
# Compute gradients
## output loss是平方损失函数，output_layer_error即为输出层误差
output_layer_error = -(y - activated_output) # TODO
## 计算输出层激活函数的导数，虽然值恒为1，但代码要求完整写出来。
output_derivative_vec= np.vectorize(output_layer_activation_derivative)
output_layer_activation_derivative_vec = output_derivative_vec(output)
out_layer_error = np.multiply(output_layer_error, output_layer_activation_derivative_vec)
````

计算隐藏层误差error： 这里是先求反向传播误差，即用hidden_to_out_weight的转置 * 输出层误差 再求隐藏层误差：反向传播误差⊙ 隐藏层激活函数的导数

```python
## 隐藏层激活函数的导数
rectified_linear_unit_derivative_vec = np.vectorize(rectified_linear_unit_derivative)
## 隐藏层误差是损失函数对隐藏层激活值的导数，具体计算等于hidden_to_out_weight的转置 * 输出层误差（因为这里只有一个隐藏层）⊙ 隐藏层激活函数的导数hidden_layer_error = np.multiply((self.hidden_to_output_weights.T @ output_layer_error),rectified_linear_unit_derivative_vec(hidden_layer_weighted_input))
```
1 计算梯度
* bias_gradients：偏置项的梯度即为隐藏项误差
* hidden_to_output_weight_gradients：隐藏层到输出层的权重梯度为：**输出层误差 @ 隐藏层的激活值转置（隐藏层的激活值为隐藏层ReLu结果）**
* input_to_hidden_weight_gradients：输入层到隐藏层的权重梯度为：**隐藏层误差 @ 输入层的激活值转置（输入层激活函数为恒等函数）

```python
bias_gradients = hidden_layer_error # TODO
hidden_to_output_weight_gradients = output_layer_error @ hidden_layer_activation.T # TODO
input_to_hidden_weight_gradients = hidden_layer_error @ input_values.T# TODO
```

1 梯度更新 self.biases = self.biases - self.learning_rate* bias_gradients

⠀self.input_to_hidden_weights = self.input_to_hidden_weights - self.learning_rate* input_to_hidden_weight_gradients
self.hidden_to_output_weights = self.hidden_to_output_weights - self.learning_rate* hidden_to_output_weight_gradients

## 5. Predicting the Test Data
```python

class NeuralNetwork(NeuralNetworkBase):

    def predict(self, x1, x2):

        input_values = np.matrix([[x1],[x2]])

        # Compute output for a single input(should be same as the forward propagation in training)
        hidden_layer_weighted_input = self.input_to_hidden_weights @ input_values + self.biases # TODO
        relu_activation_vec = np.vectorize(rectified_linear_unit)
        hidden_layer_activation = relu_activation_vec(hidden_layer_weighted_input) # TODO
        output = self.hidden_to_output_weights @ hidden_layer_activation # TODO
        output_layer_activation_vec = np.vectorize(output_layer_activation)
        activated_output = output_layer_activation_vec(output)# TODO

        return activated_output.item()
```
## 8. Fully-Connected Neural Networks
| **model** | **val accuracy** | **test accuracy** |
|:-:|:-:|:-:|
| baseline | 0.932487 | 0.9204727564102564 |
| batch size 64 | 0.940020 | 0.9314903846153846 |
| learning rate 0.01 | 0.918179 | 0.9206730769230769 |
| momentum 0.9 | 0.902072 | 0.8891225961538461 |
| LeakyReLu activation | 0.931985 | 0.9207732371794872 |
### Improving Accuracy - Hidden 128
hidden representation size 10 -> 128
| **model** | **val accuracy** | **test accuracy** |
|:-:|:-:|:-:|
| baseline | 0.978275 |  |
| batch size 64 | 0.976310 |  |
| learning rate 0.01 | 0.955047 |  |
| momentum 0.9 | 0.969084 |  |
| LeakyReLu activation | 0.978944 |  |
## 9. Convolutional Neural Networks
用torch搭积木
```python
model = nn.Sequential(
              nn.Conv2d(1, 32, (3, 3)),
              nn.ReLU(),
              nn.MaxPool2d((2, 2)),
              nn.Conv2d(in_channels=32, out_channels=64, kernel_size=(3,3)),
              nn.ReLU(),
              nn.MaxPool2d((2, 2)),
              Flatten(),
              nn.Linear(1600, 128),
              nn.Dropout(0.5),
              nn.Linear(128, 10)
        )

### 10. Overlapping, multi-digit MNIST
### Fully connected network
class MLP(nn.Module):

    def __init__(self, input_dimension):
        super(MLP, self).__init__()
        self.flatten = Flatten()
        # TODO initialize model layers here
        self.hidden = nn.Linear(input_dimension, 64)
        self.out1 = nn.Linear(64, 10)
        self.out2 = nn.Linear(64, 10)

    def forward(self, x):
        xf = self.flatten(x)
        x = self.flatten(x)
        x = F.relu(self.hidden(x))
        out_first_digit = self.out1(x)
        out_second_digit = self.out2(x)
        # TODO use model layers to predict the two digits

        return out_first_digit, out_second_digit
```
### Convolutional model
```python
class CNN(nn.Module):

    def __init__(self, input_dimension):
        super(CNN, self).__init__()
        # TODO initialize model layers here
        self.conv_layers = nn.Sequential(
            nn.Conv2d(1, 32, (3,3)),
            nn.ReLU(),
            nn.MaxPool2d((2,2)),
            nn.Conv2d(32, 64, (3,3)))

        self.fc = Flatten()
        self.linear = nn.Linear(12672, 64)
        self.dropout = nn.Dropout(0.5)
        self.out1 = nn.Linear(64, 10)
        self.out2 = nn.Linear(64, 10)

    def forward(self, x):

        # TODO use model layers to predict the two digits
        x = self.conv_layers(x)
        x = self.fc(x)
        x = self.linear(x)
        x = self.dropout(x)
        out_first_digit = self.out1(x)
        out_second_digit = self.out2(x)

        return out_first_digit, out_second_digit

