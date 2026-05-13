---
title: "[Lecture 18] Inequalities, convergence, and the Weak Law of Large Numbers 不等式，收敛性与弱大数定律"
date: 2025-08-07
course: 6.431
cover: "00B15142_image 2.png"
bear_pk: 00B15142-1A22-446D-B016-7CE84B84F06D
---

# **[Lecture 18] Inequalities, convergence, and the Weak Law of Large Numbers 不等式，收敛性与弱大数定律**
#Statistics & Machine Learning# #Courses/MITx/6.431
## 1. Lecture 18 overview and slides 概览
![](../images/00B15142_image 2.png)
Printable transcript available ~[here](https://courses.edx.org/asset-v1:MITx+6.431x+2T2025+type@asset+block/transcripts_L18-Overview.pdf)~.
Lecture slides: ~[\[clean\]](https://courses.edx.org/asset-v1:MITx+6.431x+2T2025+type@asset+block/lectureslides_L18-clean-slides.pdf)~ ~[\[annotated\]](https://courses.edx.org/asset-v1:MITx+6.431x+2T2025+type@asset+block/lectureslides_L18-annotated-slides.pdf)~
The material in this lecture is covered in ~[Sections 5.1-5.3](https://courses.edx.org/courses/course-v1:MITx+6.431x+2T2025/pdfbook/0/chapter/1/39)~ of the text.

### 2. The Markov inequality 马尔可夫不等式
马尔可夫不等式试图利用有限的信息（例如只知道期望）来回答极端事件的概率。
PPT给出了连续rv下的马尔可夫不等式推导，中间利用到了（对任意x都≥a，所以整个积分应该大于将x替换为a的积分）的性质。
![](../images/00B15142_image 3.png)

第二种推导方式更加简单：构造一个特殊的r.v. Y， 利用Y的期望性质来计算。（Y ≤ X, so 期望也符合这个不等式）。
![](../images/00B15142_image.png)
接下来是两个利用马尔可夫不等式的案例。
案例1中X是一个指数分布，可以很明显看出P(X≥a)的真实值为e^(-a)，而马尔可夫不等式给出的上界是1/a，要远大于真实值。
案例2中X是一个均匀分布，但注意这里因为X包含了负数，所以不能直接利用马尔可夫不等式。可以通过将X取绝对值来符合马尔可夫不等式的定义，计算出的上界是2/3。（更进一步，可以利用均匀分布的对称性，将绝对值又转化为原本的X形式，计算出上界为1/3）。
同样远大于真实值1/8。
![](../images/00B15142_image 4.png)

### 3. Exercise: Markov inequality
> [!IMPORTANT]
> Let $Z$ be a nonnegative random variable that satisfies $E(Z^4) = 4$. Apply the Markov inequality to the random variable $Z^4$ to find the tightest possible (given the available information) upper bound on $P(Z≥2)$.

这道题不能通过将 $E(Z^4)=4$ 化简，因为只知道四阶矩，推导不出一阶矩。因此需要想办法将Z变形为Z^4.
$$ 
P(Z\ge2) = P(Z^4\ge16) \le \frac{E[Z^4]}{16} = 1/4 
$$
### 4. The Chebyshev inequality 切比雪夫不等式
从数学上看，切比雪夫不等式是马尔可夫不等式的一个更简单的应用。
切比雪夫不等式的要求是： X是一个随机变量，有限的均值和方差。
* 对比马尔可夫不等式，切比雪夫不等式除了使用期望，还用到了方差的信息。

⠀在证明切比雪夫不等式时，需要用到马尔可夫不等式，注意到 $E[(X-\mu)^2]= Var(X-\mu) + E[(X-\mu)]^2. 方差等于 \sigma^2, 后面的期望为0.$
![](../images/00B15142_image 5.png)
以下是切比雪夫不等式应用的一个例子：
如果我们假设k = 3：意味着我们在计算距离中心三个标准差的概率，这个概率≤1/9，对任何分布都成立。
如果我们继续使用上述的指数分布的案例，假设a是一个非常大的正整数：
* 首先我们可以推导出 $P(X-1\ge a-1) \le P(|X-1|\ge a-1)$ (单侧概率小于双侧概率）
* 然后套用切比雪夫不等式，因为a非常大，所以 $1/(a-1)^2 \approx 1/a^2$.
* 切比雪夫不等式给到了一个比马尔可夫不等式更小的上界。
![](../images/00B15142_image 6.png)
### 5. Exercise: Chebyshev inequality
直接套用公式的题
### 6. Exercise: Chebyshev versus Markov
注意切比雪夫不等式并不一定 永远都比马尔可夫不等式提供一个更强的上界。只有当a 足够大的时候，这个结论才成立。

### 7. The Weak Law of Large Numbers 弱大数定律WLLN
样本均值是一个随机变量（他是 $X_i$ 随机变量的函数），而总体均值（期望是一个常数）
样本均值的期望等于总体期望；
* $E[M_n]$ 代表了两个平均：$M_n$ 是单次长实验中(one long experiment) 所有观测值 $X_i$ 的均值；而 $E[]$ 是对所有实验结果的期望。

⠀样本均值的方差等于总体方差/n 。（这里推导时用到了 $Var(X_i) = \sigma^2$ ）
再利用切比雪夫不等式，可以得到弱大数定律的形式：
**当n趋近于无穷时，样本均值减去期望的绝对值大于某个固定常数 $\epsilon$ 的概率趋近于0。**
![](../images/00B15142_image 7.png)
解释WLLN：
* 在一次实验中，即使每次抽样X_i的观测值都有误差，但样本均值不可能距离真实均值太远；
* 在同一个实验的多次独立重复中：样本均值就是事件A发生的经验频率。
![](../images/00B15142_image 8.png)
### 8. Exercise: Sample mean bounds

### 9. Polling 选举问题
**选举问题**
这是一个关于WLLN和切比雪夫不等式的应用。
假设你进行选民抽样，如果你希望让整体抽样误差足够小： $|M_n - p| \le 0.01$，这是做不到的（无法确定性的保证，因为包含了未知参数p）。
接下来，我们改成将抽样误差大于0.01的概率足够小。这时候可以使用WLLN进行计算。
假设n = 10000, 同时总体方差未知，但由于这是一个伯努利分布，我们可以求出p(1-p)的最大值是1/4。这样可以计算出抽样误差大于0.01的最大概率为25%。
如果想进一步减小抽样误差过大的概率，那么只能：
* 增加n的数量。当n=50000时，可以解出最大误差概率为5%；
* 增大误差。例如可以把0.01的误差扩大到0.05或更大。
![](../images/00B15142_image 9.png)
### 10. Exercise: Polling
### 11. Convergence in probability 依概率收敛
这里定义的依概率收敛：指的是：
一个序列Y_n，依概率收敛于一个数a。
![](../images/00B15142_image 10.png)
**对比常规收敛与依概率收敛**
![](../images/00B15142_image 11.png)
**依概率收敛的性质**
如果 $X_n \rightarrow a, Y_n \rightarrow b$, 依概率收敛。
* 如果 $g(·)$ 是连续的，那么 $g(X_n) \rightarrow g(a)$
* $X_n + Y_n \rightarrow a+b$

⠀但需要注意：如果 $X_n \rightarrow a$，**不能得出** $E[X_n] \rightarrow a$
![](../images/00B15142_image 12.png)
### 12. Convergence in probability examples 依概率收敛的例子
案例1说明，依概率收敛于0，但期望却趋近于无穷大。
**依概率收敛只依赖分布的主体部分，不care尾部分布；然而期望对尾部分布更加敏感。**
![](../images/00B15142_image 13.png)
第二个案例更典型：
当X服从一个均匀分布时，X并不收敛于任何常数。
但如果我们令 $Y_n = \min\{X_i, \dots,X_n\}$，这时Y_n收敛于0。
推导过程（注意在这个18.6501的伯努利分布时常用到类似的化简技巧）：
$P([|Y_n - 0|\ge \epsilon) = P(Y_n \ge \epsilon)$ 等同于所有一个X_i都必须大于 $\epsilon$，等于概率连乘，所以最后等于： $(1-\epsilon)^n$
![](../images/00B15142_image 14.png)
总结：当我们想展示依概率收敛时：
* 第一步：猜测这个序列收敛于什么常数；
* 第二步：写出 $\epsilon$ 的概率表达式，计算其概率，展示其等于0.

### 13. Exercise: Convergence in probability

### 14. Related topics 相关主题
**对尾部概率更好的bound（界）：**
* 马尔可夫与切比雪夫不等式
* Chernoff bound (切诺夫界）
* 中心极限定理CLT

⠀**不同类型的收敛：**
* 依概率收敛
* 依概率1收敛：对一个随机变量序列 $Y_n$，对一个实验的确定性输出结果 $\omega$， 关注 $Y_n(\omega )\rightarrow_{n\rightarrow \infty} Y(\omega)$。如果 $P(\{\omega: Y_n(\omega) \rightarrow_{n\rightarrow\infty}Y(\omega)\}) = 1$，我们说Y_n依概率1收敛于Y
* 序列CDF收敛于极限CDF
![](../images/00B15142_image 15.png)


