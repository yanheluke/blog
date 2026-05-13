---
title: "[Lecture 20] An introduction to classical statistics 经典统计导论"
date: 2025-08-07
course: 6.431
cover: "DA9843F1_image.png"
bear_pk: DA9843F1-2A26-46F5-9533-EC7CC20984E0
---

# **[Lecture 20] An introduction to classical statistics 经典统计导论**
 #Stats-ML #Courses/MITx/6.431
## 1. Lecture 20 overview and slides 概览
This lecture provides a brief introduction to the so-called classical (non-Bayesian) statistical methods. Besides presenting the general framework, it includes a discussion of estimation based on sample means, confidence intervals, and maximum likelihood estimation.
![](../images/DA9843F1_image.png)
Printable transcript available ~[here](https://courses.edx.org/asset-v1:MITx+6.431x+2T2025+type@asset+block/transcripts_L20-Overview.pdf)~.
Lecture slides: ~[\[clean\]](https://courses.edx.org/asset-v1:MITx+6.431x+2T2025+type@asset+block/lectureslides_L20-clean-slides.pdf)~ ~[\[annotated\]](https://courses.edx.org/asset-v1:MITx+6.431x+2T2025+type@asset+block/lectureslides_L20-annotated-slides.pdf)~
The material in this lecture is covered in ~[Section 9.1](https://courses.edx.org/courses/course-v1:MITx+6.431x+2T2025/pdfbook/0/chapter/1/70)~ of the text.

## 2. Overview of the classical statistical framework 经典统计框架概览
经典统计认为未知参数 $\theta$ 是一个未知的常数（对比贝叶斯统计认为是一个随机变量）
对未知参数 $\theta$ 的估计量（estimator） $\widehat \Theta = g(X)$ 是一个随机变量 $X$ 的函数，因此也是一个随机变量。
对 $X$ 的特定取值 $x$，会有一个对应的估计 $\hat \theta = g(x)$，这是一个估计（estimate）。
![](../images/DA9843F1_image 2.png)
![](../images/DA9843F1_image 3.png)
## 3. The sample mean and some terminology 样本均值与一些术语
以样本均值为例：如果我们要估计总体均值，样本均值是一个很好的估计量。它具有以下特点：
**1** **无偏性（unbiased）：** $\mathbf E[\widehat \Theta_n] = \theta$, 对所有 $\theta$ 都成立。意味着估计量的期望等于真实值。
**2** **相合性（consistency）：** WLLN: $\widehat \Theta_n \rightarrow^p \theta$，对所有 $\theta$ 都成立。意味着随着n增大，估计量依概率收敛于真实值。
**3** **均方误差（mean squared error, MSE):** $\mathbf E[(\widehat \Theta - \theta)^2] = Var(\widehat \Theta_n) = \sigma^2/n$。样本均值的均方误差只和n有关，和theta无关。但其他估计量不一定具有这个性质。

> [!IMPORTANT] 
> ⠀对MSE推导时用到了无偏性和方差的最原始形式： $Var(X) = \mathbf E[X-E[X]]^2$，即一个随机变量减去其期望的平方的期望就是随机变量X的方差。
![](../images/DA9843F1_image 5.png) 
## 4. Exercise: Estimator properties
我们假设 $\theta$ 是随机变量 $X$ 的一个未知期望（假设X的方差为正且有限）。我们构建一个样本均值 $M_n$，并且构建一个估计量： $\widehat \Theta = M_n+\frac{1}{n}$。
1. 估计量不具有无偏性：
$E[\widehat \Theta] =E[M_n+\frac{1}{n}] = \theta + 1/n \ne \theta$ 
2. 估计量具有相合性：
$\widehat \Theta =M_n+\frac{1}{n} \rightarrow^p \theta$ 
如果我们构建一个新的估计量 $\widehat \Theta_n = X_1$，即仅使用第一个样本来作为估计量。
1. 估计量具有无偏性；
2. 估计量不具有相合性：单个样本永远相等，不管n多大。

## 5. On the mean squared error of an estimator 估计量的均方误差
我们可以将MSE分解为两个部分：估计量的方差 + 偏差的平方。
$\mathbf E[(\widehat \Theta - \theta)^2] = Var(\widehat \Theta-\theta)+(\mathbf E[\widehat \Theta - \theta])^2 = var(\widehat \Theta) + (\text {bias})^2$
我们可以构造两个估计量：样本均值与0估计量。可以看出在没有对 $\theta$ 的先验判断时，不能直接比较两个估计量的优劣。
此时，我们引入一个新的概念：标准误差(standard error)，优先选择s.e.小的估计量。
一般在报告估计量时，也会同时报告相应的标准误差。
![](../images/DA9843F1_image 4.png)
## 6. Confidence intervals 置信区间
在经典统计视角下，必须注意置信区间的概念：不能说估计值在置信区间内的概率是95%。这是一个最常见的错误。首先 $\theta$ 是一个真值，置信区间的上下限也是一个真值，不能说P( $\theta$ 在一个区间内）的概率是多少。
相反，置信区间给出的上下限 $[\widehat \Theta^-, \widehat \Theta^+]$ 是两个随机变量。统计推断的本质是我们进行了多次试验，获得了关于置信区间的随机变量，而真值 $\theta$ 落在这个随机变量里的次数占比为95%。
![](../images/DA9843F1_image 6.png)
## 7. Exercise: Bias and MSE
已知随机变量 $X$ 的未知均值为 $\theta$，方差为1。构造估计量：
$$ 
\widehat \Theta_n = 1/3·M_n 
$$
求bias和MSE。
答案为-2/3*theta和1/(9*n)+4/9*theta^2。
## 8. Exercise: Confidence interval interpretation
## 9. Exercise: A simple CI
## 10. Confidence intervals for an unknown mean 对未知均值的置信区间
将样本均值标准正态化，然后变形为关于 $\theta$ 的区间。注意这里得到的置信区间需要知道 $\sigma$ 才能计算。
![](../images/DA9843F1_image 7.png)
## 11. Exercise: CI's via the CLT
## 12. Confidence intervals for the mean when the variance is unknown 当方差未知时，对未知均值的置信区间
当总体方差未知时，有三种方法可以构造出置信区间：
1. 用一个总体方差的上界（upper bound）
例如当 $X$ 是伯努利分布时，总体方差最大值为1/2，可以将1/2作为一个最保守的置信区间估计；
2. 用一个特别的(ad hoc) 方差估计
例如当 $X$ 是伯努利分布时，方差估计量可可以用期望的函数来代替: $\hat \sigma = \sqrt{\widehat \Theta_n(1-\widehat \Theta_n)}$
3. （最泛化的）用方差的样本均值估计
由于总体方差 $\sigma^2 = \mathbf E[(X_i-\theta)^2]$，当已经收集到n个样本的时候，我们可以将期望改为：
$\frac{1}{n}\sum_{i=1}^n(X_i-\theta)^2$。随n增大，由WLLN, 这个样本随机变量( $(X_i-\theta)^2$）的样本期望收敛于总体期望。所以他也收敛于总体方差。
由于总体期望也是未知的，所以我们可以用样本期望代替总体期望，这样就构造出了一个总体方差的估计量。
![](../images/DA9843F1_image 15.png)![](../images/DA9843F1_image 9.png)
## 13. Other natural estimators 其他自然估计量
从样本均值出发，我们可以推导出：
* 随机变量的函数的期望，可以用样本的函数的均值进行估计；
* 方差：可以用样本均值代替总体期望进行估计
* 协方差：用X和Y的样本均值代替总体均值
* 相关系数:

⠀所有这些估计量都具有相合性.
![](../images/DA9843F1_image 10.png)

## 14. Exercise: Natural estimators
## 15. Maximum likelihood estimation 极大似然估计
与贝叶斯统计中，求最大后验分布的情况类似，经典统计的MLE等同于贝叶斯统计中假设先验分布是flat/constant时的计算方式。但两者的哲学完全不同。
贝叶斯统计的最大后验概率（MAP）：theta最可能的值是什么？
经典统计的极大似然估计（MLE）：theta是什么值，会让数据有最大可能性？
![](../images/DA9843F1_image 11.png)
![](../images/DA9843F1_image 12.png)
## 16. Maximum likelihood estimation examples 极大似然估计的例子
![](../images/DA9843F1_image 13.png)
![](../images/DA9843F1_image 14.png)
## 17. Exercise: ML estimation

