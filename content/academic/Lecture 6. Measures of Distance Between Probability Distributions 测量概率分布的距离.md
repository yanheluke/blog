---
title: "Lecture 6. Measures of Distance Between Probability Distributions 测量概率分布的距离"
date: 2025-08-10
course: 18.6501x
cover: "F516B0B5_image.png"
bear_pk: F516B0B5-C514-4CC4-8AAE-B0314CC5B5B7
---

# Lecture 6. Measures of Distance Between Probability Distributions 测量概率分布的距离
#Courses/MITx/18.6501x

## 1. Motivation

## 2. Objective 目标
### Total Variation Distance, Kullback-Leibler (KL) divergence, and the Maximum Likelihood Principle
At the end of this lecture, you will be able to do the following:
* Describe properties of the **total variation distance** and **Kullback-Leibler (KL) divergence** .
* Compute the total variation distance and KL divergence between two distributions.
* Derive the **maximum likelihood principle** using the KL divergence.
* Define and **compute the likelihood** of a discrete distribution.

⠀The Unit 3 slides below, which are for the next **5 lectures** , are also available in the resource tab at the top of this course site.

## 3. Unit Overview
**Goals of the Next 5 Lectures**
![](../images/F516B0B5_image.png)

## 4. Introduction to Total Variation Distance
![](../images/F516B0B5_image 2.png)
![](../images/F516B0B5_image 3.png)
**Interpreting Total Variation Distance**
Recall from lecture that the **total variation distance** between two probability measures $\mathbf P_\theta$ and $\mathbf {P}_{\theta^\prime}$ with sample space $E$ is defined by
$$
 \text{TV}(\mathbf{P_\theta}, \mathbf{P_{\theta^\prime}}) = \max_{A\subset E}|\mathbf{P_\theta}(A) - \mathbf{P_{\theta^\prime}}(A)| 
$$
Let  $X_1, …, X_n \sim^{iid}\mathbf P_{\theta^*}$ where $\theta^*$ is an unknown parameter. You construct a statistical model $(E,\{\mathbf P_\theta\}_{\theta\in\mathbb R})$  for your data. By analyzing your data, you are able to produce an estimator $\hat\theta$ such that the distributions $\mathbf P_{\hat\theta}$ and $\mathbf{P}_{\theta^*}$ are close in **total variation distance**. More precisely, you know that
$$ 
\text{TV}(\mathbf{P}_{\hat\theta}, \mathbf{P}_{\theta^*}) \le \epsilon 
$$
where $\epsilon$ is a very small positive number.

## 5. Total Variation Distance for Discrete Random Variables
**Total Variation Distance for Discrete Distributions (Optional video)**
证明
![](../images/F516B0B5_image 4.png)
![](../images/F516B0B5_image 5.png)
![](../images/F516B0B5_image 6.png)
### 练习题：

## 6. Total Variation Distance for Continuous Distributions
![](../images/F516B0B5_image 7.png)

## 7. Properties of Total Variation Distance (Optional)
![](../images/F516B0B5_image 8.png)
### 练习题
TBC

## 8. Worked Examples (Optional)
**Worked Examples on Total Variation Distance**
![](../images/F516B0B5_image 9.png)
第三道题：因为是两个连续分布求TV，所以需要用到积分（注意需要把指示函数即定义域写出来）：
![](../images/F516B0B5_image 10.png)
第四题：两个分布对应着四个不同的值，所以如果按照TV的计算公式，需要分别按照0，1，a, a+1来计算。（ a属于(0,1))
但这里有一个简单的算法：因为X和X+a的取值是disjoint-support的（意味着两个集合并集为空），所以最差的TV/距离就是1。
![](../images/F516B0B5_image 11.png)
![](../images/F516B0B5_image 12.png)
但如果两个分布的取值（集合）是部分disjoint的，就不能用这个方法来求解。
继续上一道题，如果a的取值改为[0,1], 就必须要按照定义取值。
![](../images/F516B0B5_image 13.png)
第四道题：是求一个离散分布和一个连续分布的TV。没有公式，所以需要用定义来进行计算。
注意，虽然左边的分布是渐进正态的（N(0,1)）。但按照定义，他仍然是一个离散分布。
因此，首先写出他的support set（支撑集，使f(x)不为有意义的定义域）。这是一个size为n+1的有限集合。在这个集合内，左边分布的概率为1；右边分布的概率为0（连续分布在有限集内的概率都为0）。
所以TV = 1。
![](../images/F516B0B5_image 14.png)
![](../images/F516B0B5_image 15.png)
### TV存在的缺陷：
* 对于disjoint support，TV恒为1，即使两个分布有可能非常接近（例如a非常接近0）
* 离散分布和连续分布，TV恒为1，即使离散分布的极限分布与连续分布完全一致。

⠀因此，TV捕捉不到这些horizontal movements.

## 9. Motivation and Introduction to the Kullback-Leibler (KL) Divergence
![](../images/F516B0B5_image 16.png)
![](../images/F516B0B5_image 17.png)

**Definition of Kullback-Leibler (KL) Divergence**
离散形式
Let $\mathbf{P}$ and  $\mathbf{Q}$ be **discrete** probability distributions with pmfs $p$ and  $q$ respectively. Let's also assume $\mathbf{P}$ and $\mathbf{Q}$ have a common sample space $E$. Then the **KL divergence** (also known as **relative entropy** ) between  $\mathbf{P}$ and $\mathbf{Q}$  is defined by
$$
 \text{KL}(\mathbf{P},\mathbf{Q})= \sum\limits_{x\in E}p(x)\ln\left(\frac{p(x)}{q(x)}\right) 
$$
where the sum is only over the support of $\mathbf{P}$.

**Why do we sum only over the support of P?**
We use the following limit to justify the definition above. At any point $x \in E$ outside the support of $\mathbf{P}$ but where $q(x) \neq 0$:
$$
 \begin{aligned} \lim\limits_{p/q \rightarrow 0^+}q\left(\frac{p}{q}\right)\ln\left(\frac{p}{q}\right) &= q\lim\limits_{p/q \rightarrow 0^+}\left(\frac{p}{q}\right)\ln\left(\frac{p}{q}\right) \\ &= q*(0) = 0. \quad (\text{by L'hopital's rule)}.
\end{aligned} 
$$
![](../images/F516B0B5_image 25.png)<!-- {"width":328} -->![](../images/F516B0B5_image 26.png)<!-- {"width":448} -->
连续形式
Analogously, if $\mathbf{P}$ and $\mathbf{Q}$  are **continuous** probability distributions with pdfs $p$ and $q$ on a common sample space $E$, then
$$
 \text{KL}(\mathbf{P},\mathbf Q) = \int\limits_{x\in E}p(x)\ln\left(\frac{p(x)}{q(x)}\right)dx 
$$
where the integral is again only over the support of $\mathbf{P}$ .
### 练习题：KL between Gaussians
Let $\mu, \theta \in \mathbb R$, and let $\sigma^2 > 0$. What is $\text{KL}(N(\mu, \sigma^2), N(\theta, \sigma^2))$?

## 10. Properties of the Kullback-Leibler (KL) Divergence
![](../images/F516B0B5_image 18.png)

**Why does the KL divergence take only non-negative values?**

## 11. Estimating the Kullback-Leibler (KL) Divergence
![](../images/F516B0B5_image 19.png)
第一行的变形（引入期望）为什么成立？需要用到以下期望的公式：
$$
 \mathbb{E}[g(x)] = \sum\limits_{x\in E}p(x)g(x), \quad \text{p(x)是pmf of x} 
$$
The next four problems concern the following statistical set-up.
You observe discrete random variables
where  is the true parameter. You construct an associated statistical model  with a discrete sample space .
Your goal is to find an estimator  so that the distributions  and  are close. More precisely, you want to find an estimator  so that the quantity
is as small as possible.
This approach will naturally lead to the construction of the **maximum likelihood estimator** .

TBC.

## 12. Maximum likelihood principle
![](../images/F516B0B5_image 20.png)

**练习题：Deriving the Maximum Likelihood Estimator**
![](../images/F516B0B5_image 21.png)

## 13. Likelihood of a Discrete Distribution

![](../images/F516B0B5_image 22.png)
![](../images/F516B0B5_image 23.png)
补充：bernoulli分布的PMF的几种表现形式
TBC.

## 14. Likelihood of a Poisson Statistical Model
![](../images/F516B0B5_image 24.png)
