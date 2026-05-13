---
title: "Lecture 3. Parametric Statistic Models 参数统计模型"
date: 2025-08-09
course: 18.6501x
cover: "FC689F6B_image.png"
bear_pk: FC689F6B-EBDC-44D7-B04F-8E2D6B994B02
---

# **Lecture 3. Parametric Statistic Models 参数统计模型**
#Courses/MITx/18.6501x
## 1. Motivation 动机

## 2. Objectives
### Parametric Statistical Models
At the end of this lecture, you will be able to do the following:
* Construct a **statistical model** .
* Give several examples of statistical models involving commonly used distributions (e.g. Gaussian, Poisson)
* Distinguish between **parametric** and **non-parametric** statistical models.
* Determine whether or not a parameter in a statistical model is **identified** .

⠀The Unit 2 slides below, which are for the next **5 lectures** , are also available in the resource tab at the top of this course site.

## 3. The goals of statistics 统计的目标
### Estimation, confidence intervals, and hypothesis testing
![](../images/FC689F6B_image.png)
统计推断的三个主要内容（Trinity of Statistical Inference）：
* Estimation: 估计
* Confidence Intervals: 置信区间
* Hypothesis Testing: 假设检验

⠀
## 4. Statistical modelling 统计建模
### An example of a statistical model
![](../images/FC689F6B_image 2.png)

## 5. Statistical model 统计模型
### Statistical model: definition 定义
![](../images/FC689F6B_image 3.png)
statistical mode: is associated to that statistical experiment is a pair:
$$ 
(E, (\mathbb{P_\theta})_{\theta \in \Theta}) 
$$
* $E$: 可观测样本空间（measurable sample space）
* $(\mathbb{P_\theta})_{\theta \in \Theta}$ : 对E的概率测量族( is a family of probaility measures on $E$）;
* $\Theta$：参数集合（大写的theta） is any set, called parameter set

⠀**练习题：A Non-Example of a Statistical Model**
![](../images/FC689F6B_image 4.png)
选A。
一个合法的统计模型，必须包括一个可观测的样本空间，并且这个样本空间是固定的。
选项A的样本空间 $[0, a]$ 依赖未知参数 $a$，所以不是一个合法的统计模型定义。

## 6. Types of Statistical Models 统计模型的类型
### Parametric, nonparametric, and semiparametric models
![](../images/FC689F6B_image 5.png)
nuisance parameter: 冗余参数
统计模型主要有三类：
* 参数模型（parametric model)
* 非参数模型（nonparametric model)
* 半参数模型（semiparametric model)

⠀
## 7. Examples of Parametric Models 参数模型的例子
### Examples of parametric and nonparametric models
![](../images/FC689F6B_image 6.png)
### 练习题：Statistical Model for a Censored Exponential
![](../images/FC689F6B_image 7.png)
cencored version： 删失版本
这道题的解题思路是：
![](../images/FC689F6B_image 8.png)
Y服从伯努利分布，所以Y的参数空间是p（即 成功的概率）
当X>5时，Y取值为1，所以p = P(X>5)，可以由指数分布的定义得到：
$$ 
(P >= a) = e^{- \lambda a} 
$$
也可以由定义计算：
$$
 P(X>5） = 1-P（X<=5) = 1-e^{-\lambda x} = 1-(1-e^{-\lambda x}) 
$$

## 8. Mixtures of Gaussians 高斯混合
![](../images/FC689F6B_image 9.png)
![](../images/FC689F6B_image 10.png)
![](../images/FC689F6B_image 11.png)
![](../images/FC689F6B_image 12.png)
![](../images/FC689F6B_image 13.png)
![](../images/FC689F6B_image 14.png)
第二个分布的sigma^2变大了
![](../images/FC689F6B_image 15.png)

## 9. Another representation of mixtures of Gaussians 高斯混合的另一种表征
![](../images/FC689F6B_image 16.png)
注意这里的Z取值只有 ${0,1}$,意味着 $X$ 的取值也是 ${X_1, X_2}$。而不是取概率的意思。
这样做的好处是，减轻了计算复杂度。当编程计算混合高斯分布时，只需要随机从Ber里取 $Z$，然后将 $Z$ 的取值对应具体的某一个高斯分布即可。
### 练习题：Mean and Variance of a Mixture
![](../images/FC689F6B_image 17.png)
解答：
第一问求期望比较简单，带入pi就可以计算。
关键是第二问，求 $\text{Var} (X)$。
这里需要用到求方差的定义公式进行展开：
$$ 
Var(X) = \mathbb{E}[X^2] - \mathbb{E}[X]^2 
$$
利用全期望公式和全方差公式：
$$ 
\mathbb{E}[X^2]=\mathbb{E}[\mathbb{E}[X^2 | Z]] 
$$
当 $Z = 1$ 时, $X = X_1$：
$$ 
\mathbb{E}[X^2 | Z] = \mathbb{E}[X_1^2] = Var(X_1) + \mathbb{E}[X_1]^2= 0+1 = 1 
$$
当 $Z = 0$ 时， $X = X_2$:
$$ 
\mathbb{E}[X^2 | Z] = \mathbb{E}[X_2^2] = Var(X_2) + \mathbb{E}[X_2]^2= 1+1 = 2
 $$
因此：
$$ 
\mathbb{E}[X^2] = \pi*\mathbb{E}[X_1^2] + (1-\pi)*\mathbb{E}[X_2^2] = 7/4
 $$
所以，计算方差 $Var(X)$:
$$ 
Var(X) = \mathbb{E}[X^2] - \mathbb{E}[X]^2 = 7/4 - 9/16 = 19/16 
$$
另一个解题方式是利用条件方差公式，直接把deepseek的解答复制过来：
![](../images/FC689F6B_image 18.png)
官方给出的标准答案：
![](../images/FC689F6B_image 19.png)
### 练习题：Moment Generating Function of a Mixture
![](../images/FC689F6B_image 20.png)
解答：
两个解法。标准答案给的解法非常简略：
$$ 
\mathbb{E}[e^{Xt}] = \pi*\mathbb{E}[e^{X_1t}] + (1-\pi)*\mathbb{E}[e^{X_2t}] 
$$
然后直接带入正态分布随机变量的矩母函数公式：
$$ 
M_X[t] = e^{ut + \frac{1}{2}\sigma^2t^2} 
$$

## 10. Mixtures of Gaussians model 混合高斯模型
![](../images/FC689F6B_image 21.png)

## 11. Examples of nonparametric models 非参数模型的样例
![](../images/FC689F6B_image 22.png)
![](../images/FC689F6B_image 23.png)
非参数模型的意思是pdf/cdf 无法用一个特定的模型和参数来进行表示。
实际上，所有符合概率分布的函数（非负性、归一性）都有可能成为一个非参数模型。如PPT中展示的unimodal分布。这个时候，概率分布和参数都都是其自身。
特定模型（例如高斯分布）仅仅是unimodal的一个子集。
标准定义：
**parametric model:** A statistical model$(E, \{P_{\theta}\}_{\theta\in\Theta})$ is **parametric** if all parameters $\theta \in \Theta$ can be specified by a **finite** number of unknowns.
Equivalently, this means that $\Theta$ is a subset of $\mathbb R^m$. In particular, if $\Theta \subset \mathbb R^m$, then $P_\theta$ is uniquely specified by the  $m$ entries of the vector $\theta$.这意味着，参数空间由有限维向量指定。
练习题：

## 12. Identifiability 可识别性
