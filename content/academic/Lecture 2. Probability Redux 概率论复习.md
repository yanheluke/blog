---
title: "Lecture 2. Probability Redux 概率论复习"
date: 2025-08-09
course: 18.6501x
cover: "6DECE91F_image.png"
bear_pk: 6DECE91F-0AAB-4BBC-A2BF-FD8D660C1E76
---

# **Lecture 2. Probability Redux 概率论复习**

#Courses/MITx/18.6501x

## 1. Objectives 目标
1. Recall the statements of the **(strong/weak) law of large numbers** and the **central limit theorem** and know to apply these for large sample sizes.
2. (Optional:) Apply **Hoeffding's inequality** to the sample means of bounded i.i.d. random variables.
3. Recall the probability density function and properties of the **Gaussian distribution** .
4. Use **Gaussian probability tables** to obtain probabilities and **quantiles** .
5. Distinguish between **convergence almost surely（几乎处处收敛）** , **convergence in probability（依概率收敛）** and **convergence in distribution（依分布收敛）** , understand that these notions are from strongest to weakest.
6. Determine convergence of sums and products of sequences that converge almost surely or in probability.
7. Apply **Slutsky's theorem** to the sum and product of a sequence that converges in distribution and another that converges in probability to a constant.
8. Use the **continuous mapping theorem** to determine convergence of sequences of a function of random variables.

⠀
## 2. Two important probability tools 两个重要的概率工具
### 1. lectures
![](../images/6DECE91F_image.png)
rule of thumb: 经验法则
TBC
==🔴**Averages of random variables: Laws of Large Numbers and Central Limit Theorem**==
Let $X, X_1, X_2, …, X_n$ be i.i.d. random variables, with $\mu = \mathbb{E}[X]$ and $\sigma^2 = \text{Var}[X]$ .
* Laws (weak and strong) of large numbers (LLN):

$$ 
\bar X_n := \frac{1}{n}\sum\limits_{i=1}^n \xrightarrow[n\rightarrow\infty]{\text{P, a.s.}}\mu 
$$
where the convergence is in probability (as denoted by $\text{P}$ on the convergence arrow) and almost surely (as denoted by $\text{a.s.}$ on the arrow) for the weak and strong laws respectively.
* Central limit theorem (CLT):

$$
 \begin{aligned}\sqrt n\frac{\bar X_n - \mu}{\sigma} &\xrightarrow[n\rightarrow\infty]{(d)} \mathcal{N}(0,1)\\ \text{or equivalently,} \quad \sqrt n(\bar X_n - \mu) &\xrightarrow[n\rightarrow\infty]{(d)} \mathcal{N}(0, \sigma^2) \end{aligned} 
$$
where the convergence is in distribution, as denoted by $(d)$ on top of the convergence arrow.
We will revisit the different modes of convergence near the end of this lecture.
**Note** : In *6.431x: Probability–the Science of Uncertainty and Data*, we used yet another equivalent formulation of the CLT:
$$ 
\frac{S_n - n\mu}{\sqrt n \sigma} \xrightarrow[n\rightarrow\infty]{(d)} \mathcal{N}(0,1) 
$$
where $S_n = \sum_{i=1}^nX_i$ is the sum (not the average) of $X_i$ .

## 3. (Optional) Hoeffding's Inequality
### 1. Lectures
![](../images/6DECE91F_image 2.png)
![](../images/6DECE91F_image 3.png)

## 4. Gaussian distribution
![](../images/6DECE91F_image 4.png)
![](../images/6DECE91F_image 5.png)
## 5. Properties of the Gaussian distribution
### 1. Lectures
![](../images/6DECE91F_image 6.png)

## 6. Gaussian Probability Tables and Quantiles
![](../images/6DECE91F_image 7.png)
![](../images/6DECE91F_image 8.png)
![](../images/6DECE91F_image 9.png)

## 7. Modes of Convergence
![](../images/6DECE91F_image 10.png)
![](../images/6DECE91F_image 11.png)
![](../images/6DECE91F_image 12.png)
![](../images/6DECE91F_image 13.png)
