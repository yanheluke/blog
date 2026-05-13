---
title: "Lecture 13. The T-test T检验"
date: 2025-08-10
course: 18.6501x
cover: "6D1A71E9_image.png"
bear_pk: 6D1A71E9-7314-4E12-B02F-50DEDDBC98C4
---

# Lecture 13. The T-test T检验
#Courses/MITx/18.6501x

## 1. Objectives
At the end of this lecture, you will be able to do the following:
* Identify situations in which you cannot use the Wald test
* Use the T-test to when sample sizes are small
* Perform T-tests at fixed levels and compute exact p-values
* Understand the chi-squared distribution and the Student's t distribution and how they relate to the Gaussian distribution


## 2. The Wald test and small sample sizes
![](../images/6D1A71E9_image.png)


## 3. A first example
![](../images/6D1A71E9_image 2.png)
![](../images/6D1A71E9_image 3.png)


## 4. The Chi-squared distribution
The $\chi ^2_d$  **distribution with** $d$ **degrees of freedom** is given by the distribution of
$$
Z_1^2+Z_2^2+...+Z^2_d, 
$$
where $Z_1,…,Z_d \sim^{iid} \mathcal N(0,1)$.
PPT里提到的 $||Z||^2_2$，是欧几里得范数的平方。下标2代表欧几里得范数，上标2代表平方。
$$
 ||Z||_2 = \sqrt{Z_1^2+Z_2^2+...+Z_k^2}\\ ||Z||_2^2 = Z_1^2+Z_2^2+...+Z_k^2 = \chi^2_k
$$
卡方分布的基本性质：如果 $V\sim \chi^2_k$, 那么：
$$
 \mathbb E[V] = k \\ \text{var}[V] = 2k 
$$
![](../images/6D1A71E9_image 4.png)不同自由度取值下，卡方分布的PDF:
![](../images/6D1A71E9_image 5.png)
![](../images/6D1A71E9_image 6.png)

### 练习题：The Chi-Squared Distribution and the Sample Second Moment
假设 $X_1,…,X_n\sim^{iid}\mathcal N(0, \sigma^2)$，令：
$$
 V_n = \frac{1}{n}\sum_{i=1}^nX^2_i 
$$
如果想令: $a*V_n = \chi^2_k$， 求解a和自由度k。

首先根据卡方分布的基本形式，构造一个服从标准正态分布的随机变量 $Z$。（这里本身应该从单变量 $X_1$ 开始将其变形为服从 $\chi_1^2$ 的形式，但我这里直接简写了）
由: $Z = \frac{X}{\sigma} \sim \mathcal N(0,1)$， 有: $Z^2_n = \frac{X^2}{\sigma^2} \sim \chi_n^2$
再根据 $V_n$ 的形式，可以构造 $\frac{n}{\sigma^2}*V_n = Z^2_n \sim \chi_n^2$

## 5. Sample Variance and Sample Mean of IID Gaussians: Cochran's Theorem
回到第三节，我们继续求解之前遗留的表达式。
这里保留了原始的板书PPT，方便看推导过程。
![](../images/6D1A71E9_image 7.png)清晰版：
![](../images/6D1A71E9_image 8.png)

## 6. Student's T distribution
同样的，保留原始的板书。T分布是一个标准正态分布Z和一个卡方分布除以其自由度的比值。
$$
t_k = \frac{Z}{\sqrt{V/k}} 
$$
随着自由度 $k$ 变为无穷大, $V/k = Z_1^2+Z_2^2+…+Z_k^2/k$ 根据大数法则，p/a.s收敛于 $E[Z_1^2]= 1$, t分布收敛于正态分布。

![](../images/6D1A71E9_image 9.png)![](../images/6D1A71E9_image 10.png)
![](../images/6D1A71E9_image 11.png)

## 7. Student's T test
在使用T检验在小样本上是，有一个假设前提是X iid服从正态分布，期望与方差是未知的。
![](../images/6D1A71E9_image 12.png)![](../images/6D1A71E9_image 13.png)


## 8. P-values for the T-test
![](../images/6D1A71E9_image 14.png)


## 9. Comparison between the T-test and the Wald test
![](../images/6D1A71E9_image 15.png)


## 10. Two-sample T-tests and the Welch-Satterthwaite Formula
![](../images/6D1A71E9_image 16.png)![](../images/6D1A71E9_image 17.png)![](../images/6D1A71E9_image 18.png)![](../images/6D1A71E9_image 19.png)

保留第二张PPT的备注：
![](../images/6D1A71E9_image 20.png)


## 11. Who was Student? (optional)
![](../images/6D1A71E9_image 21.png)
![](../images/6D1A71E9_image 22.png)