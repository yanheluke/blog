---
title: "Lecture 21. The Bernoulli process 伯努利过程"
date: 2025-08-13
course: 6.431
cover: "52E0046B_image.png"
bear_pk: 52E0046B-3366-4771-ABD9-0D4E2F1A1110
---

# **Lecture 21. The Bernoulli process 伯努利过程**
#Courses/MITx/6.431

## **1. Lecture 21 overview and slides**
In this lecture we introduce the Bernoulli process, which consists of a sequence of independent trials. We study various associated random variables (e.g., number of successes, arrival time of the th success, time between consecutive successes, etc.). We also discuss the merging and splitting of Bernoulli arrival streams.
![](../images/52E0046B_image.png)


## **2. The Bernoulli Process**
伯努利过程是最简单的随机过程，本质上是一个独立伯努利实验的序列， $X_i$。
对每个实验 $i$ :
* $P(X_i = 1) = P(第i个实验成功) = p$ 
* $P(X_i = 0) = P(第i个实验失败) = 1-p$ 
关键假设：
* 独立
* 时间同质性(time-homogeneity) 

![](../images/52E0046B_image 2.png)

## 3. Exercise: The Bernoulli process


## 4. Stochastic processes随机过程
随机过程有两种理解的方式：

1. 将随机过程视为无限随机变量 $X_1,X_2,\dots$ 的序列;
* 我们关心每一个随机变量 $X_i$ 的性质：期望、方差、PMF；
* 同时关心无限长度的联合概率密度 $p_{X_1,\dots,X_n}(x_1,\dots,x_n) = p_{X_1}\cdot\dots p_{X_n}(x_n)$ 

2. 将随机过程视为样本空间：
* $\Omega$  = set of infinite sequences of 0’s and 1’s 样本空间是0和1的无限序列的集合。
* 视为单次试验，试验按时间运行，每个时间我们得到一个无限序列。
![](../images/52E0046B_image 3.png)

## **5. Review of known properties of the Bernoulli process**

复习伯努利过程的已知性质。
视作一个二项分布，PMF、期望、方差已知。
![](../images/52E0046B_image 4.png)

### Time until the first success/arrival 首次成功/到达所需的时间
将其视作为一个几何分布
* $T_1 = \min\{i:= X_i = 1\}$
* $P(T_1 = k) = (1-p)^{k-1}p, \  k = 1,2,…$
* $E[T_1] = 1/p$
* $Var(T_1) = (1-p)/p^2$ 
![](../images/52E0046B_image 5.png)

## **6. Exercise: Time until the first failure**
这道题做错了

## **7. The fresh start property**

![](../images/52E0046B_image 6.png)