---
title: "Lecture 19. The Central Limit Theorem (CLT) 中心极限定理"
date: 2025-08-13
course: 6.431
cover: "D9F12488_image.png"
bear_pk: D9F12488-F059-4267-A649-139A2CD8ABBF
---

# **Lecture 19. The Central Limit Theorem (CLT) 中心极限定理**
#Courses/MITx/6.431

## 1. Lecture 19 overview and slides 概览
This lecture introduces, discusses, and applies the celebrated Central Limit Theorem.
![](../images/D9F12488_image.png)
Printable transcript available ~[here](https://courses.edx.org/asset-v1:MITx+6.431x+2T2025+type@asset+block/transcripts_L19-Overview.pdf)~.
Lecture slides: ~[\[clean\]](https://courses.edx.org/asset-v1:MITx+6.431x+2T2025+type@asset+block/lectureslides_L19-clean-slides.pdf)~ ~[\[annotated\]](https://courses.edx.org/asset-v1:MITx+6.431x+2T2025+type@asset+block/lectureslides_L19-annotated-slides.pdf)~
The material in this lecture is covered in ~[Section 5.4](https://courses.edx.org/courses/course-v1:MITx+6.431x+2T2025/pdfbook/0/chapter/1/41)~ of the text.
**Note:** In all of the numerical examples in this lecture, one can of course bypass the normal table and use an online tool, such as the one found ~[here](http://stattrek.com/online-calculator/normal.aspx)~ or ~[here](http://onlinestatbook.com/2/calculators/normal_dist.html)~. Note also that such tools also allow you to go backwards, from the value of $\Phi(x)$ to the value of $x$ .

## 2. The Central Limit Theorem 中心极限定理
**iid随机变量和的不同放缩模式**
* $S_n = X_1+\dots+X_n$：方差为 $n\sigma^2$，随n趋近于无穷大， 方差也无穷大；
* $M_n = \frac{S_n}{n} = \frac{X_1+\dots+X_n}{n}$：方差为 $\frac{\sigma^2}{n}$，随n趋近于无穷大， 方差趋近于0，整个分布退化为一个单点分布；
* $\frac{S_n}{\sqrt n} = \frac{X_1+\dots+X_n}{\sqrt n}$：方差为 $\sigma^2$，这个分布比较好，既不趋近于无穷大， 也不退化。

![](../images/D9F12488_image 2.png)
在这里，我们重新构建一个新的随机变量： $Z_n = \frac{S_n-n\mu}{\sqrt n\sigma}$。这个新构建的随机变量有良好的性质：
期望为0，方差为1。
由此，给出中心极限定理：
对任意 $z$， $\lim_{n\rightarrow\infty}\mathbf P(Z_n \le z) = \mathbf P(Z \le z)$
![](../images/D9F12488_image 3.png)

## 3. Exercise: CLT
简单的标准正态化题目

## 4. Discussion of the CLT 对CLT的讨论
$$
 Z_n = \frac{S_n-n\mu}{\sqrt n\sigma} = \frac{M_n-\mu}{\sigma/\sqrt n} 
$$
![](../images/D9F12488_image 4.png)
**CLT的理论性质**
* $Z_n$ 的CDF收敛于正态CDF；
* $Z_n$ 的PDF或PMF也收敛（但需要更多的假设）；
* $X_i$ 不需要保证同分布；
* $X_i$ 弱相关时，CLT也成立。例如X_1和X_2相邻相关，但和X_10000不相关，这时候CLT也是成立的。
* 完整的数学证明比较复杂。
![](../images/D9F12488_image 5.png)

**CLT的实践应用**
* 可以将 $Z_n$ 看做标准正态分布，那么样本和 $S_n \sim \mathcal N(n\mu, n\sigma^2)$
* 当 $X_i$ 的分布更接近正态分布时（例如具有对称性，并且只有一个峰值(unimodel)），那么n在小样本下CLT也成立。
![](../images/D9F12488_image 6.png)

## 5. Exercise: CLT applicability

## 6. Illustration of the CLT CLT图例
这一节主要展示不同的X分布下，随机变量和随n增大而逐渐趋近于正态分布。
![](../images/D9F12488_image 7.png)
![](../images/D9F12488_image 8.png)

## 7. CLT examples CLT的例子
本节介绍如何利用CLT解决问题。
第一类问题是： $P(S_n \le a) \approx b$。 在这类问题里，有n,a,b三个参数，已知其中两个，可以求第三个。
![](../images/D9F12488_image 9.png)
![](../images/D9F12488_image 10.png)
![](../images/D9F12488_image 11.png)
第四个案例有一些变形：这里我们不再直接求解n,a,b。问题变成：
当container的重量超过210的时候，停止装卸。**求装载包裹数量 N>100的概率。**
这里的变形在于：
装载包裹数量N>100的概率等同于前一百个包裹的重量都还没有超过210。所以概率变形为: $P(N>100) = P(\sum_{i=1}^{100}X_i ≤ 210)$。后面的步骤就一样了。
![](../images/D9F12488_image 12.png)

## 8. Exercise: CLT practice
第七节案例的翻版

## 9. Normal approximation to the binomial 对二项分布的正态近似
对二项分布来说，如果我们计算S_n ≤21的概率，按照二项分布的精确计算答案是0.8785。
现在我们使用CLT进行正态近似。由于S_n是一个二项分布，可以直接利用二项分布的期望与方差来进行标准正态化（对比常规的S_n，期望是nu,方差时n*sigma^2）。
以≤21算，对应的概率是0.8413，会低估概率；以≤22算，对应概率是0.9082，会高估概率。
造成这个区别的原因是，对离散分布来说，取21和22来计算结果是一样的，但对连续分布来说会多出21到22的这一段概率。这一段概率是否该被计算？答案是只有一部分需要被计算，因此可以取中点，即计算≤21.5的概率。这时候算出来的概率为0.8790，就非常接近二项分布的精确概率了。

![](../images/D9F12488_image 13.png)
![](../images/D9F12488_image 14.png)

### 二项分布的De Moivre-Laplace近似
如果对离散变量计算一个精确值的概率：例如S_n = 19，那么我们在做正态近似的时候，采用1/2 correlation：计算 18.5 ≤ S_n ≤ 19.5的概率。这个结果与二项分布精确计算的概率十分接近。
![](../images/D9F12488_image 15.png)


## 10. Exercise: CLT for the binomial
## 11. Polling revisited 重访选举问题
重新看选举问题，上一节里我们是用切比雪夫不等式和WLLN来求解的一个误差上界，但不够精确。
现在用正态近似来重新求解这道题：
首先是将原概率标准正态化，转化为一个正态分布求概率问题。
$P(|M_n-p| ≥ 0.01) = P(|Z_n| ≥ \frac{0.01\sqrt n}{\sigma}) \approx P(|Z| ≥ \frac{0.01\sqrt n}{\sigma})$
由于右边带有 $\sigma = \sqrt{p(1-p}$，无法精确求解，所以选择取sigma的最大值 1/2。
* 这里需要注意放缩之后的不等式方向。由于 $\sigma ≤ 1/2$，所以 $\frac{0.01\sqrt n}{\sigma} \ge \frac{0.01\sqrt n}{1/2}$。接下来画出概率分布图，发现后者前者是更加极端的概率事件，所以 $P(|Z| \ge \frac{0.01\sqrt n}{\sigma}) \le P(|Z| \ge\frac{0.01\sqrt n}{1/2})$。
然后打开绝对值，令单侧分布概率为0.025，求解出误差上界为0.046。

如果要精确让误差在5%，可以算出n = 9604。
![](../images/D9F12488_image 16.png)
![](../images/D9F12488_image 17.png)
