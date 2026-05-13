---
title: "Lecture 15. Linear models with normal noise 正态噪声的线性模型"
date: 2025-08-13
course: 6.431
cover: "2E29D88C_image.png"
bear_pk: 2E29D88C-A88C-4BFA-B558-53DFA9FBBDA5
---

# **Lecture 15. Linear models with normal noise 正态噪声的线性模型**
#Courses/MITx/6.431


## 1. Lecture 15 overview and slides
In this lecture we focus on an important special case of inference problems in which the random variables of interest are normal and are related through linear relations. We show that the posterior distribution is also normal and examine how we can calculate the posterior mean and variance. We illustrate the methodology through a progression of increasingly complex examples, including the problem of estimating a trajectory on the basis of multiple noisy measurements.

Some of the material in this lecture is covered in Example 8.3 on page 415 and page 421, and on pages 480-482 of the textbook.
![](../images/2E29D88C_image.png)

## 2. Recognizing normal PDFs
![](../images/2E29D88C_image 2.png)

## 3. Exercise: Recognizing normal PDFs

## 4. Normal unknown and additive noise
![](../images/2E29D88C_image 3.png)
![](../images/2E29D88C_image 4.png)

## 5. Exercise: Normal unknown and additive noise
**Exercise: Normal unknown and additive noise**
TBC

## 6. The case of multiple observations
![](../images/2E29D88C_image 5.png)![](../images/2E29D88C_image 6.png)![](../images/2E29D88C_image 7.png)

## 7. Exercise: Multiple observations
## 8. Exercise: Multiple observations, more general model

## 9. The mean squared error
注意这里的方差：
$\sigma_0^2$ 是 $\Theta$ 的方差； $\sigma_i^2$ 是噪声 $W_i$ 的方差。
特别的，当所有方差 $\sigma_i^2$ 都相等时，MAP的均方误差 就等于 $\sigma^2/(n+1)$。这个均方误差不依赖于样本个数，对任意一个观测值 $x_i$，均方误差都相等。
![](../images/2E29D88C_image 8.png)![](../images/2E29D88C_image 9.png)

## 10. Exercise: The mean-squared error
## 11. Exercise: The effect of a stronger signal
## 12. Multiple parameters; trajectory estimation
在有多个未知参数 $\Theta_0, \Theta_1, \Theta_2$ 时，求解MAP的方法还是从基本定义入手：
首先，假设给定了 $\theta_0, \theta_1, \theta_2$, 那么 $X_i \sim N(\theta_0+\theta_1*t_1+\theta_2*t^2, \sigma^2)$
然后，写出 $f_\Theta$ 的先验分布（这里有三个未知参数，意味着有三个关于 $\theta$ 的正态分布概率密度函数。
然后，写出 $f(x|\theta)$ 的分布函数，并且他们之间是独立的。
最后，联立、求导数，再分别令 $\theta_0, \theta_1, \theta_2$ 的偏导等于0，可以得到三个线性方程和三个未知数。
![](../images/2E29D88C_image 10.png)![](../images/2E29D88C_image 11.png)![](../images/2E29D88C_image 12.png)

## 13. Exercise: Multiple observations and unknowns

## 14. Linear normal models
线性正态模型的每一个参数 $\Theta$ 的MAP估计是一个关于观测值X的线性函数： $\widehat \Theta_{MAP,j}: \text{Linear function of }X=(X_1,...,X_n)$
线性正态模型有以下良好的性质：
* **参数MAP估计等于给定X下的条件期望： $\Theta_{MAP,j}=\mathbf E[\Theta_j|X]$；**
* **后验分布 $f_{\Theta|X}(\theta|x)$ 的边缘后验分布概率密度函数 $f_{\Theta_j|X}(\theta_j|x)$ 也是正态分布。**所以对当想求解参数的MAP估计时，有两种方式：一是对联合后验分布求偏导后联立方程；二是对单个边缘分布概率密度函数求导后找极值。两者是等价的。
* **对特定观测值 $x$ 的均方误差，对所有 $x$ 始终相等。**

⠀![](../images/2E29D88C_image 13.png)

## 15. Trajectory estimation illustration
这一节主要讲对抛物线试验的贝叶斯统计推断。
为了更贴合实际，假设了参数 $\Theta_0 \sim N(200, 50^2)$ 代表初始点； $\Theta_1\sim N(50,50^2)$ 代表重力； $\Theta_2 = -9.81$ 代表加速度。
由此，原方程的未知参数从3个减少为两个，因此MAP估计时，对 $\Theta_2$ 的部分就直接删除了；同时，由于方差已知且相等，且与 $\theta$ 无关，所以方差项也移出不考虑。
由于未知参数的均值不再是0，所以需要对原最小化公式变形：从MAP估计的似然函数可知，如果均值发生了变化，等价于 $\theta^2 \rightarrow (\theta-\mu)^2$。
最后，这里还给出了贝叶斯置信区间的概念。由于贝叶斯估计将未知参数 $\Theta$ 视为随机变量，因此MAP估计是可以刻画出一个分布来的。在限定95%置信度下，可以得到关于点估计的概率区间。这是与频率学派不同的一点。
![](../images/2E29D88C_image 14.png)
![](../images/2E29D88C_image 15.png)
![](../images/2E29D88C_image 16.png)
![](../images/2E29D88C_image 17.png)
![](../images/2E29D88C_image 18.png)
![](../images/2E29D88C_image 19.png)
