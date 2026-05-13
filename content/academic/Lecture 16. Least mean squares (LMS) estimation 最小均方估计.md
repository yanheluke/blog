---
title: "Lecture 16. Least mean squares (LMS) estimation 最小均方估计"
date: 2025-08-13
course: 6.431
cover: "259C908E_image.png"
bear_pk: 259C908E-EFAD-4B18-B849-E8C1ED4886F7
---

# **Lecture 16. Least mean squares (LMS) estimation 最小均方估计**
#Courses/MITx/6.431

## 1. Lecture 16 overview and slides
In this lecture we focus on the conditional expectation estimator. We show that it minimizes both the conditional and the unconditional mean squared estimation error. We develop some its mathematical properties and also illustrate the calculation of the mean squared error.

![](../images/259C908E_image.png)

## 2. LMS estimation without any observations
![](../images/259C908E_image 2.png)
![](../images/259C908E_image 3.png)

## 3. LMS estimation; single unknown and observation

这一段比较绕。上一节是在假设没有任何观测值的情况下，推导出了最小化MSE的参数估计：
$$
 \mathbf E[(\Theta-\hat\theta)^2] : \hat\theta = \mathbf E[\Theta] 
$$
那么，现在我们有观测值X = x了，最小化条件MSE的参数估计的形式是一样的，最优参数theta是在X=x时， $\Theta$ 的条件期望。
$$
 \mathbf E[(\Theta-\hat\theta)^2|X=x] : \hat\theta = \mathbf E[\Theta|X=x] 
$$
所以，抽象表述，LMS估计量（一个随机变量）为：
$$
 \widehat \Theta = \mathbf E[\Theta|X] 
$$
第二页PPT则是用到了不等式变形和迭代期望定理。
![](../images/259C908E_image 4.png)
![](../images/259C908E_image 5.png)

## 4. Exercise: LMS estimation

**Exercise: LMS estimation**
Let $\Theta$ be the bias of a coin, i.e., the probability of Heads at each toss. We assume that $\Theta$ is uniformly distributed on [0, 1]. Let $K$ be the number of Heads in 9 independent tosses.
By performing some fancy and very precise measurements on the structure of that particular coin, we determine that $\Theta = 1/3$. Find the LMS estimate of $K$ based on $\Theta$ .

这道题比较迷惑的是，求的是 $K$ 的LMS估计，而不是 $\Theta$。
因为 $K$ 是代表正面向上的次数，并且单次试验正面向上的概率为 $\Theta = 1/3$。所以我们知道：
$$
 p(K|\Theta) \sim Binomial(9,1/3) 
$$
根据LMS的公式（注意这里和PPT的形式不同）：
$$
 \hat K_{LMS} = \mathbf E[K|\Theta = \theta] = n*\theta = 9*1/3 = 3 
$$

## 5. LMS performance evaluation
整体均方误差也是一个确定值，而不是一个随机变量？

![](../images/259C908E_image 6.png)![](../images/259C908E_image 7.png)

## 6. Exercise: LMS estimation error
**Exercise: LMS estimation error**
As in the previous exercise, let $\Theta$ be the bias of a coin, i.e., the probability of Heads at each toss. We assume that $\Theta$ is uniformly distributed on [0, 1]. Let  $K$ be the number of Heads in  9 independent tosses. We have seen that the LMS estimate of $K$ is $\mathbf E[K|\Theta = \theta] = n\theta$.

1. **Find the conditional mean squared error $\mathbf E[(K -\mathbf E[[K|\Theta - \theta])^2|\Theta = \theta]$ if $\theta = 1/3$.**
第一问直接套用公式：
在给定观测值时，条件均方误差等价于条件方差。
$$
 \mathbf E[(K -\mathbf E[[K|\Theta - \theta])^2|\Theta = \theta] = Var(K|\Theta = \theta) = n\theta(1-\theta) = 2 
$$

2. **Find the overall mean squared error of this estimation procedure.**
第二问犯了一个错误：**全局均方误差，并不是一个随机变量，而是一个确定数。**全局均方误差是所有可能的 Θ 取平均后的期望误差，消除了 Θ 的随机性。
从定义上，可以推导出全局均方误差等于条件方差的期望。在这道题里，即：
$$
 \mathbf E[(K -\mathbf E[[K|\Theta ])^2] = \mathbf E[Var(K|\Theta)] \\ = E[n\Theta(1-\Theta)] = nE[\Theta(1-\Theta)] 
$$
注意现在 $\Theta$ 不再是条件分布了，所以根据题目定义，可知 $\Theta \sim Uniform[0,1]$。对 $\Theta$ 求期望可以视作对随机变量的函数求期望，求积分：
$$
 nE[\Theta(1-\Theta)] = n\int_0^1(\theta(1-\theta)d\theta \\ = 9*1/6 = 3/2 
$$
## 7. Example: the LMS estimate

![](../images/259C908E_image 8.png)

## 8. Exercise: LMS example
## 9. Example: LMS performance evaluation
这里积分的对象应该是 $\theta$ 而不是 $x$?
这个例题中的条件均方误差，是一个关于x的函数： $Var(\Theta|X = x)$。在给定X的时候， $\Theta$ 是一个[0,x]上的均匀分布，所以条件方差 = x^2/12。
全局均方误差要更复杂一点： $\mathbf E[Var(\Theta|X)]$ 是对条件方差求平均。即：
$$
 \mathbf E[Var(\Theta|X)] = \int f_X(x)\mathbf E[Var(\Theta|X=x)]dx 
$$
但题目中并没有给出关于X的边缘概率密度函数，只给了联合密度函数。所以需要从联合密度函数里求解出边缘密度函数。
![](../images/259C908E_image 9.png)


## 10. Exercise: Mean squared error
TBC
因为联合区域是一个直角三角形，所以 $f_{\Theta, X}(\theta, x) = 2$。
所以，边缘密度函数 $f_X(x) = \int_0^x f_{\Theta, X}(\theta, x) d\theta = 2x$。

## 11. The multidimensional case

![](../images/259C908E_image 10.png)
![](../images/259C908E_image 11.png)

## 12. Exercise: Multidimensional challenges

## 13. Properties of the LMS estimation error
![](../images/259C908E_image 12.png)

## 14. Exercise: Theoretical properties

homework重新做
