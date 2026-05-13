---
title: "Lecture 18. Introduction to Bayesian Statistics 贝叶斯统计导论"
date: 2025-08-10
course: 18.6501x
cover: "B13572B8_image.png"
bear_pk: B13572B8-B07E-4A90-A77B-FE6AA6458206
---

# **Lecture 18. Introduction to Bayesian Statistics 贝叶斯统计导论**
#Courses/MITx/18.6501x

## 1. Motivation 动机
## 2. Objectives
### Bayesian Statistics Part 1
At the end of this lecture, you will be able to do the following:
* Describe the **Bayesian approach** to statistical decision making.
* Explain the mechanisms of the Bayesian approach, particularly the **prior and posterior beliefs** .
* Understand the role and significance of the prior distribution in a Bayesian set-up.
* Identify the **Beta distribution** and its role in Bayesian statistics as a prior distribution on a one-dimensional parameter.

⠀The Unit 5 slides below, which are for the next **2 lectures** , are also available in the resource tab at the top of this course site.


## 3. Introduction to the Bayesian Framework
### Frequentist vs Bayesian Approaches
频率学派认为未知参数 $\theta^*$ 是一个固定的常数，而贝叶斯学派认为未知参数是一个已知分布的随机变量。
频率学派认为需要重复试验才可以得到一个置信区间，而贝叶斯学派关注实验只进行一次。
注意：在统计建模（statistical model) 中，需要先假设:
* 参数集合 $\Theta$
* 概率模型 $\mathbb P_{\theta}$

⠀这是基本步骤，不管是频率学派还是贝叶斯学派都需要做。
~[Lecture 14. Introduction to Bayesian inference 贝叶斯统计推断导论](https://www.notion.so/Lecture-14-Introduction-to-Bayesian-inference-2356f10f26688058baded4e94e0ff0c5?pvs=21)~
![](../images/B13572B8_image.png)![](../images/B13572B8_image 2.png)![](../images/B13572B8_image 3.png)


## 4. Basic Example of the Bayesian Approach
以kiss案例为例：
频率学派视角里，我们利用MLE估计 $p$，构建关于 $p$ 的置信区间，进行假设检验，例如H0为 $p=0.5$。在分析数据之前，我们认为 $p$ 接近1/2。

而贝叶斯视角是一个工具，可以用数据来更新我们的先验信念。
首先，我们对于 $p$ 的先验信念是可以被量化的。
所以，我们可以利用关于 $p$ 的分布来刻画我们的先验信念（假设 $p$ 是一个随机变量）。
虽然在现实中，真值参数不是随机变量。但贝叶斯视角可以利用将其假设为随机变量来刻画我们对于未知参数的信念。
例如，假设 $p \sim \text{Beta}(a, b)$. 这里的beta分布就是先验分布。
在我们的统计实验中， $X_1, …, X_n$ 被视为在给定 $p$ 条件下的，关于参数 $p$ 的IID伯努利随机变量。
在进行实验后，我们可以更新关于 $p$ 的信念，基于实验数据的条件分布。
给定实验结果的条件下， $p$ 的分布为后验分布。
在这个案例中，后验分布为：
$$
 \text{Beta}(a+\sum_{i=1}^nX_i, b+n-\sum_{i=1}^nX_i) 
$$
![](../images/B13572B8_image 4.png)![](../images/B13572B8_image 5.png)
![](../images/B13572B8_image 6.png)

### **Mode of the Beta Distribution beta分布的众数**

Recall that the **Beta distribution** in $x$ is defined as the distribution with support [0, 1] and pdf
$$
 C(\alpha, \beta)x^{\alpha-1}(1-x)^{\beta-1} 
$$
where $\alpha$ and $\beta$ are parameters that satisfy $\alpha >0, \beta >0$. Here,  $C(\alpha, \beta)$ is a normalization constant that does not depend on $x$ .
The Beta distribution can take many shapes depending on the chosen parameters $\alpha$ and $\beta$. As a result, the highest point (mode) of this distribution can vary wildly. Due to the different overall shapes depending on parameter values, there isn't also a consistent formula for the mode. Compute the correct mode for each of the parameter sets. (A mode of the distribution is the value(s) of $x$ where the pmf attains its highest value in the entire support of the distribution.)
You may use the variables  $\alpha$ and $\beta$  in your answer. If there is no unique mode, enter -1. Note that it is possible for the mode to have a “probability" of infinity, which would be a mode if this happens only once.

这道题是求解beta分布的众数(mode)。
一个分布的众数的定义是PMF在自身支撑集内取得最大值时的x的取值。
首先观察分布的PDF的形式。可以看到：在 $\alpha >1$ 时， x单调递增， 小于1时单调递减；同样，在 $\beta >1$ 时，(1-x)单调递减， 小于1时单调递增。

**Case 1: $\alpha < 1 \ and \ \beta <1$：**
这个时候需要观察: $\alpha < 1$ 时, $x^{\alpha-1}$ 在x趋近0时无穷大； 同样的，在 $\beta <1$ 时, $(1-x)^{\beta-1}$ 在x趋近于1时无穷大。所以这种情况下有两个众数:0和1.
**Case 2: $\alpha \le 1 \ and \ \beta \ge1, \ \text{but excluding } \alpha = \beta =1$**
这种情况下，整个函数是单调递减的，那么众数出现在x的最小值0。
**Case 3: $\alpha \ge 1 \ and \ \beta \le1, \ \text{but excluding } \alpha = \beta =1$**
这种情况下，整个函数是单调递增的，那么众数出现在x的最小值1。
**Case 4:  $\alpha =1 \ and \ \beta=1$**  
此时函数变为固定值 $C(\alpha, \beta)$。在定义域内都是众数。
**Case 5: $\alpha > 1 \ and \ \beta > 1$**
这是最标准的形式，对原函数取Log后求导，解得：
$$
 x = \frac{\alpha-1}{\alpha+\beta—2} 
$$
这是标准形式下beta分布众数的通解。

### **Beta Distribution Probability Example**
Suppose that you have a coin with unknown probability $p$ of landing heads; assume that coin toss outcomes are i.i.d Bernoulli random varaiables. You flip it 5 times and it lands heads thrice. Our parameter of interest is $p$. Compute the likelihood function for the first five tosses $X_1, X_2, …, X_5$.

这道题是利用beta分布来解题的案例。
首先，对应的似然函数为 $L(X_1, X_2, …, X_5; p) = p^3(1-p)^2$
这个似然函数等价于一个固定比例的beta分布。按照beta分布的形式，我们可知： $\alpha-1 = 3, 所以\alpha = 4, \beta = 3$。
接下来再次进行5次实验，正面朝上出现4次。这时候似然函数会变成 $p^7(1-p)^3$
最后，在频率学派视角里，**这个似然函数的MLE等同于其众数对应的x值。** $MLE = \frac{\alpha-1}{\alpha + \beta -2} = 7/10 = 0.7$


## 5. The Prior Distribution
**Clinical Trial Examples, Source of Priors**
![](../images/B13572B8_image 7.png)![](../images/B13572B8_image 8.png)


## 6. Review: Conditional Likelihood and Bayes' Rule
略


## 7. The Posterior Distribution, Bayes' Formula
**Prior to Posterior**
贝叶斯学派与频率学派的区别就在于似然函数再多乘一个先验概率pi(theta)。
分母在这里不重要，后验概率是一个常数的一部分，并且这个常数不依赖theta。
如果对分子也在theta上积分，右边的结果是1。
![](../images/B13572B8_image 9.png)![](../images/B13572B8_image 10.png)![](../images/B13572B8_image 11.png)![](../images/B13572B8_image 12.png)
### 练习题
**Prior Implications to Posterior: True or False**
TBC
**Updating Prior (Belief Propagation)**
TBC


## 8. Warm-up / Review: Proportionality
### Distributions with One Parameter
TBC
这个题看得有点云里雾里的
### Distributions with Two Parameters
TBC


## 9. Bayes' Formula with the Beta Distribution
**Application: Bernoulli Experiment with the Beta Prior**
TBC
