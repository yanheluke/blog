---
title: "Lecture 12. The Wald Test and Likelihood Ratio Test -Wald检验与似然比检验"
date: 2025-08-10
course: 18.6501x
cover: "EABC49E4_image.png"
bear_pk: EABC49E4-1DBA-4442-8EA7-AAC5B6AF4609
---

# Lecture 12. The Wald Test and Likelihood Ratio Test -Wald检验与似然比检验
#Courses/MITx/18.6501x

## 1. The Wald Test
### Objectives
At the end of this lecture, you will be able to do the following:
* Construct one-sample and two-sample Wald tests with specified asymptotic level
* Compute the asymptotic p-value of a Wald test
* Construct the Wald test from an asymptotically normal maximum likelihood estimator
* Perform the **likelihood ratio test** for a family of hypothesis testing questions.

Wald检验只能保证在渐进等级上应用。如果样本非常小，不满足CLT，另一个可选择的检验方式是T-test。
![](../images/EABC49E4_image.png)
## 2. The Wald Test
构造Wald检验的关键步骤是构造估计量 $\hat \theta$，使之具有渐进正态性。
$$
 \frac{\hat \theta - \theta}{\sqrt{\widehat{var}(\hat \theta)}} \xrightarrow[n\rightarrow\infty]{(d)}\mathcal N(0,1) 
$$
其中， $\widehat{var}(\hat \theta)$ 是 $\hat \theta$ 的方差的估计量。
以伯努利分布为例, $var(\hat p) = p(1-p)/n$。 但这不是一个估计量，因为他依赖未知参数p。
所以我们需要估计他。估计的方式是加上\hat在他的上面： $\widehat{var}(\hat p) = \hat p(1-\hat p)/n$。
所以，我们重新写出上面的渐进正态性表达：
$$
 \frac{\hat p-p}{\sqrt{\widehat{var}(\hat p)}} = \sqrt{n}*\frac{\hat p-p}{\hat p(1-\hat p)} \xrightarrow[n\rightarrow\infty]{(d)}\mathcal N(0,1) 
$$
**在零假设下，当真值等于假设值时，W收敛于N(0,1)；但当真值不等于 $\theta_0$ 时，W的渐进分布就会偏移，不再是标准正态，而是“中心化项+偏移项”。**
![](../images/EABC49E4_image 2.png)
![](../images/EABC49E4_image 3.png)
![](../images/EABC49E4_image 4.png)

## 3. Asymptotic level of the Wald test
在推导Wald检验的渐进性时，需要注意：需要在 $\mathbf P_{\theta_0} 和W$ 中保持同一个 $\theta_0$。（注意在power function定义的时候求的是 $\mathbf P_\theta$，而不是 $\mathbf P_{\theta_0}$。
**双侧检验：**
在双侧检验时这个条件很好满足：我们假设，在零假设的条件下，最糟糕的情况概率就是 $\theta = \theta_0$。所以我们可以直接将 $\mathbf P_\theta$ 替换为 $\mathbf P_{\theta_0}$。
这时候直接利用定义求解.因为 $W=\frac{\hat \theta - \theta}{\sqrt{\widehat{var}(\hat \theta)}} \xrightarrow[n\rightarrow\infty]{(d)}\mathcal N(0,1)$，我们令右边的形式为Z，可以直接将W替换为Z，得到：
$$
 \lim_{n\rightarrow\infty}\mathbf P_{\theta_0}[|W| > q_{\alpha/2}] = \lim_{n\rightarrow\infty}\mathbf P_{\theta_0}[|Z| > q_{\alpha/2}] = \alpha 
$$
**单侧检验：**
单侧检验情况更复杂一些。我们希望控制犯Type 1错误的概率，也即是所有 $\theta \leq \theta_0$。
按照定义，可以进行以下变形：
$$
 \lim_{n\rightarrow\infty}\mathbf P_{\theta}[W > q_{\alpha}] = \lim_{n\rightarrow\infty}\mathbf P_{\theta}[\frac{\hat \theta - \theta_0}{\sqrt{\widehat{var}(\hat\theta)}}>q_\alpha] 
$$
注意到外层的概率是 $\theta$, 内层的W的表达式是 $\theta_0$。所以我们需要做一些变形将两者统一：
$$
 \frac{\hat \theta - \theta_0}{\sqrt{\widehat{var}(\hat\theta)}} = \frac{\hat \theta - \theta}{\sqrt{\widehat{var}(\hat\theta)}} +\frac{\theta - \theta_0}{\sqrt{\widehat{var}(\hat\theta)}} 
$$
当 $\theta \leq \theta_0$ 时，右边第二项<0。所以：
$$
 \frac{\hat \theta - \theta_0}{\sqrt{\widehat{var}(\hat\theta)}} \leq \frac{\hat \theta - \theta}{\sqrt{\widehat{var}(\hat\theta)}} 
$$
后续的步骤就是带入表达式，与双侧检验的做法一致。
具体的推导步骤见：
![](../images/EABC49E4_image 5.png)
![](../images/EABC49E4_image 6.png)
![](../images/EABC49E4_image 7.png)
这两页PPT都是推导出了一个极限上界，即：
单侧检验时：
对所有 $\theta < \theta_0$, 极限不超过 $\alpha$。但这并不意味着在给定真值 $\theta$时，这个极限就等于 $\alpha$。具体的极限是多少，仍需带入W的具体公式进行计算。
* 在 $\theta < \theta_0$ 时，样本均值收敛到 $\theta$，分子会变负，标准化后会趋向负无穷，拒绝概率 → 0。
* 在 $\theta = \theta_0$ 时，标准化后的分布是 $\mathcal N(0,1)$，所以拒绝域概率就是 $\alpha$。
* 在 $\theta > \theta_0$ 时，分子趋向正的，统计量会趋向正无穷，拒绝域的概率 → 1。

⠀![](../images/EABC49E4_image 8.png)
双侧检验时：
![](../images/EABC49E4_image 9.png)
### 练习题：Asymptotic level of the Wald test
![](../images/EABC49E4_image 10.png)第一问：
第一问有两种解法。最简单的解法是假设n趋近无穷时, $\bar X_n 或 p$ 趋近于真值1/2。然后带入W统计量，有：
$$
 W =\sqrt n *\frac{\hat p - p}{\sqrt{\hat p(1-\hat p)}} = \sqrt n*\frac{0.2-0.5}{\sqrt{0.2*0.8}} = -\sqrt n * C ,\ C是一个正整数。 
$$
随n趋近正无穷，W趋近负无穷，永远小于 $q_\alpha$，所以概率为0。
标准的做法：
根据CLT和slutsky定理，首先定义 $Y:= \sqrt n*\frac{\bar X_n-0.2}{\sqrt{\bar X_n(1-\bar X_n)}} \rightarrow N(0,1)$

然后写出W统计量，将其变形为 $W = Y(中心化项) + 局部偏移项$。
$$
 \begin{aligned} W &= \sqrt n*\frac{\bar X_n-0.5}{\sqrt{\bar X_n(1-\bar X_n)}} \\ &= \sqrt n*\frac{\bar X_n-0.2}{\sqrt{\bar X_n(1-\bar X_n)}} + \sqrt n*\frac{0.2-0.5}{\sqrt{\bar X_n(1-\bar X_n)}}\\ &= Y + \text{determinstic shift} \end{aligned} 
$$
Y → N(0,1)，第二项趋近负无穷，所以W > q/a的概率为0。

第二问：
第二问的解法与第一问基本一致。根据题目含义， $p$ 的真值为 $0.5 - \lambda/\sqrt n$。所以: $P_{0.5 - \lambda/\sqrt n}[\psi = 1]$ 的含义是：
在真参数值为 $0.5 - \lambda/\sqrt n$ 时，检验拒绝H0的概率。
这里的 $0.5 - \lambda/\sqrt n$ 是局部替代真值（来自局部替代理论）。
![](../images/EABC49E4_image 11.png)局部替代理论是想回答：当“几乎零差异”的时候，检验对这类情况有多敏感？
在局部替代下，W的极限分布不再是 $\mathcal N(0,1)$，而是：
$$
 Z + \text{Shift}(\lambda) 
$$
和第一问类似，将第二问的W统计量进行变形：
$$
 \begin{aligned} Y &:= \sqrt n*\frac{\bar X_n-(0.5-\frac{\lambda}{\sqrt n})}{\sqrt{\bar X_n(1-\bar X_n)}} \\
W &= \sqrt n*\frac{\bar X_n-0.5}{\sqrt{\bar X_n(1-\bar X_n)}} \\ &= \sqrt n*\frac{\bar X_n-(0.5-\frac{\lambda}{\sqrt n})}{\sqrt{\bar X_n(1-\bar X_n)}} + \sqrt n*\frac{(0.5-\frac{\lambda}{\sqrt n})-0.5}{\sqrt{\bar X_n(1-\bar X_n)}} \\ &= Y + \frac{-{\lambda}}{\sqrt{\bar X_n(1-\bar X_n)}} \end{aligned} 
$$
Y → N(0,1)，第二项 $\sqrt{\bar X_n(1-\bar X_n)} \rightarrow 0.5$（根据局部替代理论也能看出来，随n增大， 扰动项趋近0，那么真值就趋近于0.5）.
所以：
$$
 \lim_{n\rightarrow\infty}\mathbf P_{0.5-\frac{\lambda}{\sqrt n}}[\psi = 1] = \mathbf P[Z > 1.645 + 2\lambda] 
$$

## 4. P-value for the Wald test
这一节主要讲Wald test的P值计算。
* 根据题目给出的样本数据和零假设，首先计算出 $W^{obs}$。
* 然后，对应的P-value，本质上就是 $W$比 $W^{obs}$ 更大的概率。但实践中 $W$ 很难计算。
* 在渐进正态性下，可以将 $W$ 近似看做 $Z$，这样就可以使用标准正态分布的分位数来求解对应的概率了。

⠀注意，在计算实际的p-value时，原分布可以是离散分布（例如伯努利）；这时候计算的 $P(|W| > |W^{obs}|)$ 实际上就是计算 $P(W取值不等于观测值）$
在计算渐进p-value时，就是将W看成Z，只能是连续分布了。

![](../images/EABC49E4_image 12.png)
![](../images/EABC49E4_image 13.png)

## 5. Two-sample Wald test 双样本Wald检验
![](../images/EABC49E4_image 14.png)![](../images/EABC49E4_image 15.png)![](../images/EABC49E4_image 16.png)![](../images/EABC49E4_image 17.png)

## 6. Other examples
![](../images/EABC49E4_image 18.png)
![](../images/EABC49E4_image 19.png)
### 练习题
**Wald Test and the MLE**
![](../images/EABC49E4_image 20.png)TBC，这道题挺复杂的。


## 7. Who was Abraham Wald (optional)
![](../images/EABC49E4_image 21.png) 

## 8. Likelihood Ratio Test: Basic Form
**Basic Form of the Likelihood Ratio Test**
Let $X_1,…,X_n \sim^{iid}\mathbf P_{\theta^*}$ , and consider the associated statistical model $(E,\{\mathbf P_\theta\}*{\theta\in\mathbb R^d} )$. Suppose that  $\mathbf P*\theta$ is a discrete probability distribution with pmf given by $p_\theta$ .
In its most basic form, the **likelihood ratio test** can be used to decide between two hypotheses of the following form:
$$
 H_0: \theta^* = \theta_0\\ H_1: \theta^* = \theta_1 
$$
Recall the likelihood function:
$$
 L_n : \mathbb R^n \times \mathbb R^d \rightarrow \mathbb R\\ (x_1,...,x_n;\theta) \mapsto \prod_{i=1}^np_\theta(x_i) 
$$
The **likelihood ratio test** in this set-up is of the form
$$
 \psi_C = \mathbf 1\left(\frac{L_n(x_1, ..., x_n;\theta_1)}{L_n(x_1, ..., x_n;\theta_0)}>C\right) 
$$
where $C$ is a threshold to be specified.

简单来说，极大似然估计就是出现概率连乘。
例如丢一枚不均匀硬币，假设 $H_0:p^* = 0.25; H_1:p^* = 0.75$。如果只丢一次， $X_1 = 1$。
那么这个时候，两个假设下的似然函数分别是：
$$
 L_1(1;0.25) = 0.25; L_1(1;0.75) = 0.75 
$$
计算似然比等于 $3 > C=1$。所以拒绝原假设。
如果丢16次硬币，6次为HEAD, 10次为TAIL，那么两个假设下的似然函数分别是：
$$
\begin{align}
 L_{16}(\mathbf X;0.25)=(1/4)^6(3/4)^{10}\\ L_{16}(\mathbf X;0.75)=(1/4)^{10}(3/4)^6 
\end{align}
$$
这时候不用直接计算两个似然函数，而是直接比较其比值是否大于C。就能知道是否拒绝原假设了。


## 9. Likelihood Ratio Test（这段没太听懂）
Wilks’s Theorem:
渐进服从自由度为d的卡方分布
d = 备择假设自由参数个数 - 原假设自由参数个数
![](../images/EABC49E4_image 22.png)![](../images/EABC49E4_image 23.png)
**Concept Check: The Constrained Maximum Likelihood Estimator**
![](../images/EABC49E4_image 24.png)