---
title: "Lecture 8. Examples of Maximum Likelihood Estimators 极大似然估计量的例子"
date: 2025-08-10
course: 18.6501x
cover: "1CB3CF0F_image.png"
bear_pk: 1CB3CF0F-DCE4-43FF-9864-BBC4AAC605CD
---

# Lecture 8. Examples of Maximum Likelihood Estimators 极大似然估计量的例子
#Courses/MITx/18.6501x

## 1. Examples of Maximum Likelihood Estimators
**Objectives**
At the end of this lecture, you will be able to compute the maximum likelihood estimator in a variety of models including: Bernoulli, Poisson, Gaussian, Uniform.
You will also learn about mixtures of Gaussians as a flexible statistical model and you will be able to apply the Expectation-Maximization (EM) algorithm to compute the maximum likelihood estimator in this model.

## 2. Examples of Maximum Likelihood Estimators: Bernoulli Model
![](../images/1CB3CF0F_image.png)
### Maximum Likelihood Estimator of a Bernoulli Statistical Model I
TBC

## 3. Examples of Maximum Likelihood Estimators: Poisson Model
![](../images/1CB3CF0F_image 2.png)
### Maximum Likelihood Estimator of a Poisson Statistical Model
TBC

## 4. Maximum Likelihood Estimator of Gaussian Statistical Model
**Maximum Likelihood Estimator of Gaussian Statistical Model: the mean**
![](../images/1CB3CF0F_image 3.png)
![](../images/1CB3CF0F_image 4.png)

**Maximum Likelihood Estimator of Gaussian Statistical Model: the Variance**
![](../images/1CB3CF0F_image 5.png)
![](../images/1CB3CF0F_image 6.png)
![](../images/1CB3CF0F_image 7.png)

## 5. Maximum Likelihood Estimator of Uniform Statistical Model

并不是所有likelihood都可以按照取Log——求导——等于0来求极大值的。
有些函数是不可导（不可微）函数，比如均匀分布的likelihood。
这时候我们是通过画图找极值点。
![](../images/1CB3CF0F_image 8.png)
练习题TBC

## 6. Maximum Likelihood Estimator of Mixture of Gaussians Statistical Model
TBC

## 7. Overview of the EM algorithm
通常情况下，log-likelihood函数是concave的，可以利用数学性质求解极值，并且极值为全局极大值。
但有时候Log-likelihood是non-concave的，例如混合分布时。
![](../images/1CB3CF0F_image 9.png)
![](../images/1CB3CF0F_image 10.png)

## 8. Complete observations
EM算法目标是对混合高斯分布的log-likelihood求极值。
这里求混合高斯模型的PDF时，利用到了和第7小节中的相似假设来简便运算。
![](../images/1CB3CF0F_image 11.png)
注意这里最后一步的化简trick用到了第二排的 X = ZX(1) + (1-Z)X(2)的等式。
这样做的目的是为了将两个指数相加变为一个底数e的指数之和，这样就与第六节求似然函数时不同了：因为只有一个底数e，在求log-likelihood时，就可以直接约掉e，计算会简便很多。
在求两个混合分布的混合密度时，特别的，如果一个为离散分布，一个为连续分布，可以将其试作为两个连续/离散分布来求解。
在这个案例中，隐变量 $Z \sim Ber(1/2)$ 是一个离散分布。因此，我们在求解混合密度时，按照下列方式进行计算：
$$
 f(x, z) = p(z)*f(x|z) 
$$
代表的含义是，首先求观测点来自于伯努利分布的概率（marginal density or marginal PMF)，再乘以对应的条件概率（条件密度函数）。
$$
 p(z) = \left\{ \begin{array}{ll} \frac{1}{2} & \text{if } Z = 1 \\ \frac{1}{2} & \text{if } Z = 0\\ \end{array} \right. 
$$
![](../images/1CB3CF0F_image 12.png)
![](../images/1CB3CF0F_image 13.png)

### Mixture of Exponentials
We can easily generalize the mixture of Gaussians model to a mixture of **any** distributions. These generalizations are useful in cases where observations come from heteregenous populations but each sub-population does not follow a Gaussian distribution. In this exercise we consider the mixture of two exponential distributions.
The Massachussetts Registry of Motor Vehicles (RMV) mainly provides two services: issuing new driver's licenses and renewing old ones. All these services are provided by getting in line to meet with an RMV clerk who processes these requests. The time (in minutes) it takes a clerk to process a new driver's license follows an exponential distribution with unknown parameter $\lambda$  and the time it takes to renew an old driver's license follows an exponential distribution with unknown parameter $4\lambda$. On average, one quarter of all customers are new drivers, against three quarters that come to the RMV to renew their old drivers licenses.
Let $X$ denote the processing time of a random customer.
What is $\mathbb{E}[X]$?
$$
 \mathbb{E}[X]=\frac{7}{16\lambda} 
$$
What is the pdf of $X$ ?
$$
 pdf: f(x) =\frac{1}{4}\lambda e^{-\lambda x} + \frac{3}{4}*4\lambda e^{-4\lambda x} 
$$

## 9. Details of the EM algorithm
现在唯一的问题是需要知道 $z_i$ (即隐变量）是什么。
这是E-Step的作用。E-step并不需要知道 $z_i$是什么，而是用 $z_i$的期望来替代他。
我们希望用条件期望（在给定 $X_i$ 时 $Z_I$ 的期望）来估计 $Z_i$。这时候需要用到贝叶斯公式来计算：因为 $P(Z_i =1|X_i)$ 不好计算，但 $P(X_i|Z_i=1)$ 很好计算。
![](../images/1CB3CF0F_image 14.png)
?这里的P(Z_i=1)=1/2是怎么来的？
![](../images/1CB3CF0F_image 15.png)
![](../images/1CB3CF0F_image 16.png)
### EM: Mixture of Exponentials
TBC
