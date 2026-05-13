---
title: "Lecture 12. Sums of independent r.v.'s; Covariance and correlation 独立随机变量和，协方差与相关性"
date: 2025-08-13
course: 6.431
cover: "EC826964_image.png"
bear_pk: EC826964-2595-4EA2-B756-CB9785ACBF91
---

# **Lecture 12. Sums of independent r.v.'s; Covariance and correlation 独立随机变量和，协方差与相关性**
#Courses/MITx/6.431

## 1. Lecture 12 overview and slides
This lecture covers two different topics:
1 the calculation of the PMF or PDF of the sum of independent random variables;
2 the concepts of covariance and correlation, and their main properties.

这个lecture主要包含两个主题：
* 计算独立随机变量和的PMF或PDF;
* 协方差、相关性的概念与他们的主要性质。

## 2. The sum of independent discrete random variables 独立随机变量和
![](../images/EC826964_image.png)
![](../images/EC826964_image 2.png)
shift的距离就是要求的Z的数值

## 3. Exercise: Discrete convolution
## 4. The sum of independent continuous r.v.'s
$$ 
由\ f_{X+b}(x) = f_X(x-b), \\ 有\ f_{Z|X}(z|x) = f_Y(z-x)
$$
![](../images/EC826964_image 3.png)
## 5. Exercise: Continuous convolution
TBC

## 6. The sum of independent normal r.v.'s
![](../images/EC826964_image 4.png)

## 7. Exercise: Sum of normals

## 8. Covariance
X和Y独立， cov = 0
反过来不成立，若cov = 0, X和Y不一定独立
![](../images/EC826964_image 5.png)

## 9. Exercise: Covariance calculation
Suppose that $X,Y$ , and $Z$ are independent random variables with unit variance. Furthermore,  $\mathbf E[X]=0$ and $\mathbf E[Y]=\mathbf E[Z] = 2$ . Then, 求解 $\text{Co}v(XY, XZ) = ?$

首先按照协方差公式进行展开，这里有两种展开方式：
$$
Cov(X, Y) = E\left[(X-E[X])·(Y-E[Y])\right]
$$ 
 一般常用下面的形式：
$$ 
\\ Cov(X, Y) = E(XY) - E(X)E(Y) 
$$
得到:
$$
\begin{aligned} 
\text{Co}v(XY, XZ) &= E[XY·XZ] = E[X^2YZ] = E[X^2]E(Y)E(Z) \\
&=(Var(X)+(E[X])^2)·E(Y)E(Z) \\
&= 4 
\end{aligned}
$$
这里有两个小点不太熟悉：
1 $E[XY·XZ] = E[X^2YZ]$ 可以对随机变量的乘积进行乘法规则计算，因为E是一个线性算子；
2 $X,Y,Z$ 相互独立，可以推导出任意可测函数 $g,h,k$, $g(x), h(y), k(z)$ 也是相互独立的。


## 10. Covariance properties
![](../images/EC826964_image 6.png)


## 12. The variance of the sum of r.v.'s
![](../images/EC826964_image 7.png)
![](../images/EC826964_image 8.png)


## 13. Exercise: The variance of a sum

## 14. The correlation coefficient
这里有一个知识点是 $\rho$ 的数学运算法则：
![](../images/EC826964_image 9.png)

## 15. Exercise: Correlation coefficient
**It is known that for a standard normal random variable $X$ , we have $E[X^3] = 0, E[X^4] = 3, E[X^5] =0, E[X^6] = 15$. Find the correlation coefficient between $X$  and $X^3$ . Enter your answer as a number.**
由定义：
$$
\begin{gather}
 \rho(X, X^3) = \frac{Cov(X, X^3)}{\sigma_X\sigma_{X^3}}\\ Cov(X, X^3) = E[X*X^3] - E[X]E[X^3] = E[X^4] - E[X]E[X^3]\\ 由X是标准正态分布，由E[X]=0, Var[X] = 1, E[X^2] = 1\\ 所以：Cov(X, X^3) = 3-0 = 3\\ 接下来计算方差： Var(X^3) = E[(X^3)^2] - (E[X^3])^2 \\= E[X^6]-0 = 15\\ 所以：\sigma_{X^3} = \sqrt 15 \\ 所以有，\rho(X, X^3) = \frac{3}{\sqrt15}
\end{gather}
 $$
## 16. Derivation of key properties of the correlation coefficient
![](../images/EC826964_image 10.png)

## 17. Interpreting the correlation coefficient
这一节主要介绍：相关不一定具有因果关系。
举例用一个隐变量Z来描述，X和Z相关、Y和Z相关，但X和Y没有关系。通过计算相关系数，可以得到 $\rho(X,Y)$ = 1/2。
这说明即使两个随机变量相关系数不为零，也不能说明他们存在因果关系。
另外有一个小trick： 如果一个随机变量X的期望为0，那么X^2的期望就等于方差。 $E[X^2] = Var(X) + (E[X])^2 = Var(X)$
![](../images/EC826964_image 11.png)

## 18. Exercise: Correlation properties

## 19. Correlations matter
![](../images/EC826964_image 12.png)