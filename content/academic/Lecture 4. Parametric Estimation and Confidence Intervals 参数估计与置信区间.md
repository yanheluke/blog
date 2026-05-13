---
title: "Lecture 4. Parametric Estimation and Confidence Intervals 参数估计与置信区间"
date: 2025-08-10
course: 18.6501x
cover: "662692BB_image.png"
bear_pk: 662692BB-F4D1-4F67-A4F5-C0ACF04014D7
---

# Lecture 4. Parametric Estimation and Confidence Intervals 参数估计与置信区间
#Courses/MITx/18.6501x
## 1. Parametric Estimation and Confidence Intervals 参数估计与置信区间
### Objectives 目标
At the end of this lecture, you will be able to
* Distinguish between an **estimator** and a **statistic** .
* Compute the **bias** , **variance** , and **quadratic risk** of an estimator.
* Determine whether or not an estimator is **consistent** .
* Construct a confidence interval for an unknown parameter.
* Explain the frequentist interpretation of the confidence interval.

⠀
## 2. Statistics, Estimators, Consistency, and Asymptotic Normality 统计量、估计量、一致性与渐进正态性

![](../images/662692BB_image.png)
![](../images/662692BB_image 2.png)
这里板书的问题是: $Var(\hat \theta_n) \xrightarrow[n \rightarrow \infty]{} 0$。
因为 $Var(\hat \theta_n) = \sigma^2/n$，当n 无穷大时，方差趋近于0。

**区分样本方差和渐进方差。**
* **样本方差（原始估计量视角）描述估计量在当前样本量n下的实际方差。是直接计算估计量在当前样本下的离散程度：**
$$ 
Var(\hat \theta_n) = \frac{\sigma^2}{n}
$$
当 $n \rightarrow \infty$ 时， $Var(\hat \theta_n) = 0$。 （n越大，样本方差离散程度越小）。这里的方差指的是原始估计量的渐近方差（也常叫“方差渐近行为”）。
* **渐进方差（AVar）通过极限理论（如中心极限定理）推导，描述估计量标准化后，在大样本（ $n \rightarrow \infty$）下的极限分布的方差，与n无关。**
  * 例如在渐进正态性里，渐进方差为 $\sigma^2$，是一个常数。
* 对于大多数估计量（如MLE，样本均值等），两者满足：
$$
 AVar(\hat \theta_n) = \lim_{n\rightarrow\infty} n * Var(\hat \theta_n) 
$$
![](../images/662692BB_image 3.png)<!-- {"width":638} -->
$\sqrt n(\hat\theta_n - \theta)$ 的分布，在n取不同值的时候。
* 各条曲线代表不同样本量 nnn 时该量的分布。
* 随着 $n$ 增大，曲线越来越集中（更尖、更高），说明方差随 $n$ 增大而线性增大( $∼n⋅p(1−p)$)。
* 黑色虚线是其渐进分布 $\mathcal{N}(0, p(1-p))$，这个分布描述的是“归一化前”的极限行为。
⠀![](../images/662692BB_image 4.png)<!-- {"width":626} -->
$\sqrt n(\hat\theta_n - \theta)/\sqrt{p(1-p)}$ 的分布，n取不同值。
* 所有样本量下的分布几乎都重合，并与标准正态 $\mathcal{N}(0, 1)$ 完美一致。
* 这说明该标准化后的量的极限分布是固定的，不会随着 $n$ 变化而变尖或变平。

A **statistic** is any measurable function of the sample. An **estimator** of $\theta$ is a statistic $\hat \theta_n = \hat \theta_n(X_1, …, X_n)$ whose expression **does not** depend on $\theta$ .

**一致性（consistence）** 一个关于 $\theta$ 的估计量 $\hat \theta_n$，如果随 $n \rightarrow \infty$，依概率收敛至 $\theta$，那么他是弱一致性的（weakly consistent)； 如果随 $n \rightarrow \infty$，几乎处处收敛至 $\theta$，那么他是强一致性的（strongly consistent)。
**渐进正态性（Asymptotic Normality):** 指的是当样本量 *n* 趋近于无穷大时，某个估计量（或统计量）的标准化形式 **依分布收敛于正态分布**。
$$
 \sqrt n(\hat \theta_n - \theta) \xrightarrow[n \rightarrow \infty]{(d)} N(0, \sigma^2) 
$$
其中：
* $\hat \theta_n$ 是参数 $\theta$ 的估计量（如样本均值、MLE等）；
* $\sigma^2$ 是渐进方差（Asymptotic Variance）

练习题：Quantifying Consistency
![](../images/662692BB_image 5.png)
![](../images/662692BB_image 6.png)
解题思路：
由Xn服从伯努利分布，可以知道： $\sigma = \sqrt{(p(1-p)}$ 。
所以，由CLT，可以得到: $\frac{\sqrt(n)}{\sigma} (\bar X_n - p) \rightarrow N(0,1)$ (依分布收敛）
将这个公式变形（与题目要求的形式做一些联系，可以得到）：
$$
 \frac{\sigma}{n^{1/2-c}}\frac{n^{1/2}}{\sigma}(\bar X_n - p) \approx \frac{\sigma}{n^{1/2-c}}N(0,1) 
$$
根据slutsky定理：
如果一个随机变量序列依分布收敛，另一个序列依概率收敛到常数，则它们的加、减、乘、除运算后的收敛性可以拆解为对极限的运算。
要想使上面的公式不依概率收敛到0，必须前一项发散。
所以 需要 $1/2-c > 0 , 有 c <1/2$。
参考deepseek给出的解释：
![](../images/662692BB_image 7.png)

## 3. Bias of Estimators; Jensen's Inequality 估计量偏差；Jensen不等式
**Bias Estimators and an application of Jensen's Inequality**
![](../images/662692BB_image 8.png)
![](../images/662692BB_image 9.png)
bias（偏差）的定义：
$$
 \text{bias}(\hat\theta_n) = \mathbb{E}(\hat\theta_n) - \theta 
$$
如果bias = 0，那么估计量 $\hat\theta_n$ 是无偏的。但无偏估计量可能会有很大的方差：所以无偏估计量不一定是我们想要的。
黑板上的板书中，白色为无偏估计量的PDF，黄色为有偏估计量的PDF，很明显我们更想要有偏估计量，因为他离真实的 $\theta$ 更近。
lecture中值得注意的是最后一个估计量：
$$
 \hat p_n = \sqrt{\mathbb{I}(X_1 = 1, X_2 = 1) }, \quad \mathbb{I}为指示函数。 
$$
可以令 $Z = \mathbb{I}(X_1 = 1, X_2 = 1)$，Z需要X_1和X_2同时为1时才为1，所以Z本质上服从 $Z \sim Ber(p^2)$。
注意：**函数的期望不等于期望的函数，因为Jensen’s inequality。**
* 如果f(*)为凸函数(convex)：
$$ 
\mathbb{E}f(X) \ge f(\mathbb{E}(X)) 
$$
* 如果f()为凹函数（concave）：

$$
 \mathbb{E}f(X) \le f(\mathbb{E}(X)) 
$$
因为f(x) = sqrt(Z)是凹函数：
$$
 \mathbb{E}[\sqrt Z] \le \sqrt{\mathbb{E}[Z]} = p 
$$
### Jensen’s Inequality
![](../images/662692BB_image 10.png)
![](../images/662692BB_image 11.png)

## 4. Variance of Estimators 估计量的方差

![](../images/662692BB_image 12.png)
同样需要注意的是最后一个。
We recall the following useful formulas for the variance. First if $X$ is a random variable, then the variance of  $X$ is defined by:
$$
 \text{Var}[X] = \mathbb{E}[(X - \mathbb{E}[X])^2] 
$$
The following equivalent ‘shortcut' formula is convenient when we already know the expectation of $X$:
$$
 \text{Var}[X] = \mathbb{E}[X^2] - (\mathbb{E}[X]^2) 
$$
Finally, in the class, we often compute the variance of averages of random variables. If $X_1, …, X_n$ are i.i.d., each with variance $\sigma^2$, then
$$
 \text{Var}[\bar X_n] = \frac{\sigma^2}{n} 
$$

## 5. Quadratic Risk of Estimators 估计量的二次风险
![](../images/662692BB_image 13.png)

## 6. Worked Example: Bias, Variance and Quadratic Risk
![](../images/662692BB_image 14.png)

## 7. Exercise: Strengths and Weaknesses of Estimators
这一小节是练习题。TBC

## 8. Confidence Intervals 置信区间
**Confidence Interval for the Kiss Example**
![](../images/662692BB_image 15.png)
![](../images/662692BB_image 16.png)
![](../images/662692BB_image 17.png)
![](../images/662692BB_image 18.png)
![](../images/662692BB_image 19.png)

## 9. Conservative Bound
**Confidence Interval using a Conservative Bound**

