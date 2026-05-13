---
title: "Lecture 15. Goodness of Fit Test for Discrete Distributions 对离散分布的拟合优度检验"
date: 2025-08-10
course: 18.6501x
cover: "92C9EF46_image.png"
bear_pk: 92C9EF46-2FDD-4875-8CB2-58616FD80A21
---

# **Lecture 15. Goodness of Fit Test for Discrete Distributions** 对离散分布的拟合优度检验
#Courses/MITx/18.6501x 

## 1. Objectives
At the end of this lecture, you will be able to do the following:
* Understand the difference between parameter estimation, parametric hypothesis testing, and goodness of fit testing.
* Know when and how to apply a **goodness of fit** test for discrete distributions.
* Understand the **categorical distribution** , compute probabilities associated with it, and know how to compute **likelihoods** for a categorical distribution.
* Use the **maximum likelihood estimator** for the categorical distribution.

⠀在本讲座结束时，您将能够做到以下几点：
* 理解参数估计、参数假设检验和拟合优度检验之间的区别。
* 了解何时以及如何应用离散分布的**拟合优度**检验。
* 理解**类别分布**，计算与之相关的概率，并知道如何计算类别分布的**似然函数**。
* 使用类别分布的**最大似然估计量**。


## 2. Introduction to Goodness of Fit Tests
### Recap of Parametric Hypothesis Testing: The Uniform Statistical Model
这道题做错了，需要复习
### Goodness of Fit Tests: Motivation 拟合优度检验：动机
![](../images/92C9EF46_image.png)![](../images/92C9EF46_image 2.png)![](../images/92C9EF46_image 3.png)![](../images/92C9EF46_image 4.png)

### Intuition for Goodness of Fit Tests(TBD)
In the topic goodness of fit testing, we want to decide whether our data can be modeled by a specific type of distribution (**e.g.**, uniform, Gaussian, Poisson). In practice, a useful tool for making such a decision is to use a **histogram** of the data set.
A histogram for a sample data set is shown below. The -axis, which represents the sample space, is divided into the intervals  for all . The bar over the interval  represents **how many** data points took values in that interval.

### Concept Check: Terminology(TBD)


## 3. The Probability Simplex of Discrete Distributions 离散分布的概率单纯形
按黑板上的板书，假设x轴是p1, y轴是p2, 那么 $\Delta k(k=2)$ 就是图中的x+y=1这条线。
更一般的表述： $\Delta_k$ 是所有可能的PMF的集合。 $\mathbb P_p$ 是某个特定PMF p的随机变量的分布。
![](../images/92C9EF46_image 5.png)![](../images/92C9EF46_image 6.png)

**The Probability Simplex in** $K$ **Dimensions** (TBD):
![](../images/92C9EF46_image 7.png)
The probability simplex in , denoted by , is the set of all vectors  (note that we are using subscripts for vector indices for simplicity) such that
where  denotes the vector . Equivalently, in more familiar notation,


## 4. Goodness of Fit Test - Discrete Distributions
### The Goodness of Fit Hypothesis Test for Discrete Distributions（一道练习题，TBD）
### The Goodness of Fit Test: Categorical Likelihoods
![](../images/92C9EF46_image 8.png)
![](../images/92C9EF46_image 9.png)
![](../images/92C9EF46_image 10.png)

我们尝试写出似然函数，那么首先需要写出PMF of X。
multinomial是binomial的扩展形式。所以这里用到了一个小trick，目的是把iff X = a_j的PMF变形为一个连乘形式，所以用到了指示函数。
然后对n个样本的概率连乘，就写出了似然函数。


### Multinomial Distribution （TBD，内容很多）

The **Multinomial Distribution** with $K$ modalities (or equivalently $K$ possible outcomes in a trial) is a generalization of the binomial distribution. It models the probability of counts of the $K$ possible outcomes of the experiment in $n'$ i.i.d. trials of the experiment.
It is parameterized by the parameters $n', p_1, p_2, …, p_K$ where
* $n'$ is the number of i.i.d trials of the experiment;
* $p_i$ is the probability of observing outcome $i$ in any trial, and hence the $p_i$'s satisfy  for all $p_i \ge 0$, and .

Let  and note that .
The multinomial distribution can be represented by a random vector  to represent the number of instances  of the outcome . Note that . The **multinomial pmf** for all  such that , , and  is given by
![](../images/92C9EF46_image 11.png)
**Categorial (Generalized Bernoulli) Distribution and its Likelihood**
The multinomial distribution, when specialized to $n' = 1$  for any $K$ gives the **categorical distribution** . When $K=2$  and the two outcomes are 0  and 1 the categorical distribution is the Bernoulli distribution, and for any $K \ge 2$ the categorical distribution is also known as the **generalized Bernoulli distribution** .
The categorical distribution, therefore, models the probability of counts of the  possible outcomes of a discrete experiment in a single trial. Since the total count is equal to 1 (only one trial), we can use a random variable  to represent the outcome of the trial. This means the sample space of a **categorical random variable**  is


## 5. Maximum Likelihood Estimator for the Categorical Distribution
上一节我们已经写出了似然函数，那么现在需要求解MLE。
首先一个最容易犯的错误就是将其取log后求偏导，这时候算出来的p_j 为无穷大。
→ 为什么？因为没有考虑到一个限制条件 sum p_j = 1。所以我们要将最后一项变形为 1 - sum^K-1 p_j。
现在求解出来了偏导为0时，关于p_j的一个表达式。
![](../images/92C9EF46_image 12.png)

我们现在有K-1个未知数，K-1个方程，但目前还不能单独对每个p_j求解，因为所有方程都依赖所有的变量。
我们将每一个偏导方程都列出来，可以很轻易发现，等式右边都是相等的。
我们令方程右边都等于gamma, 可以发现 p_j = N_j/gamma。
现在求解gamma: 因为sum p_j = 1, 意味着sum N_j/gamma = 1. 又因为sum N_j = n，所以gamma = n.
当然，如果要正式求解，可以利用拉格朗日算子，但这里的内容简单，没必要。

![](../images/92C9EF46_image 13.png)
### Concept Check: Examples of the Categorical Distribution
TBD
### Maximum Likelihood Estimator for Categorical Distribution
这道题里既可以用上面PPT推导出的结论做，也可以用拉格朗日算子，但我不太清楚怎么应用的，后面复习
## 6. Preparation for the Chi-Squared Test
### A Vector Inner Product
这道题完整理论理解需要用到线性代数知识，需要复习
![](../images/92C9EF46_image 14.png)
### A Degenerate Gaussian Random Variable
高斯分布的退化
$\sqrt n(\hat p-p^0)^T*\mathbb 1$ 代表两个向量求内积。（1是n维全1向量），结果是向量的内积之和。
等于 $\sqrt n\sum_{j=1}^K(\hat p_j-p_j^0) = 0 \xrightarrow[n\rightarrow\infty]{}0.$ (p_j的和为1）
![](../images/92C9EF46_image 15.png)
![](../images/92C9EF46_image 16.png)
### Degrees of Freedom of a Known Test
![](../images/92C9EF46_image 17.png)
这道题主要是定义比较复杂。
首先抓住问题中的关键假设：MLE渐进正态性，有：这是MLE渐进正态性的标准通式。
$$
 \sqrt n(\hat\theta^{MLE}_n-\theta^0=*) \xrightarrow[]{d}\mathcal N(0, I(\theta^*)^{-1}) 
$$
在原假设H0下, $\theta^* = \theta^0$， 带入后，MLE的误差 $\hat \theta_n - \theta^0$ 服从正态分布，协方差 $\Sigma$ 是Fisher信息矩阵的逆。
接下来看构造的统计量（结合这一节的PPT与课前练习）,将他转变为一个向量二次型的形式：
$$
 T_n = n\sum_{i=1}^d\frac{(\theta_i^0 - \hat \theta_i)^2}{t_i} \\ = (\sqrt n(\hat \theta_n - \theta^0)^T·I(\theta^0)·(\sqrt n(\hat \theta_n - \theta^0) 
$$
这是一个标准化的平方误差和，类似一个广义形式的Wald统计量。
T_n是一个均值为0、协方差为 $I^{-1}$ 的正态向量经过 $I$ 的二次型。

> 这么写的目的是：
> 1. 便于分析渐进分布：在H0下， $\sqrt n(\hat \theta - \theta^0) \sim N(0, I(\theta^0)^{-1})$
> 2. 将标准正态分布左乘一个矩阵再右乘其转置（标准正态的二次型），正好是卡方分布的定义。？

⠀
接下来做渐进行为分析：
设 $Z_n:= \sqrt n(\hat \theta - \theta^0) \xrightarrow{d} \mathcal N(0, I(\theta^0)^{-1})$。那么，有：
$T_n = Z_n^T \Sigma^{-1} Z_n \xrightarrow{d} \chi_d^2$, 这里的 $\Sigma = I^{-1}$。
**这里用到了定义（虽然Z_n不是标准正态分布，但左右乘上了I(theta)，就起到了标准化的作用。**
> [!IMPORTANT]
> 任何形如 $Z_n^T \Sigma^{-1}, \text{where }Z\sim\mathcal N(0, \Sigma), 都服从\chi_d^2$。

还有另一种思路：独立标准正态随机变量的平方和服从自由度为d的卡方分布。
那么，我们要构造出这类随机变量的平方和形式，需要将T_n进行变形。
![](../images/92C9EF46_image 18.png)


## 7. The Goodness of Fit Test for Discrete Distributions: Chi-Squared Test
### The Chi-Squared Test for Testing Goodness of Fit of Discrete Distributions


#Stats-ML
