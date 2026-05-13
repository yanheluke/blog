---
title: "Lecture 7. Computing the Maximum Likelihood Estimator 计算极大似然估计量"
date: 2025-08-10
course: 18.6501x
cover: "6FF87CD3_image.png"
bear_pk: 6FF87CD3-5F76-47C4-98D0-03E6CF8233C4
---

# Lecture 7. Computing the Maximum Likelihood Estimator 计算极大似然估计量
#Courses/MITx/18.6501x


## 1. Objectives
### Maximum Likelihood Estimation
At the end of this lecture, you will be able to do the following:
* Compute the likelihood of discrete and continuous distributions.
* Interpret the **maximum likelihood estimator** as the objective value of an optimization problem.
* Define and **compute** the maximum likelihood estimator of an unknown parameter.
* **Maximize** a **strictly concave** function in one dimension.

⠀
## 2. Review and Likelihood of a Gaussian Distribution
**Concept Check: Likelihoods of a Bernoulli, a Poisson, and a Gaussian Distribution**
![](../images/6FF87CD3_image.png)
![](../images/6FF87CD3_image 2.png)

## 3. Likelihood of an Exponential Distribution
![](../images/6FF87CD3_image 3.png)
注意这里的指示函数。如果指示函数依赖于未知参数（unknown parameter），需要在公式中保留指示函数（并且用一种巧妙的方法，例如if min x_i >0）；但在本门课上都假设是wel-definied model, 所以不依赖未知参数的指示函数可以不用写。
![](../images/6FF87CD3_image 4.png)

**练习题：Product of Indicators**
TBC

## 4. Likelihood of a Uniform Distribution
![](../images/6FF87CD3_image 5.png)
![](../images/6FF87CD3_image 6.png)
同样的问题，注意这里的指示函数是如何变形和化简的

## 5. Likelihood of a Mixture of Gaussians
![](../images/6FF87CD3_image 7.png)
![](../images/6FF87CD3_image 8.png)
![](../images/6FF87CD3_image 9.png)

## 6. Maximum Likelihood Estimator
**Definition of Maximum Likelihood Estimator and Log Likelihood**
![](../images/6FF87CD3_image 10.png)
![](../images/6FF87CD3_image 11.png)

## 7. Interlude: Minimizing and Maximizing Functions
![](../images/6FF87CD3_image 12.png)

## 8. Worked examples: Concavity in 1 dimension
![](../images/6FF87CD3_image 13.png)

## 9. Strictly Concave Functions and Unique Maximizer
![](../images/6FF87CD3_image 14.png)