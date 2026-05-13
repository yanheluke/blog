---
title: "[Lecture 20] Linear Regression 1 线性回归1"
date: 2025-08-08
course: 18.6501x
cover: "B4A3781D_image.png"
bear_pk: B4A3781D-AFDD-4BFC-A637-60D39BF26BBD
---

# **[Lecture 20] Linear Regression 1 线性回归1**
#Stats-ML #Courses/MITx/18.6501x

## **1. Motivation** 动机


## **2. Objectives**
**Linear Regression**

At the end of this lecture, you will be able to do the following:
* Understand the **goals of regression** .
* Identify the **regression function** and know what property of the **dependent** random variable the regression function is trying to capture as a function of the **explanatory variables** .
* Plot and understand **box-and-whisker plots** .
* Know the **linear regression function** .
* Understand the **theoretical** and **empirical** linear regression solutions.
* Write the linear regression problem as a **noisy linear model** .

⠀The Unit 6 slides below, which are for the next **2 lectures** , are also available in the resource tab at the top of this course site.

## **3. Goals of Regression**
![](../images/B4A3781D_image.png)<!-- {"width":736} -->
![](../images/B4A3781D_image 2.png)![](../images/B4A3781D_image 3.png)<!-- {"width":761} -->

## **4. Modeling Assumptions in Regression** 回归的模型假设
### Review: Joint, Conditional, and Marginal Distributions
复习联合分布与边缘分布。
假设 $(X,Y)$ 是一对随机变量并且联合密度为 $h(x,y) = x+y$, 定义域是 $[0,1]^2$ 。
1. **求X的边缘密度函数。**
边缘密度函数就是联合密度函数对另一个变量积分，所以:
$$
h(x) = \int_0^1h(x,y)dy = \int_0^1(x+y)dy = x+\frac{1}{2}
$$
2. **求给定 $X = x$ 时，Y的条件密度函数 $h(y|x)$ 。**
条件密度函数就是联合密度函数除以另一个变量的边缘密度函数。
$$
h(y|x) = \frac{h(x,y)}{h(x)} = \frac{x+y}{x+1/2}
$$
3. **求条件方差 $Var(Y|X=x)$** 
求条件方差还是需要从定义入手：先求条件期望，再求条件二阶矩，然后用方差定义。
$$
\mathbf E[Y|X=x] = \int_0^1yh(y|x)dy = \frac{3x+2}{3(2x+1)}
$$
然后求条件二阶矩：
$$
\mathbf E[Y^2|X=x] = \int_0^1y^2h(y|x)dy = \frac{4x+3}{6(2x+1)}
$$
最后条件方差就是用定义：
$$
Var(Y|X=x) = \mathbf E[Y^2|X=x] - (\mathbf E[Y|X=x])^2
$$
标准答案可以不用化简，但化简其实是最浪费时间的。

### Review: Joint, Conditional, and Marginal Distributions: Discrete Example
> [!IMPORTANT]
> $X$ 是一个服从泊松分布的离散随机变量。给定 $X=x$, $Y$ 是一个二项随机变量 $\text{Binom}(x,p)$ 

1. 给定 $X=x,\ Y$ 的上下界分别是多少？
首先翻译这这道题给出来的条件：
$X \sim \text{Poisson}(\lambda)$
$Y|X=x \sim \text{Binom}(x,p)$
由于二项分布的取值是从0到n的整数（二项分布的Y是在n次实验里成功的次数），这里n = x, 所以Y的取值范围就是最小0次，最大n=x次。

2. $E[Y|X=x]$ 和 $x$ 的关系。
二项分布的期望是np。在这道题里，由于n = x, 所以条件分布的期望：
 $E[Y|X=x] = xp$

3. 求无条件期望 $E[Y]$ 。
需要用到迭代期望定律（laws of iterated expectation)： $E[Y] = E[E[Y|X]]$ 。
由前两问，可以知道
$$
\begin{aligned}
E[Y|X=x] &= xp \\
E[Y|X] &= Xp\\
E[Y] &= E[E[Y|X]] = E[Xp] = pE[X] = p \lambda 
\end{aligned}
$$

### **Modeling Assumptions**
在线性回归中，我们关心的是 $h(y|x)$ ，并不关心 $h(x)$。 
![](../images/B4A3781D_image 4.png)

## **5. Partial Modeling, Regression Function, and Conditional Quantiles**
如果想要精确的描述X和Y的关系是非常复杂的一个事情，因为需要对每一个X的取值都估计一个密度。因此，我们只考虑描述在X条件下的一部分Y的性质（期望、中位数、分位数等）。这被称为部分建模（Partial Modeling)。

**期望**
给定 $X=x$, $Y$ 的条件期望方程被称为回归方程。
$$
\begin{aligned}
x \mapsto f(x) := \mathbb E[Y|X=x] &= \int yh(y|x)dy \\
&= \sum_{\Omega_Y}y\cdot\mathbf P(Y=y|X=x)
\end{aligned}
$$
**其他概率**
* 条件中位数
* 条件分位数
* 条件方差
![](../images/B4A3781D_image 5.png)

### Concept Check: Conditional Quantile 概念复习：条件分位数
> [!IMPORTANT] 
> 令 $(X,Y)$  是一对随机变量并且联合密度 $f(x,y)=x+y$，定义域为 $[0,1]^2$ 。
> 给定x, 求分位数 $q_\alpha(x)$ 使 $P[Y\le q_\alpha(x)|X=x] = 1-\alpha$ 。这个等于是求 $Y|X=x$ 的 $(1-\alpha)$ -分位数函数。

首先得到Y|X的条件密度函数 $h(y|x) =(x+y)/(x+1/2)$ 。
然后根据定义，写出条件分位数的概率：
$F_{Y|X}(y|x) = \int_0^qh(y|x)dy = 1-\alpha$
解这个方程，可以得到一个q的二次方程，求q在[0,1]内的根，即可。

## **6. Plots of Conditional Distributions and Conditional Quantiles and Box-and-Whisker Plots**

第一章PPT是一个标准的线性回归方程。
![](../images/B4A3781D_image 6.png)

接下来三张PPT用离散分布来说明。

![](../images/B4A3781D_image 7.png)

离散分布的概率密度
![](../images/B4A3781D_image 8.png)

离散分布的箱型图。
箱型图包含了：25%分位数、中位数、75%分位数。所以箱型图里的总概率为50%，超过箱型图的点被认为是离群点（outliers)。
箱型图的大小可以说明条件方差的变动。
![](../images/B4A3781D_image 9.png)


## **7. Linear Regression - Basic Setup**
### Linear Regression: The Function for Conditional Expectation of Y Given a value x

在线性回归中，我们都基于这样一个假设：回归方程（regression function) 是线性的。
这是一个假设，因为E[Y|X=x]有无数种形式，我们需要假设最简单的一种形式，即
$$
v(x) := \mathbb E[Y\mid X=x] = a+bx
$$
![](../images/B4A3781D_image 10.png)
![](../images/B4A3781D_image 14.png)![](../images/B4A3781D_image 15.png)

> [!IMPORTANT]
> **最小化问题（Minimization Problem)：**
> 假设 $X$ 是一个任意的随机变量，均值和方差为 $\mu, \sigma$ 。现在我们计算一个标量 $k$ ，使方程 $f(k) = \mathbb E[(X-k)^2]$ 最小。

对f(k)进行化简，有：$f(k) = E[X^2-2kX+k^2]  = E[X^2] - 2kE[X] + k^2$
由于已知均值和方差，所以有： $f(k) = \sigma^2+\mu^2 - 2k*\mu + k^2$
这是一个关于k的二次函数，求极值就是函数求导。
$k = \arg\min f(k) = E[X] = \mu$
这个结论说明：对任意随机变量，要令其距离k的欧氏距离的期望最小，那么这个k就是他自身的期望。

由此引出下一道题：
> [!IMPORTANT]
> **估计量（Estimator)**
> 回归方程： $v(x) := \mathbb E[Y\mid X=x] = a+bx$ ,如果令 $\hat Y = g(X)$, 那么 $\hat Y$ 取什么值，可以令：
> $$
> \mathbb E[(Y-\hat Y)^2\mid X =x]
> $$ 
> 最小。

这道题有两个解法，一是按照上一题的结论，可以得到 $\hat Y = \arg\min \mathbb E[(Y-\hat Y)^2\mid X =x] = E[Y] = v(x) = a+bx$
另一种解法是按照定义打开期望（计算方式与上面相同）。 

These two exercises verify that the Least Squares Estimator is consistent in the following sense: **using the actual distribution on $(X,Y)$  , the true pair $(a,b)$ itself is a least squares estimator.** 

## **8. Probabilistic Analysis of Theoretical Linear Regression** 理论线性回归的概率分析

### Derivation of Theoretical Linear Least Squares Regression I

### Derivation of Theoretical Linear Least Squares Regression II

### **Optimal Theoretical Regression Line**

理论线性回归（theoretical linear regression) 是使线性回归方程与Y的平方偏差期望最小的一条线，即：
$$
(a^*, b^*) = \arg\min_{(a,b)\in\mathbb R^2}\mathbb E[(Y-a-bX)^2]
$$
接下来求解a和b。
> 这里有一个化简的技巧：偏导和期望符号可以任意交换。在统计的课程上这个技巧永远成立。
分别对a和b求偏导，令其等于0，有：
$$
\begin{align}
\frac{\partial}{\partial a}\mathbb E[(Y-a-bX)^2] &= E[Y]-a^*-b^*E[X]=0 \\
\frac{\partial}{\partial b}\mathbb E[(Y-a-bX)^2] &= E[XY]-a^*E[X]-b^*E[X^2] = 0 \\
\text{化简得：}\\
a^* &= E[Y]-b^*E[X] \\
b^* &= \frac{Cov(X,Y)}{Var(X)}
\end{align}
$$
观察 b的性质。b是斜率，分子是X和Y的协方差，分母是X的方差。协方差衡量了X和Y的变动方向。分母X的方差衡量尺度。
![](../images/B4A3781D_image 11.png)

![](../images/B4A3781D_image 12.png)

![](../images/B4A3781D_image 13.png)



## **9. Linear Regression in Practice: Linear Model Plus Noise** 线性回归实践：线性模型叠加噪声

![](../images/B4A3781D_image 16.png)


## **10. Empirical Linear Regression via The Statistical Hammer**
### **Least Squares Estimator (LSE)**

在实践中，$a^*, b^*$ 需要从数据中进行估计。利用 $a^*, b^*$ 的定义，将期望改为样本均值，就可以得到具体的数值。
这就是最小二乘估计量（Least Squares Estimator, LSE）。
目标是通过计算LSE，拟合线性模型 $Y=a+bX+\epsilon$ ，最小化损失函数：
$$
\frac{1}{n}\sum_{i=1}^n(y_i - (a+bx_i))^2
$$
结果为:
$$
\hat a = \bar y - \frac{\overline{xy}-\bar x \cdot\bar y}{\overline{x^2}-\overline{y^2}}\bar x
$$
$$
\hat b= \frac{\overline{xy}-\bar x\cdot\bar y}{\overline{x^2}-\bar x^2}
$$

![](../images/B4A3781D_image 17.png)

![](../images/B4A3781D_image 18.png)
![](../images/B4A3781D_image 19.png)
![](../images/B4A3781D_image 20.png)


### **Residuals** 残差

注意这里的残差是指实际观测点与拟合方程（红线）的距离，所以残差也是一个估计值 $\hat \epsilon_i$。
理论上的噪声是蓝线与红线的差值。
![](../images/B4A3781D_image 21.png)