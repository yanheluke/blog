---
title: "Lecture 9. Statistical Properties of the MLE 极大似然估计量的统计性质"
date: 2025-08-10
course: 18.6501x
cover: "4B494B78_image.png"
bear_pk: 4B494B78-478A-4A15-B790-6E26665CBCBD
---

# Lecture 9. Statistical Properties of the MLE 极大似然估计量的统计性质
#Courses/MITx/18.6501x

## 1. Statistical properties of the MLE
### Objectives
At the end of this lecture, you will be able to do the following:
* Derive the maximum likelihood estimator for the uniform statistical model and prove its consistency.
* Recognize that the maximum likelihood estimator is consistent.
* Compute the Fisher information of a statistical model
* Establish asymptotic normality of a maximum likelihood estimator and compute its asymptotic variance using Fisher information

⠀
## 2. Consistency of Maximum Likelihood Estimator

**Review: Definition of MLE**
**Consistency of the Maximum Likelihood Estimator**
![](../images/4B494B78_image.png)
![](../images/4B494B78_image 2.png)
![](../images/4B494B78_image 3.png)
### Consistency of MLE
Given i.i.d samples  and an associated statistical model  the maximum likelihood estimator  of  is a **consistent** estimator under mild regularity conditions (e.g. continuity in  of the pdf  almost everywhere), i.e.
TBC

### Consistency of the MLE of a Uniform Model
TBC

## 3. Fisher Information
![](../images/4B494B78_image 4.png)
![](../images/4B494B78_image 5.png)

Note: PPT里的 第二排更正为：$\mathcal{l}(\theta) = \ln(L_1(X_1,\theta))$
![](../images/4B494B78_image 6.png)
### A Geometric View on the Fisher Information
TBC

## 4. Equivalence between the two definitions of Fisher Information
The content of this video is **optional** but is a good practice to manipulate the quantities involved in the definition of the Fisher information.
TBC

## 5. Examples of Fisher Information Computation
### Fisher Information of the Bernoulli Random Variable
有两种计算方式可以算Fisher信息，但教授说通常情况下计算二阶导会更简便。
通常情况下，求一阶导之后再计算方差，不像期望一样有很好的线性性质可以计算。
**进一步，如果已知了fisher信息 $I(p)$， 同时 $p$ 是一个关于 $\theta$ 的函数：例如 $p = \theta^2$，那么求 $\theta$ 的fisher信息量 $I(\theta)$，就是用p的fisher信息量再乘以p对theta的一阶导的平方。**
$$
 I(\theta) = I(p)\left(\frac{dp}{d\theta}\right)^2 
$$
右下角板书，有一些计算错误，正确的见下一个板书
![](../images/4B494B78_image 7.png)
![](../images/4B494B78_image 8.png)
![](../images/4B494B78_image 9.png)
### Fisher Information of the Binomial Random Variable
tbc
### Fisher Information of a Poisson Random Variable
tbc

## 6. Asymptotic normality of the maximum likelihood estimator
* revise

⠀The **asymptotic normality of the ML estimator** , which will be discussed in the upcoming video, depends upon the Fisher information. For a one-parameter model (like the exponential and Bernoulli), the asymptotic normality result will say something along the lines of following: that the asymptotic variance of the ML estimator is inversely proportional to the value of Fisher information at the true parameter  of the statistical model. This means that if the value of Fisher information at  is high, then the asymptotic variance of the ML estimator for the statistical model will be low.

![](../images/4B494B78_image 10.png)
### Asymptotic Normality of the MLE
TBC

## 7. An idea of the proof of asymptotic normality.
Optional
TBC
