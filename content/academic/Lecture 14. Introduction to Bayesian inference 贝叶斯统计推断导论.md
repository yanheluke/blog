---
title: "Lecture 14. Introduction to Bayesian inference 贝叶斯统计推断导论"
date: 2025-08-13
course: 6.431
cover: "72CEB3F7_image.png"
bear_pk: 72CEB3F7-06D7-4566-A0E4-40114C8511B6
---

# **Lecture 14. Introduction to Bayesian inference 贝叶斯统计推断导论**
#Courses/MITx/6.431

## 1. Lecture 14 overview and slides
In this lecture, we start by discussing the numerous domains in which inference is useful. We then develop the conceptual framework of Bayesian inference, and review the various forms of the Bayes rule. We discuss possible ways of arriving at a point estimate based on the posterior distribution, and present the relevant performance metrics, namely, the probability of error for hypothesis testing problems and the mean squared error for estimation problems.

![](../images/72CEB3F7_image.png)

## 2. Overview of some application domains
![](../images/72CEB3F7_image 2.png)
![](../images/72CEB3F7_image 3.png)
![](../images/72CEB3F7_image 4.png)
![](../images/72CEB3F7_image 5.png)
![](../images/72CEB3F7_image 6.png)


## 3. Types of inference problems
![](../images/72CEB3F7_image 7.png)
![](../images/72CEB3F7_image 8.png)
## 4. Exercise: Hypothesis testing versus estimation

## 5. The Bayesian inference framework
贝叶斯统计推断的核心是将未知参数 $\theta$ 视作一个已知分布的随机变量，而频率学派则将未知参数 $\theta$ 看做一个常数。
在模型假设上，贝叶斯学派的观点是从一类已知的模型中随机选择的，引入随机变量 $\Theta$ 来刻画这一个模型；而频率学派的观点是多个待选的概率模型，每个 $\theta$ 的可能值对应一个模型。
**显著性检验（Significance Testing）、假设检验（Hypothesis Testing）和极大似然估计（Maximum Likelihood Estimation, MLE）** 都属于**频率学派（经典统计推断）****的核心方法。它们基于频率学派的框架，强调****数据的重复抽样性质**和**参数作为固定常数**的假设。
![](../images/72CEB3F7_image 9.png)
![](../images/72CEB3F7_image 10.png)
![](../images/72CEB3F7_image 11.png)
第三页PPT说的是，在求出后验分布后，如果你想用一个单独的数或者一个单独的预测来表示后验分布，有两种可以选择的方式：
* MAP（最大后验概率）
* LMS（最小均方估计）


## 6. Exercise: Estimates and estimators
## 7. Discrete parameter, discrete observation
![](../images/72CEB3F7_image 12.png)

## 9. Discrete parameter, continuous observation
在连续观测值的情况下，如果要计算over probability of error(全局错误概率），选择第二个公式会比较方便（只需要求和，不需要积分）：
$$
 \mathbf P(\hat\Theta \neq \Theta) = \sum_\theta\mathbf P(\hat\Theta \neq \Theta|\Theta =\theta)p_\Theta(\theta) 
$$
![](../images/72CEB3F7_image 13.png)

## 10. Exercise: Discrete unknown and continuous observation

## 11. Continuous parameter, continuous observation
![](../images/72CEB3F7_image 14.png)

## 12. Exercise: Continuous unknown and observation
**Let $\Theta$ and $X$ be jointly continuous nonnegative random variables. A particular value $x$ of $X$  is observed and it turns out that $f_{\Theta|X}(\theta|x) = 2e^{-2\theta}$, for $\theta \ge 0$ .**
The following facts may be useful: for an exponential random variable $Y$ with parameter $\lambda$ , we have  $E[Y]=1/\lambda$ and $Var(Y) = 1/\lambda$ .
这道题是已经告诉了后验分布是一个指数分布，求MAP和LMS。

1. **The LMS estimate (conditional expectation) of** $\Theta$:
⠀根据定义，LMS(最小均方估计）等于 $E[\Theta|X=x]$。也就是后验分布的期望 = 1/2

2. **The conditional mean squared error  $\mathbf E[(\Theta - \widehat \Theta_{LMS})^2|X=x]$：**
还是根据定义，由于LMS是条件期望，那么均方误差就是条件方差，所以等于1/4。
如果带入数值，也可以得到:
$$
 \mathbf E[(\Theta - \widehat \Theta_{LMS})^2|X=x] = \mathbf E[(\Theta - E[\Theta])^2|X=x] = Var(\Theta|X=x) 
$$

3. **The MAP estimate of** $\Theta$：
MAP估计 $\hat\theta = \arg\max_\theta f_{\Theta|X}(\theta|x) = 2e^{-2\theta}$。由于后验分布是一个单调递减函数，所以在 $\theta = 0$ 处取得极大值。

4. **The conditional mean squared error $\mathbf E[(\Theta - \widehat \Theta_{MAP})^2|X=x]$  :**
还是带入定义， $\mathbf E[(\Theta - \widehat \Theta_{MAP})^2|X=x]= \mathbf E[(\Theta)^2|X=x] = E[Y^2] = Var(Y) + (E[Y])^2 = 1/4+1/4 = 1/2$


## 13. Inferring the unknown bias of a coin and the Beta distribution
丢一枚不均匀的硬币，记正面向上的概率为 $\theta$, 并且将 $\theta$ 看做随机变量 $\Theta$ 的一个值。 $\Theta$ 的先验概率密度函数记为 $f_\Theta$。
现在考虑n次独立实验，记 $K$ 为观测到正面朝上的总次数。
**首先，我们假设先验分布 $f_\Theta(·)$ 服从[0,1]之间的均匀分布。**
写出后验分布：
$$
 f_{\Theta|K}(\theta|k) = \frac{1*\tbinom{n}{k}\theta^k(1-\theta)^{n-k}}{p_K(k)} 
$$
然后将与 $\theta$ 无关的项提出来，记为 $\frac{1}{d(n,k)}$，得到：
$$
 f_{\Theta|K}(\theta|k) = \frac{1}{d(n,k)}\theta^k(1-\theta)^{n-k} 
$$
这就是beta分布，参数为 $(k-1, n-k+1)$。其中+1是一个历史习惯。

现在我们假设先验分布不再是均匀分布，而是一个beta分布：
$$
 f_\Theta(\theta) = \frac{1}{c}\theta^\alpha(1-\theta)^\beta, \quad \alpha, \beta \ge 0 
$$
再求其后验分布，将与 $\theta$ 无关的项抽出来，可以得到：
$$ 
f_{\Theta|K}(\theta|k) = d*\theta^{\alpha+k}(1-\theta)^{\beta+n-k} 
$$
可知，beta分布的后验分布也是beta分布。
![](../images/72CEB3F7_image 15.png)

## 14. Exercise: The posterior of a coin's bias

## 15. Inferring the unknown bias of a coin - point estimates
在先验分布为均匀分布的假设下，我们求得了后验分布是一个beta分布。接下来需要分别求解点估计：MAP估计和LMS估计。
首先是MAP估计：对后验分布取对数后求导，求导数为0的极值点，得到：
$$
 \hat\theta_{MAP} = k/n 
$$
同时，对 $\Theta$ 随机变量可以刻画为：
$$
 \hat\Theta_{MAP} = K/n 
$$
然后是LMS估计。由于LMS估计是 $\theta$ 的条件期望，所以带入条件期望的公式，有：
$$ 
\begin{aligned}\mathbf E[\Theta|K=k] &= \int_0^1\theta f_{\Theta|K}(\theta|k)d\theta\\ &= \frac{1}{d(n,k)}\int_0^1\theta^k(1-\theta)^{n-k}d\theta \end{aligned} 
$$
从后验分布的形式可知 $\frac{1}{d(n,k)}$ 是归一化常数，让后验分布的概率密度函数在[0,1]上积分等于1，所以带入PPT种蓝色方框的等式，再进行化简，有：
$$
 \mathbf E[\Theta|K=k] = \frac{k+1}{n+2} 
$$
![](../images/72CEB3F7_image 16.png)

## 16. Exercise: Moments of the Beta distribution
**Exercise: Moments of the Beta distribution**
Suppose that $\Theta$ takes values in [0,1],  and its PDF is of the form
$$
 f_\Theta(\theta) = a\theta(1-\theta)^2, \ for \ \theta \in [0,1] 
$$
where  $a$ is a normalizing constant.
Use the formula:
$$
 \int_0^1\theta^\alpha(1-\theta)^\beta d\theta = \frac{\alpha!\beta!}{(\alpha+\beta+1)!} 
$$

**首先求解 $a$**：
根据定义, $\alpha = 1, \beta = 2$，带入公式，有a = 12.
**其次求解 $\mathbf E[\Theta^2]$**:
这是求先验信息，本体不涉及任何后验分布和后验估计。
根据定义，有：
$$
 \mathbf E[\Theta^2] = \int_0^1\theta^2f_\Theta(\theta)d\theta = \int_0^1a\theta^3(1-\theta)^2d\theta = 12*1/60 = 1/5 
$$
## 17. Summary
![](../images/72CEB3F7_image 17.png)