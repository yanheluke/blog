---
title: "Lecture 10. Other Methods of Estimation: Method of Moments and M-Estimation 其他估计方法：矩方法和M-估计"
date: 2025-08-10
course: 18.6501x
cover: "40A6E9C5_image.png"
bear_pk: 40A6E9C5-5E59-46A2-BD24-E0030EFBD49F
---

# Lecture 10. Other Methods of Estimation: Method of Moments and M-Estimation 其他估计方法：矩方法和M-估计
#Courses/MITx/18.6501x

## 1. Other methods of estimation
### Objectives
At the end of this lecture, you will be able to do the following:
* Extend the principles of maximum likelihood estimation to the more general M-estimation approach favored in machine learning.
* Define an **M-estimator** for the **mean** , **median** , and **quantile** of an unknown distribution.
* Compare and contrast the maximum likelihood estimator and the method of moments .

## 2. Introduction to M-estimation
M: minimization
![](../images/40A6E9C5_image.png)
我们可以将KL散度替换为任意的损失函数，只要这个损失函数能够转化为期望形式，后面的推导步骤就与MLE类似。
关键的统计技巧（statistical trick）来定义M-estimator是用均值（average）来代替期望（expectation）。
![](../images/40A6E9C5_image 2.png)
如果我们定义损失函数 loss function $\rho(x,\mu)$，有以下形式：
$$
 \mu ^* = \arg\min\limits_{\mu\in \mathbb R} \mathbb{E}_{X\sim \mathbf{P}}[\rho(X,\mu)] 
$$
利用统计技巧，将期望替换为均值，那么有：
$$
 \hat\mu = \arg\min\limits_{\mu\in \mathbb R}\frac{1}{n}\sum\limits_{i=1}^n[\rho(X_i, \mu)] 
$$
这里的 $\hat \mu$ 是 $\rho(x, \mu)$ 的M-estimator.

## 3. M-estimation
![](../images/40A6E9C5_image 3.png)

使用M-estimator的问题是，如何找到一个合适的 $\rho$，来代表我们想计算的统计量（期望/方差/中位数/其他分位数）？
下面，通过一个例子：定义 $\rho(x, \mu) = (x-\mu)^2$, 推导对 $\mu$ 求一阶导，可以得到 $\mu = \mu^*$。说明这个损失损失函数是求期望 $E(X)$。
![](../images/40A6E9C5_image 4.png)

以下是期望、中位数的损失函数 $\rho$ 定义。
![](../images/40A6E9C5_image 5.png)

特别的，如果想定义一个求分位数的损失函数，用到的技巧是：
绝对值损失函数 $\rho(x, \mu) = |x-\mu|$ 是一个对称函数， $\mu^*$ 是中位数。那么将这个函数进行倾斜（等于重心进行了偏移），那么这个Check function就可以求解任何分位数 $\alpha$。
![](../images/40A6E9C5_image 6.png)
![](../images/40A6E9C5_image 7.png)
![](../images/40A6E9C5_image 8.png)

### M-estimation
Let $X_1, … ,X_n$ be i.i.d. with some unknown distribution $\mathbf{P}$ and an associated parameter $\mu^*$ on a sample space $E$. We make no modeling assumption that $\mathbf{P}$  is from any particular family of distributions.
An **M-estimator** $\widehat \mu$ of the parameter $\mu^*$ is the **argmin of an estimator of a function** $\mathcal{Q}(\mu)$  **of the parameter** which satisfies the following:
* $\mathcal{Q}(\mu) = \mathbb{E} [\rho(X, \mu)]$ for some function $\rho: E \times \mathcal M \rightarrow \mathbb R$ where  $\mathcal M$ is the set of all possible values of the unknown true parameter $\mu^*$;
* $\mathcal{Q}(\mu)$ attains a **unique** minimum at $\mu = \mu^*$  in $\mathcal M$.  That is, $\arg\min_{\mu\in\mathcal M}\mathcal Q(\mu) = \mu^*$.

⠀In general, the goal is to find the **loss function** $\rho$  such that $\mathcal{Q}(\mu) = \mathbb{E} [\rho(X, \mu)]$ has the properties stated above.
Note that the function $\rho(X, \mu)$ is in particular a function of the random variable $X$ and the expectation in $\mathbb{E} [\rho(X, \mu)]$ is to be taken against the **true distribution** $\mathbf P$ of  $X$, with associated parameter value $\mu^*$.
Because $\mathcal Q(\mu)$ is an expectation, we can construct a (consistent) estimator of $\mathcal Q(\mu)$ by replacing the expectation in its definition by the sample mean.

### Median as a Minimizer
这道题很复杂
首先是median of 连续随机变量X的定义为 $med(X) \in \mathbb R$:
$$
 P(X > \text{med}(X)) = P (X < \text{med}(X)) = \frac{1}{2} 
$$
在这个问题中，我们要求解的是：任意median符合下列条件：
$$
 \text{med}(X) = \arg\min_{\mu\in\mathbb R}\mathbb E[|X-\mu|] 
$$
Step1: 用密度函数 $f(x)$ 来表示 $\mathbb E[|X-\mu|]$:
按照期望的定义:
$$
 \begin{aligned} \mathbb E[|X-\mu|] &= \int_{-\infty}^{+\infty}|x-\mu|f(x)dx \\ &= \int_{-\infty}^{\mu}(\mu-x)f(x)dx + \int_{\mu}^{+\infty}(x-\mu)f(x)dx \\ &= \int_{\mu}^{+\infty}xf(x)dx - \int_{-\infty}^{\mu}xf(x)dx - \mu(\int_{\mu}^{+\infty}f(x)dx - \int_{-\infty}^{\mu}f(x)dx)
\end{aligned} 
$$

Step2: 令 $\mathcal Q(\mu) = \mathbb E[|X-\mu|]$, 对 $\mu$ 求导：
$$
 \begin{aligned} \frac{d}{d\mu}\left(\int_\mu^\infty xf(x)dx\right) &= -\mu f(\mu) \quad \text{利用积分基本定理}\\ \frac{d}{d\mu}\left(\int_{-\infty}^\mu xf(x)dx\right) &= \mu f(\mu) \end{aligned} 
$$
$$
 \frac{d}{d\mu}\left(\mu(\int_{\mu}^{+\infty}f(x)dx - \int_{-\infty}^{\mu}f(x)dx)\right) \\ = (\int_{\mu}^{+\infty}f(x)dx - \int_{-\infty}^{\mu}f(x)dx) + \mu*(-f(\mu)-f(\mu)) \\ = \int_{\mu}^{+\infty}f(x)dx - \int_{-\infty}^{\mu}f(x)dx - 2\mu f(\mu)
$$
合并结果，得到：
$$
 \begin{aligned} \mathbb E[|X-\mu|] &= -\mu f(\mu) - \mu f(\mu) - \int_{\mu}^{+\infty}f(x)dx + \int_{-\infty}^{\mu}f(x)dx + 2\mu f(\mu) \\ &= \int_{-\infty}^{\mu}f(x)dx - \int_{\mu}^{+\infty}f(x)dx
\end{aligned} 
$$

Step 3: 求解 $\mathcal Q^\prime(\text{med}(X))$：
$$
 \begin{aligned} \mathcal Q^\prime(\text{med}(X)) &= \int_{-\infty}^{\text{med}(X)}f(x)dx - \int_{\text{med}(X)}^{+\infty}f(x)dx \\ &= P(X < \text{med}(X)) - P(X >\text{med}(X)) \\ &= 1/2 -1/2 \\ &= 0 \end{aligned}
$$
注意到第二问的结论，由CDF（概率分布函数）的性质，有：
$$
 \begin{aligned} \mathcal Q^\prime(\mu)
&= \int_{-\infty}^{\mu}f(x)dx - \int_{\mu}^{+\infty}f(x)dx \\ &= F(\mu)-(1-F(\mu)) \\ &= 2F(\mu) -1 \end{aligned} 
$$
### Quantile as a Minimizer
TBC
与上一题类似
### (Optional) Convexity of the Expectation of the Loss Function
TBC

## 4. (Optional) Preparations for the Asymptotic Normality of M-estimators
这里定义了两个新的矩阵（matrices）： J matric和K matric
主要用于计算渐进方差。对比之前的MLE，这里有一些形式上的扩展变形。
* J矩阵：损失函数的曲率（二阶导），也是二阶导数的期望。反应曲率信息：目标函数在 $\mu^*$ 附近的凸性。——来自delta method.
* K矩阵：损失函数的协方差，反映波动信息：梯度估计的稳定性 ——来自渐进协方差矩阵

⠀可以注意到，在参数为一维的特殊情况下， $\mathbf J$ 和 $\mathbf K$ 就是Fisher Information的两种等价形式。
![](../images/40A6E9C5_image 9.png)
![](../images/40A6E9C5_image 10.png)

**The** $\mathbf J$ and  $\mathbf K$ **matrices** :
Let $\mathbf X_1, … , \mathbf X_n$ be i.i.d. random vector in $\mathbb R^k$ with some unknown distribution  $\mathbf P$ with some associated parameter $\vec \mu^*\in\mathbb R^d$   on some sample space $E$.   Let $\mathcal Q(\vec \mu) = \mathbb E[\rho(\mathbf X, \vec\mu)]$ for some function $\rho: E \times \mathcal M \rightarrow \mathbb R$  where $\mathcal M$ is the set of all possible values of the unknown true parameter $\vec\mu^*$.
Then the matrices $\mathbf J$  and $\mathbf K$ are defined as
![](../images/40A6E9C5_image 11.png)
In one dimension, i.e. $d=1$, the matrices reduce to the following:
$$
 \begin{aligned} J(\mu) &= \mathbb E\left[\frac{\partial^2\rho}{\partial\mu^2}(X_1,\mu)\right] \\ K(\mu) &= \text{Var} \left[\frac{\partial\rho}{\partial\mu}(X_1,\mu)\right] \end{aligned}
$$


## 5. (Optional) Asymptotic Normality of M-estimators
需要复习一下Fisher Information的推导过程。
回忆一下如何证明MLE的渐进正态性：
* 首先对Log-likelihood的一阶导做泰勒展开
* 再进行二阶导

⠀![](../images/40A6E9C5_image 12.png)
### Asymptotic normality of the M-estimators
这一段内容描述M-估计量的渐进正态性。用于解决：
* **估计量的分布性质**：当样本量 $n\rightarrow\infty$ 时，估计量 $\widehat \mu$ 的标准化形式收敛于某个分布 $Q$ （通常为正态分布）。
* **统计推断基础**：为构建置信区间（例如 $\mu^* \pm 1.96\times标准误$)和假设检验提供理论依据。

⠀Let $\mathbf X_1, … , \mathbf X_n \stackrel{\text{iid}}{\sim} \mathbf P$ . Let $\rho(x, \mu)$ denote a loss function satisfying
$$
 \mu^* = \arg\min_{\mu\in\mathbb R}\mathbb E[\rho(X_1, \mu)] 
$$
where  $\mu^*\in\mathbb R$ is some unknown one-dimensional parameter associated with $\mathbf P$  that we would like to estimate. Let
$$
 \begin{aligned} J(\mu) &= \mathbb E\left[\frac{\partial^2\rho}{\partial\mu^2}(X_1,\mu)\right] \\ K(\mu) &= \text{Var} \left[\frac{\partial\rho}{\partial\mu}(X_1,\mu)\right] \end{aligned} 
$$
You construct the M-estimator $\widehat\mu$ associated $\rho$.
Assuming that the conditions for the asymptotic normality of this M-estimator hold, we have
$$
 \sqrt n\frac{\widehat\mu-\mu^*}{\sqrt{J(\mu^*)^{-2}K(\mu^*)}}\xrightarrow[n\rightarrow\infty]{(d)}Q 
$$
for some distribution .
根据M-estimator的渐进正态性，可以推导出 $\widehat\mu$ 的渐进方差为： $J(\mu^*)^{-2}K(\mu^*)$.
因此，
$$
 \sqrt n\frac{\widehat\mu-\mu^*}{\sqrt{J(\mu^*)^{-2}K(\mu^*)}}\xrightarrow[n\rightarrow\infty]{(d)}\mathcal N(0,1) 
$$
即收敛于标准正态分布（或者说极限分布Q为标准正态分布）。
**这里在进行推导时利用了 $X_1$ 计算期望而非全体 $X$。因为样本满足iid，任意单一样本 $X_i$ 的分布均等同于总体分布 $\mathbf P$，使用 $X_1$ 可以代表总体分布的性质，同时避免冗余的求和符号。**

## 6. Robust Statistics
### Robust Statistics, Cauchy Distribution
![](../images/40A6E9C5_image 13.png)
![](../images/40A6E9C5_image 14.png)

## 7. Moments of a random variable
![](../images/40A6E9C5_image 15.png)
trick: 计算Ber(p)的二阶矩时，既可以使用定义: $E[X^2] = \text{Var}[X] + (E[X])^2 = p(1-p)+p^2 = p$，也可以从定义上看：由于X的取值只有0和1，所以X^2的取值也是0和1，所以X^2 = X, 所以 $E[X^2] = E[X]$.
**Let $X \sim \mathcal N(0,1)$. Compute its moment of order $2k+1$ for any integer $k \geq 0$.**
**标准正态分布的奇数阶矩恒为0。**
两个证明方式：
1. 因为X和-X有相同的分布，即 $f(x) = f(-x)$。所以：
$$
 \mathbb EX^{2k+1} = \mathbb E(-X)^{2k+1} = (-1)^{2k+1}\mathbb EX^{2k+1} 
$$
由于k是一个非负整数，所以 $\mathbb EX^{2k+1} =0$

2. 从期望的定义出发证明，利用 $g(x) = x^{2k+1}e^{-x^2/2}$ 为奇函数，奇函数在对称区间上 $[-a, a]$ 上的积分为0的性质来求解。 


### Mapping Parameters to Moments I

## 8. Moment Generating Function
![](../images/40A6E9C5_image 16.png)
![](../images/40A6E9C5_image 17.png)
![](../images/40A6E9C5_image 18.png)

### MGF of the Exponential Distribution 求解指数分布的矩母函数
指数分布的密度函数为：
$$
 f_X(x) = \lambda e^{-\lambda x}, \quad x\geq0, \lambda >0 
$$
矩母函数的计算公式实质上是求 $e^{tx}$ 的期望，所以有：
$$
 \begin{aligned} M_X(t) &= \mathbb E[e^{tx}]=\int_0^{+\infty}e^{tx}\lambda e^{-\lambda x}dx \\ &= \lambda \int_0^{+\infty}e^{tx}e^{-\lambda x}dx \\ &= \lambda \int_0^{+\infty}e^{(t-\lambda)x}dx \end{aligned} 
$$
上面的广义积分如果需要收敛，需要满足条件：指数部分<0。所以有： $t-\lambda <0$.
所以有：
$$
 \begin{aligned} M_X(t) &= \lambda \int_0^{+\infty}e^{(t-\lambda)x}dx \\ &= \lambda \frac{e^{(t-\lambda)x}}{t-\lambda}\bigg|_0^{+\infty}\\ &= \lambda(0-\frac{1}{t-\lambda})\\ &= -\frac{\lambda}{t-\lambda} \quad \text{when}\quad t<\lambda \end{aligned} 
$$
现在如果需要求 $\lambda = 2$ 时，X的8阶导：
$$
\begin{align}
 M_X(t) = \frac{-2}{t-2} = (-2)(t-2)^{-1} 
\\
 m_8 = \mathbb E[X^8] = \frac{d^8}{dt^8}(-2)(t-2)^{-1}\bigg|*{t=0}
\\
 由：\frac{d^k}{dx^k}\frac{1}{x} = \frac{(-1)^kk!}{x^{k+1}}
\\ 
有: m_8 = -2*\frac{(-1)^88!}{(t-2)^9}\bigg|*{t=0}\\ = \frac{8!}{(-2)^9}
 \\
 = 157.5
\end{align}
$$

## 9. The method of moments
![](../images/40A6E9C5_image 19.png)
![](../images/40A6E9C5_image 20.png)

### Method of Moments Concept
Let $(E, \{\mathbf P_\theta\}*{\theta\in\Theta})$ denote a statistical model associated to a statistical experiment $X_1, …, X_n \stackrel{\text{iid}}{\sim} \mathbf P*{\theta^*}$ where $\theta^*\in\Theta$ is the true parameter. Assume that  $\Theta\subset \mathbb R^d$ for some $d \geq 1$. Let  $m_k{(\theta)} := \mathbf E[X^k]$ where $X \sim \mathbf P_\theta$. $m_k{(\theta)}$  is referred to as the $k$**-th moment of** $\mathbf P_\theta$ . Also define the moments map:
$$
 \begin{aligned} \psi: \Theta &\rightarrow \mathbb R^d \\ \theta &\mapsto (m_1(\theta), m_2(\theta)..., m_d(\theta)) \end{aligned} 
$$
Assume that $\psi$  is one-to-one (and hence, invertible).
> Note: $\mapsto$ 用latex打是\mapsto, 代表函数映射
> one-to-one: 单射
> $\psi$： 希腊字母psi

设 $(E, \{\mathbf P_\theta\}*{\theta\in\Theta})$ 表示一个统计模型，对应统计实验 $X_1, …, X_n \stackrel{\text{iid}}{\sim} \mathbf P_{\theta^*}$，其中 $\theta^*\in\Theta$ 是真实参数。 假设  $\Theta\subset \mathbb R^d$ ($d \geq 1$) 。定义：
$m_k{(\theta)} := \mathbf E[X^k]$ ，其中 $X \sim \mathbf P_\theta$。
$m_k{(\theta)}$  被称为 **$\mathbf P_\theta$**的 $k$ 阶矩。同时定义矩映射：
$$
 \begin{aligned} \psi: \Theta &\rightarrow \mathbb R^d \\ \theta &\mapsto (m_1(\theta), m_2(\theta)..., m_d(\theta)) \end{aligned} 
$$
**真实参数 $\theta^*$ 等于什么？**
根据定义，真实参数 $\theta^*$ 满足：
$$
 \psi(\theta^*) =(m_1(\theta^*), m_2(\theta^*)..., m_d(\theta^*)) 
$$
由于 $\psi$ 是一一对应且可逆的，所以真实参数 $\theta^*$ 为：
$$
 \theta^* =\psi^{-1}(m_1(\theta^*), m_2(\theta^*)..., m_d(\theta^*)) 
$$
**真实参数 $\theta^*$ 的矩估计量是什么？**
矩估计法的核心是**用样本矩代替总体矩。对每个** $k=1,2,…,d$， 用样本矩 $\frac{1}{n}\sum_i^nX_i^k$ 来估计 $m_k(\theta^*)$。所以矩估计量为：
![](../images/40A6E9C5_image 21.png)
### Applying the Method of Moments to a Gaussian Statistical Model
![](../images/40A6E9C5_image 22.png)正态分布的矩定义：
* 一阶矩（期望）： $m_1 = \mathbf E[X] = \mu$
* 二阶矩: $m_2 = E[X^2] = \sigma^2 + \mu^2$

⠀接下来，我们要用样本来估计这两个矩：
* $\widehat m_1 = \frac{1}{n}\sum_i^nX_i$
* $\widehat m_2 = \frac{1}{n}\sum_i^nX_i^2$

⠀带入题中给定的四个样本进行计算：
$$
 \widehat m_1 = 0.225,\quad \widehat m_2 = 2.3975 
$$
再利用正态分布矩的定义求解期望和方差：
$$
 \widehat \mu^{MM} = \widehat m_1 = 0.225\\ \widehat \sigma^{MM} = \sqrt{\widehat m_2 - \widehat m_1^2\\} = 1.5326
$$
### Plus Minus 1 - Method of Moments
TBC
### Method of Moments - Multiple Estimators
TBC

# 10. (Optional) Asymptotic Normality of the Method of Moments Estimator
### Lectures
TBC

# 11. Conclusions
![](../images/40A6E9C5_image 23.png)MLE是最好的参数估计方法：虽然三种方法都具有渐进正态性，但MLE的渐进方差是最小的。MLE具有最小的边界：Cramer-Rao Lower Bound.
