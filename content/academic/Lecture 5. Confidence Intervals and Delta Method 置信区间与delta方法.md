---
title: "Lecture 5. Confidence Intervals and Delta Method 置信区间与delta方法"
date: 2025-08-10
course: 18.6501x
cover: "5E7163C0_image.png"
bear_pk: 5E7163C0-27D9-4345-BB8C-C95B0C29A260
---

# Lecture 5. Confidence Intervals and Delta Method 置信区间与delta方法
#Courses/MITx/18.6501x

## 1. Confidence Intervals, the Delta Method, and Hypothesis Testing
### Objectives
At the end of this lecture, you will be able to:
* Apply the **Delta method** to an asymptotically normal sequence of random variables.
* Estimate the parameter and construct **confidence intervals for an exponential statistical model** using the Delta method.
* Construct confidence intervals for a variety of statistical models using the Delta method and one of the **conservative** , **solve** , or **plug-in** methods.
* Give a **frequentist interpretation** of the meaning of a (asymptotic) confidence interval of level $1-\alpha$.
* Understand the basic principle behind hypothesis testing.

⠀
## 2. Confidence Intervals Concept Checks
### Confidence Interval Concept Check 1
![](../images/5E7163C0_image.png)
Solution:
![](../images/5E7163C0_image 2.png)
备注：
置信区间 $\mathcal{L}=[L(X_1, ..., X_n), U(L(X_1, ..., X_n)]$ 的上下界L和U是关于样本的函数。样本X_n是随机变量，所以 $\mathcal{L}$ 也是随机变量。

### Confidence Interval Concept Check 2
Recall that a **realization** of a random variable $X$ is the value that it takes when we observe $X$. For example, if  $X \sim Ber(1/2)$ and we observe the event $X=1$, then $x=1$ is the realization (observed value) of the random variable $X$.
Let $\mathcal{L}, \mathcal{J}$,  be some 95% and 98% asymptotic confidence intervals respectively for the unknown parameter $p$. Which of the following statements is true?
![](../images/5E7163C0_image 3.png)
Solution:
### 渐近置信区间（Asymptotic Confidence Intervals）的解释
**1** **核心概念**： 渐近置信区间是一种**基于大样本理论**的统计方法，适用于样本量*n*足够大的情况。当*n*→∞时，该区间以预设的概率（如95%或98%）覆盖未知参数的真值*p*。
**2** **构造原理**：
	* 利用样本统计量（如样本均值*p*^）的**渐近正态性**（Asymptotic Normality）。例如，对于二项分布参数*p*，当*n*很大时，*p*^近似服从 $N(p, \frac{p(1-p)}{n})$
	* 通过统计量的渐近分布确定区间边界。例如，95%渐近置信区间为：
$$
 \hat p \pm 1.96 \sqrt \frac{\hat p(1-\hat p)}{n} 
$$
### Confidence Interval Review
![](../images/5E7163C0_image 4.png)
![](../images/5E7163C0_image 5.png)

## 3. Confidence Intervals Concept Checks Continued 置信区间概念检查（续）
### Lectures
![](../images/5E7163C0_image 6.png)
![](../images/5E7163C0_image 7.png)
### Confidence Interval Concept Check 4
![](../images/5E7163C0_image 8.png)
Solution:
![](../images/5E7163C0_image 9.png)
$p$ 属于一个 **确定性**的区间的概率，只能是0或者1。不会是其他百分比。

# 4. Confidence Intervals Concept Checks Continued
