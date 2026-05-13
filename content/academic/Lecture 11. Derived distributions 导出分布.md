---
title: "Lecture 11. Derived distributions 导出分布"
date: 2025-08-13
course: 6.431
cover: "1CE2D164_image.png"
bear_pk: 1CE2D164-3079-4648-82FD-6971C559DCC7
---

# **Lecture 11. Derived distributions 导出分布**
#Courses/MITx/6.431

## 1. Lecture 11 overview and slides 讲义概览
This lecture develops a method for finding the distribution (PMF or PDF) of a function of one or more random variables with known distribution.
![](../images/1CE2D164_image.png)

## 2. The PMF of a function of a discrete r.v. 离散随机变量的函数的PMF

![](../images/1CE2D164_image 2.png)
![](../images/1CE2D164_image 3.png)

## 3. Exercise: Linear functions of discrete r.v.'s

## 4. A linear function of a continuous r.v. 连续随机变量的线性函数
与离散随机变量不同的是，连续随机变量的线性函数的PDF，需要对X前的系数a做放缩。
![](../images/1CE2D164_image 4.png)
![](../images/1CE2D164_image 5.png)

## 5. Exercise: Linear functions of continuous r.v.'s
## 6. A linear function of a normal r.v. 正态随机变量的线性函数
正态分布的线性变换仍然为正态分布。
![](../images/1CE2D164_image 6.png)
## 7. The PDF of a general function 一般性函数的PDF
接下来是对于一个一般函数g(x)，求解PDF的步骤。
![](../images/1CE2D164_image 7.png)
![](../images/1CE2D164_image 8.png)
![](../images/1CE2D164_image 9.png)

## 8. Exercise: PDF of a general function
![](../images/1CE2D164_image 10.png)
![](../images/1CE2D164_image 11.png)
主要是在求解Y的PDF的时候，需要先求CDF。
但从这道题里，不用显性的写出CDF，只要能转化为 $F_X(g^{-1}(x))$ 的形式，接下来就用链式法则，直接套用公式: $f_X(\sqrt y)$ 对y求导数。


## 9. The monotonic case 单调案例
当g(x)是单调函数的时候，可以不用写出F_Y的CDF，只需要找到反函数h(y)，然后套用下列公式：
$$
 f_Y(y) = f_X(h(y))\left|\frac{dh}{dy}(y)\right| 
$$
![](../images/1CE2D164_image 12.png)
![](../images/1CE2D164_image 13.png)

## 10. Exercise: Using the formula for the monotonic case

## 11. The intuition for the monotonic case 单调案例的直觉性解释
当x变动 $\delta_1$ 个单位时，y 变动 $\delta_2$ 个单位。我们现在将两者联系起来，可以得知：
$$
\begin{aligned}
\delta_2 \approx \delta_1 * \frac{g}{x}(x) \\ \delta_1 \approx \delta_2 * \frac{h}{y}(y)
\end{aligned}
$$
由于X和Y的变化事件的概率是相等的，即：
$$
 \mathbf P(y \le Y \le y + \delta_2) = \mathbf P(x \le X \le x+\delta_1) 
$$
所以有：
$$
\begin{gather}
f_Y(y)*\delta_2 \approx \mathbf P(y \le Y \le y + \delta_2) = \mathbf P(x \le X \le x+\delta_1) \approx f_X(x)*\delta_1 \\
 有\\ 
f_Y(y)*\delta_2 \approx f_X(x) * \delta_2 * \frac{h}{y}(y)\\ 所以有：\\ f_Y(y) = f_X(x)\frac{h}{y}(y)
\end{gather}
$$
![](../images/1CE2D164_image 14.png)


## 12. A nonmonotonic example 非单调案例
![](../images/1CE2D164_image 15.png)

## 13. Exercise: Nonmonotonic functions

## 14. A function of multiple r.v.'s 多元随机变量的函数
![](../images/1CE2D164_image 16.png)


## 15. Exercise: A function of multiple r.v.'s
![](../images/1CE2D164_image 17.png)
![](../images/1CE2D164_image 18.png)
这道题的标准解法需要求联合概率密度函数的积分，但根据题目的意思，可以有渐变求法：
P(Z ≤ z) = P(sqrt(X^2 + Y^2) ≤ z)
x^2 + y^2 ≤ z^2表示以z为半径的圆,， 又因为(X, Y)均匀分布在单位圆内，所以这里求P(Z ≤ z)等于是求z为半径的圆与单位圆的面积比值，即 z^2*pi / pi = z^2
然后求导即可。
