---
title: "Lecture 8. Introduction to Feedforward Neural Networks 前馈神经网络导论"
date: 2025-08-09
course: 6.86x
cover: "1256F483_image.png"
bear_pk: 1256F483-4F2A-4506-8946-150C6FEC9BC2
---

# **Lecture 8. Introduction to Feedforward Neural Networks 前馈神经网络导论**

#Courses/MITx/6.86x

## 1. Unit 3 Overview
At the end of this unit, you will be able to

- Implement a **feedforward neural networks** from scratch to perform image classification task.
- Write down the gradient of the loss function with respect to the weight parameters using **back-propagation** algorithm and use SGD to train neural networks.
- Understand that **Recurrent Neural Networks (RNNs)** and **long short-term memory (LSTM)** can be applied in modeling and generating sequences.
- Implement a **Convolutional neural networks (CNNs)** with machine learning packages.

## 2. Objectives
**Introduction to Feedforward Neural Networks**  

At the end of this lecture, you will be able to
- Recognize different **layers** in a **feedforward neural network** and the number of **units** in each layer.
- Write down common **activation functions** such as the hyperbolic tangent function , and the **rectified linear function (ReLU)** .
- Compute the output of a simple neural network possibly with **hidden layers** given the **weights** and **activation functions** .
- Determine whether data after transformation by some layers is linearly separable, draw decision boundaries given by the weight vectors and use them to help understand the behavior of the network.

## 3. Motivation
Motivation to Neural Networks
![](../images/1256F483_image.png)
### 4. Neural Network Units
![](../images/1256F483_image 2.png)

## 5. Introduction to Deep Neural Networks
一道练习题：Representation Power of Neural Networks: 2
![](../images/1256F483_image 3.png)<!-- {"width":377} -->![](../images/1256F483_image 4.png)<!-- {"width":313} -->

答案：
![](../images/1256F483_image 5.png)
这道题直接去推导反而比较痛苦，用德摩根定律（De Morgan's Law）来做比较方便：
德摩根定律：
1. 第一定律： NOT(A AND B) = NOT(A) OR NOT(B)
2. 第二定律：NOT(A OR B) = NOT(A) AND NOT(B)
德摩根定律的推导：
1. NAND门：NAND(A,B) = NOT(A AND B)
2. NOR门：NOR(A, B) = NOT(A OR B)
NOT(x) = NAND(x, x) = NOT(x AND x)
所以这道题里：
第一个图想表达的是：NAND(x1, x1)  = NOT(x1 AND x1) = NOT(x1)
第二个图想表达的是：NAND(NAND(x1, x1) AND NAND(x2, x2)) = NAND(NOT(x1) and NOT(x2)) = NOT(NOT(x1 OR x2)) = OR(x1, x2)

> 妈的头都看晕了

## 6. Hidden Layer Models

一道练习题：
![](../images/1256F483_image 6.png)
![](../images/1256F483_image 7.png)答案是：
![](../images/1256F483_image 8.png)
注意也可以带入数值进行计算（算起来比较麻烦），以B为例，带入之后的计算：
D ={[-9, 7], 1}, {[-1, -1], -1}, {[-1, -1], -1}, {[7, -9], 1}
带入C得到的D的集合和B选项是对称的
这个时候会发现三个点在二维平面上是在一条直线上，即，线性不可分。但我一开始画图画错了所以选错了:(
另外答案给出了一个法则：**对于原本线性不可分的问题，对特征空间做线性变换，也一样保持线性不可分。**

问题2：
![](../images/1256F483_image 9.png)
这里我就不再计算了，猜测所有非线性变换均可分。如果一定要计算，可以这样：
RELU(z):
![](../images/1256F483_image 10.png)
tanh(z):
![](../images/1256F483_image 11.png)
