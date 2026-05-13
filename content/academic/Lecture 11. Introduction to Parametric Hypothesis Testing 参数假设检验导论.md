---
title: "Lecture 11. Introduction to Parametric Hypothesis Testing 参数假设检验导论"
date: 2025-08-10
course: 18.6501x
cover: "3A1C3900_image.png"
bear_pk: 3A1C3900-A1B7-48E0-A05E-E5FB038005C6
---

# Lecture 11. Introduction to Parametric Hypothesis Testing 参数假设检验导论

#Courses/MITx/18.6501x


## 1. Goals of Unit 4
## 2. Introduction to Parametric Hypothesis Testing 参数假设检验导论
### Objectives 目标
At the end of this lecture, you will be able to do the following:
* Reformulate experimental questions in terms of a **hypothesis test** by specifying an appropriate **null hypothesis** and an **alternative hypothesis** .
* **Design** statistical **tests** to decide between a null and alternative hypothesis.
* Understand the types of error of a test
* Compute the power function of a test
* Design statistical tests with a specific level or asymptotic level.
* Apply a test to a given sample to determine whether or not the null hypothesis should be rejected.
* Compute a test from a confidence interval
* Compute and interpret the p-value associated to a statistical test.

⠀
## 3. Null and alternative hypotheses 零假设与备择假设
![](../images/3A1C3900_image.png)
![](../images/3A1C3900_image 2.png)

## 4. Different types of hypotheses 假设的不同类型
![](../images/3A1C3900_image 3.png)
![](../images/3A1C3900_image 4.png)

## 5. Statistical modelling 统计建模
在这个实验中，我们将预期的结果”新药物效果更好“作为了备择假设。professor说这是常用的方式，即将我们期望出现的结果作为备择假设。
![](../images/3A1C3900_image 5.png)
![](../images/3A1C3900_image 6.png)
## 6. Asymmetry in the hypotheses 假设中的渐进性
![](../images/3A1C3900_image 7.png)
![](../images/3A1C3900_image 8.png)
## 7. Tests 试验
一个试验（test）是一个统计量 $\psi \in \{0,1\}$，并且不依赖其他未知参数。
这个统计量经常被写成指示函数的形式: $\psi = \mathbb I\{R\}$。其中 $R$ 是一个被叫做拒绝域的事件。
简单理解这里的 $R$ 就是令 $\psi = 1$ 的事件，可以写成 $\psi = \mathbb I\{\psi = 1\}$，这是一个同义反复。
![](../images/3A1C3900_image 9.png)
### 对比statistic和statistical test
* statistic: a function that can be computed from the data. 是一个函数，可以从数据中计算出的函数。
* statistical test: is an **statistic** whose output is **always** either  0 or 1 , and like an estimator, does not depend explicitly on the value of true unknown parameter. 是一个输出永远为0或1的统计量。并且与估计量一样，statistical test并不显式依赖于未知参数的真实值。

## 8. Errors of a test 假设的错误类型

![](../images/3A1C3900_image 10.png)
![](../images/3A1C3900_image 11.png)
### 练习题
### Testing the Support of a Uniform Variable: Type 1 Error of a Test
![](../images/3A1C3900_image 12.png)![](../images/3A1C3900_image 13.png)
### Testing the Support of a Uniform Variable: Type 2 Error of a Test
TBC
![](../images/3A1C3900_image 14.png)![](../images/3A1C3900_image 15.png)

## 9. Level and asymptotic level 水平与渐进水平
![](../images/3A1C3900_image 16.png)
![](../images/3A1C3900_image 17.png)

### 练习题
### Testing the Support of a Uniform Variable: Level and Threshold
![](../images/3A1C3900_image 18.png)
### Testing the Support of a Uniform Variable: Determine the Threshold
![](../images/3A1C3900_image 19.png)s
## 10. Building a test from a confidence interval 从置信区间构建一个试验
![](../images/3A1C3900_image 20.png)![](../images/3A1C3900_image 21.png)
### 练习题
## 11. Meaning of the level of a test 试验水平的含义
![](../images/3A1C3900_image 22.png)alpha 代表了 实际上拒绝了H0的试验，但不应该拒绝H0的试验次数
## 12. P-values P值
![](../images/3A1C3900_image 23.png)![](../images/3A1C3900_image 24.png)
## 13. The evidence scale 证据权重
![](../images/3A1C3900_image 25.png)