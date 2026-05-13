---
title: "Lecture 13. Conditional expectation and variance revisited; Sum of a random number of independent r.v.'s 条件期望与条件方差复习；随机数个独立随机变量和"
date: 2025-08-13
course: 6.431
cover: "5FA3404B_image.png"
bear_pk: 5FA3404B-9E4B-4A2E-8D3B-1F49A232E0AD
---

# **Lecture 13. Conditional expectation and variance revisited; Sum of a random number of independent r.v.'s 条件期望与条件方差复习；随机数个独立随机变量和**
#Courses/MITx/6.431

## 1. Lecture 13 overview and slides
This lecture explains that the conditional expectation and variance can be viewed, more abstractly, as random variables, and presents some of their properties, concluding with an application to the calculation of the mean and variance of the sum of a random number of random variables.
textbook: 4.3和4.5章节
![](../images/5FA3404B_image.png)

## 2. Conditional expectation as a r.v.
![](../images/5FA3404B_image 2.png)

## 3. Exercise: Conditional expectation

## 4. The law of iterated expectations
利用全期望公式，可以推导出：
$$
 \mathbf E[\mathbf E[X|Y]] = \mathbf E[X] 
$$
条件期望通常是一个随机变量，是所条件化的随机变量的函数。条件化一般就是 | 右边，所以条件期望就是右边的随机变量的函数。

![](../images/5FA3404B_image 3.png)

## 5. Exercise: Iterated expectations
TBC

## 6. Stick-breaking revisited
这是一道题：
**一根长度为 $l$ 的木棍，从一点将其截断，这一点是随机选择的，且相应概率在整根木棍上均匀分布。截断以后，留下木棍的左边部分。接下来重复以上步骤，问，在截断两次以后，剩下木棍长度的期望是多少？**
记 $Y$ 是第一次截断后剩下的木棍长度， $X$ 为第二次截断以后木棍剩下的长度。因为截断点在剩下的长度 $Y$ 上均匀选择的，所以 $E[X|Y] = Y/2$。类似的，有 $E[Y] = l/2$。因此：
剩下木棍长度的期望为：
$$
 \mathbf E[X] = \mathbf E[E|Y]] = \mathbf E[Y/2] = \mathbf E[Y]/2 = l/4 
$$
![](../images/5FA3404B_image 4.png)

## 7. Exercise: Conditional expectation example
**The random variable $Q$ is uniform on $[0,1]$ . Conditioned on $Q=q$ , the random variable $X$ is Bernoulli with parameter $q$. Then, $E[X|Q]$ is equal to:**
首先翻译这道题目的意思：
1. Q ~ Uni(0,1)
2. 当Q = q时，X服从参数为q的伯努利分布。
3. 求解 $E[X|Q]$, 意味着求解：在已知Q的条件下，X的期望是多少。
由于伯努利分布的期望是参数 $q$，意味着 $E[X|Q = q] = q$。
用抽象表达，即 $E[X|Q] = Q$。


这个类型的题有一个万能解法。
假设：
1. 有个随机变量 $\Theta$（参数），他本身是随机的。
2. 给定 $\Theta = \theta$ 时， $X$ 的条件分布是已知的。

⠀**那么，条件期望就是“参数本身”。**
$$
 \mathbf E[X|\Theta] = 分布的参数(参数是\Theta的函数） 
$$

## 8. Forecast revisions
以预测为例：
在数学上，当你在年初的时候，对未来的销量做预测 $E[X]$。同时，你假定随时间推移，你会获得一些新的信息 $Y = y$ 来修正你的预测:revised forecast。
在新的时间节点一月底：修正预测 revised forecast ： $E[X|Y=y]$
在年初的时间节点，你的修正预测 revised forecast: $E[X|Y]$。
由迭代期望率， $E[\text{revised forecast} ] = E[X] =\text{original forecast}$
意味着在给定上年的销量后，你不应该对预期销量做任何上涨或下跌的预测，而是认为新一年的销量应该等于上一年。
但这只是数学上的结果，实际工作中通常会预测销量会上涨。
![](../images/5FA3404B_image 5.png)

## 9. The conditional variance
总方差（无条件方差） = 条件期望的方差 + 条件方差的期望
![](../images/5FA3404B_image 6.png)
![](../images/5FA3404B_image 7.png)


## 10. Exercise: Conditional variance II

**继续上一节的练习题：**
1. **求解 $Var(X|Q)$**
由 $Var(X|Q = q) = q(1-q)$, 可以知: $Var(X|Q) = Q(1-Q)$

2. **假设 $E[Q^2] = 1/3$，求解： $Var(E[X|Q]), E[Var(X|Q)]$。**
由定义可知， $E[Q] = 1/2, Var(Q) = 1/12$
所以, $Var(E[X|Q]) = Var(Q) = 1/12$
$E[Var(X|Q)] = E[Q(1-Q)] = E(Q) - E[Q^2] = 1/2 - 1/3 = 1/6$
同时，利用全方差公式可以计算出：
$$
 Var(X) = \mathbf E[\text{Var}(X|Q)] + \text{Var}(\mathbf E[X|Q]) = 1/6+1/12=1/4 
$$

## 11. Exercise: Conditional variance definition

## 12. Derivation of the law of total variance

![](../images/5FA3404B_image 8.png)

## 13. A simple example
注意这里在计算 $Var(E[X|Y])$ 时，使用的是方差的定义：
$$
 Var(X) = E[(X-E[X])^2] 
$$
这个期望其实就是“所有可能取值下，偏差平方的加权平均”。
所以上式可以变形为：
$$
 Var(X) = \sum_x\mathbf P(X = x)(x-\mathbf E[X])^2 
$$
![](../images/5FA3404B_image 9.png)


## 14. Section means and variances
![](../images/5FA3404B_image 10.png)![](../images/5FA3404B_image 11.png)

## 15. Exercise: Sections of a class
TBC


## 16. Mean of the sum of a random number of random variables
当N是一个随机变量时，随机数个变量和 $Y = X_1+X_2+…+X_N$ 也是一个随机变量。
这一页的PPT使用了两个方法来计算 $E[Y]$。
* 全期望公式；
* 迭代期望定律

⠀最后的结果都是:
$$
 \mathbf E[Y] = \mathbf E[N]·\mathbf E[X] 
$$
![](../images/5FA3404B_image 12.png)


## 17. Variance of the sum of a random number of random variables
![](../images/5FA3404B_image 13.png)

## 18. Exercise: Second generation offspring

**Every person has a random number of children, drawn from a common distribution with mean 3 and variance 2. The numbers of children of each person are independent. Let**  $M$ **be the number of grandchildren of a certain person. Then:**
求解： $E[M], \ Var[M]$
解答：
这也是一个**两层嵌套的随机变量问题**。与Lecture中的例题一致。
假设每个人的孩子数量为 $N$, 同时，孩子的孩子数量为 $X$。即， $X_i$ 代表第i个孩子的孩子数量。
接下来就是套公式: $M = X_1+X_2+…+X_N$。
根据题意，有: $E[N] = E[X] = 3, Var(N) = Var(X)=2$。
$E[M] = E[N]·E[X] = 3*3 = 9$
$Var[M] = E[N]Var(X) + (E[X])^2 Var(N) = 3*2+9*2 = 24$
