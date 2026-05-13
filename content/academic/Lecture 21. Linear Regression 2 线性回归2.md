---
title: "Lecture 21. Linear Regression 2 线性回归2"
date: 2025-08-09
course: 18.6501x
cover: "1B314286_image.png"
bear_pk: 1B314286-F4ED-4787-B56D-0C777F922898
---

# Lecture 21. Linear Regression 2 线性回归2
#Courses/MITx/18.6501x

## **1. Objectives** 目标 
### **Multivariate Linear Regression** 多元线性回归

At the end of this lecture, you will be able to
* Write down the **multivariate linear regression model** .
* Compute the **distribution of the least square estimator (LSE)** for linear regression with **deterministic design** .
* Know that in the setting of deterministic design, the least square estimator is the maximum likelihood estimator.
* Compute the **quadratic risk** and **prediction error** of the LSE.
* Perform **hypothesis test** for linear regression models.
* Design **Bonferroni's tests** for testing multiple hypotheses.

## **2. Linear Independence and Rank** 线性不相关与秩
这一节主要是复习线性代数里的线性无关、向量张成和维度以及矩阵的秩 三个内容。

### **Linear Independence** 线性不相关
线性相关：指对向量 $v_1, \dots, v_n$ ，有一组**不全为零**的标量 $c_1, \dots, c_n$，使：
$c_1v_1+\dots+c_nv_n=0$。 反之则是线性无关。
特别的，对两组非零向量 $v_1, v_2$, 当且仅当 $v_1 = cv_2$ 时，两者线性相关。简单说就是两个向量呈倍数关系。
examples：
![](../images/1B314286_image.png)<!-- {"width":498} -->![](../images/1B314286_image 2.png)<!-- {"width":498} -->

### **Span and dimension** 张成与维度
由非零向量 $\mathbf{v}_1, \dots, \mathbf{v}_n \in \mathbb{R}^m$ 组成的集合确定了 $\mathbb{R}^m$ 的一个子空间。
这个 $\mathbb{R}^m$ 的**子空间**，也称为向量 $\mathbf{v}_1, \dots, \mathbf{v}_n$ 的**张成空间**（span），是所有形如
$c_1\mathbf{v}_1 + \cdots + c_n\mathbf{v}_n$ 的向量的集合，其中 $c_1, \dots, c_n \in \mathbb{R}$。
记作

$$
\langle \mathbf{v}_1, \dots, \mathbf{v}_n \rangle 
= \{ \mathbf{v} \in \mathbb{R}^m : \mathbf{v} = c_1 \mathbf{v}_1 + \cdots + c_n \mathbf{v}_n \}
$$
（即 $\mathbf{v}_1, \dots, \mathbf{v}_n$ 的 span）。

这个子空间 $\langle \mathbf{v}_1, \dots, \mathbf{v}_n \rangle$ 的**维数**，是由这些（非零）向量 $\mathbf{v}_1, \dots, \mathbf{v}_n$ 中能取出的**最大数量的线性无关向量**所决定的。

回到上一部分的例子中：
1. 张成空间是任意一个向量。意味着任意一个向量张成为整个子空间，所以子空间维度为1；
2. 张成空间是两个向量，子空间维度为2；
3. 张成空间是两个向量，子空间维度为2；
4. 在三个向量线性相关，任意两个向量张成为子空间，维度为2；
5. 这个比较复杂。前三个向量是线性相关的，因此span维度为2；第三个向量与前三个都线性无关，所以总span 维度为2+1 = 3

### **Rank** 秩
矩阵的**列空间**（column space）和**行空间**（row space）分别是由矩阵的列和行张成的子空间。
线性代数中的一个事实是：矩阵 **M** 的列空间的维数等于它的行空间的维数（你可以通过行化简来验证这一点）。
这个维数就是矩阵的**秩**（rank），记作 $\mathrm{rank}(\mathbf{M})$。
并且有 $\mathrm{rank}(\mathbf{M}) = \mathrm{rank}(\mathbf{M}^T)$。

这里的意思就是：矩阵的行秩 = 列秩 = 秩，而且转置不会改变秩。
一个 $m \times n$ 矩阵的秩为 $\min(m,n)$ 。

判断矩阵的秩有以下几个方法：
**1. 行化简法（最常用）**
* 把矩阵通过**初等行变换**化为**行阶梯形（row echelon form）**或**最简行阶梯形（reduced row echelon form）**。
* **非零行的个数**就是矩阵的秩。
* 适合手算，也方便在概念上理解秩 = 最大线性无关行（列）的个数。
> ### 判断步骤
> 1. 检查矩阵的每一行，从上到下。
> 2. 如果整行都是 0 → 不计入 rank。
> 3. 如果该行有主元（第一个非零元素），就算作一行。
> 4. 统计所有有主元的行数，这个数就是 rank。

**2. 线性无关法**
* 通过判断列向量（或行向量）之间的线性无关性，找到最大线性无关组的个数，这个数就是秩。
* 可以用**解线性方程组**的方法来判断线性无关性。
* 适合低维矩阵或概念推导，不太适合大矩阵手算。

**3. 行列式法（方阵或子式法）**
* 对于方阵：如果 $\det(M) \neq 0$，则 rank = 矩阵的阶数。
* 对于一般矩阵：找出矩阵中所有阶数的子式（submatrix determinant），最大非零子式的阶数就是矩阵的秩。
* 缺点：大矩阵计算行列式会很麻烦。

**4. 奇异值分解（SVD）法**
* 数值计算中常用：
$$
M = U \Sigma V^T
$$
秩 = $\Sigma$ 中非零奇异值的个数。
* 稳定、适合用计算机做数值分析（比如浮点数误差环境）。

**5. 特征值法（对称矩阵或方阵）**
* 对于对称矩阵（或厄米矩阵）：
$$
  \text{rank}(M) = \text{非零特征值的个数（重数计入）}
$$
* 适合理论分析和数值计算，尤其是对称正定矩阵判断满秩时非常方便。

### **The rank of a matrix** 矩阵的秩
这道题旨在回答这样一个问题：**如果你把两个秩为 1 的矩阵相加，会得到一个秩为 2 的矩阵吗？** 乘积的情况又是怎样的呢？更一般地说，秩为 $r_1$ 的矩阵与秩为 $r_2$ 的矩阵相加，它们的和的秩是多少？设
$$
A = \begin{pmatrix} -1 & 1 \\ -3 & 3 \end{pmatrix}, \quad
B = \begin{pmatrix} 1 & -1 \\ -1 & 1 \end{pmatrix}, \quad
C = \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix}, \quad
D = \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}
$$
可以看到，这四个矩阵的秩都是 1。
有很多方法可以用来判断矩阵的秩。这里提供一个有用的事实：
> **每一个秩为 1 的矩阵都可以写成两个向量的外积。反之，每一个外积 $\mathbf{u} \mathbf{v}^T$ 都是一个秩为 1 的矩阵。**
例如：
$$
A = u v^T, \quad B = v v^T, \quad C = w w^T, \quad D = x x^T
$$
其中：
$$
u = \begin{pmatrix} 1 \\ 3 \end{pmatrix}, \quad
v = \begin{pmatrix} -1 \\ 1 \end{pmatrix}, \quad
w = \begin{pmatrix} 0 \\ 1 \end{pmatrix}, \quad
x = \begin{pmatrix} 1 \\ 1 \end{pmatrix}.
$$
计算: $A+A, A+B, A+C, AB, AC, BD$ 的秩。

如果两个矩阵相加的结果可以被化简为： $ut^T$ 的形式，那么根据定义，这仍然是一个rank=1的矩阵。更进一步的，如果中间的值可以被合并为一个内积（标量），也不影响结果。
例如:
$A+B = uv^T + vv^T = (u+v)v^T$ ，rank = 1.
$AB = uv^Tvv^T = u(v^Tv)v^T$ ，中间是内积，结果是一个标量，不影响结果，rank  =1。

## **3. Multivariate Regression: Definitions, Modeling, and Matrix LSE** 多元回归：定义，建模与矩阵LSE
### **Multivariate Regression: Setup and Definitions**
定义一个多元线性回归的方程形式为：
$$
Y_i = \mathbf X_i^T\beta^* + \epsilon_i, \quad i = 1,\dots, n
$$
注意在这节课上定义的 $\mathbf X_i$ 是p*1的列向量，每一列是一个样本，每一行是特征。这与完整的矩阵运算有一些区别。
一般矩阵形式会直接写成 $\mathbf Y = \mathbf X\theta + \text{bias}$ ，其中 $X_{m\times n}$, m个样本，n个特征；$\theta_{n\times1}$ ，n个特征的权重。写成代码的话一般是```y_pred = X @ theta```, 输出值Y是一个 $m\times 1$ 维向量。
但在神经网络里又不一样： hidden_layer_weighted_input（隐藏层加权输入）：```input_to_hidden_weights @ input_values + self.biases``` , 输出值Y是一个(输出单元数，1)向量。
![](../images/1B314286_image 3.png)

### **LSE in Matrix Form: Setup**
接下来我们利用矩阵形式来表达LSE估计量。
$$
\mathbf Y = \mathbb X\beta^* + \epsilon
$$
$Y \in \mathbb R^n$, 是一个(n,1)维向量
$\mathbb X_{n\times p}$ 是设计矩阵，(n, p)维矩阵
$\beta$ 是特征权重，(p, 1)维向量。
> 当 $\mathbf X$ 是协变量向量时（即单样本情况下）， $\beta^T\mathbf X$ 和 $\mathbf X\beta^T$ 是等价的，结果都是标量。但如果是X是矩阵，这个等式就不成立了。

LSE估计量 $\hat \beta$ 满足下列条件：
$$
\hat \beta = \arg\min_{\beta\in\mathbb R^p}\left\Vert \mathbf Y-\mathbb X\beta\right\Vert^2_2
$$
注意这里用到了L2范数平方。
**1. 下标的 2（$\| \cdot \|_2$）**: 表示这是 **L₂ 范数**（欧几里得范数），用平方和开根号来度量向量的长度。
$$
\|v\|_2 = \sqrt{v_1^2 + v_2^2 + \dots + v_n^2}
$$
**2. 上标的 2（$^2$）**，表示 **把范数的结果再平方**，这样根号会被消掉，得到的是平方和：
$$
\|v\|_2^2 = \left( \sqrt{v_1^2 + v_2^2 + \dots + v_n^2} \right)^2
$$
$$
\|v\|_2^2 = v_1^2 + v_2^2 + \dots + v_n^2
$$
![](../images/1B314286_image 4.png)

### Linear Regression as a Statistical Model  线性回归作为一个统计模型
TBD 这里主要是考察将线性回归映射维一个统计模型之后，看样本空间与参数空间的取值范围。


## **4. Multivariate Linear Regression** 多元线性回归
### **Review: Setup of Multivariate Linear Regression**

![](../images/1B314286_image 5.png)

求L2范数平方对 $\beta$ 的梯度（这里的 $\beta$ 是一个p维向量，所以这里是求梯度，而不是偏导，即对 $\beta$ 的每一个分量都求偏导再集合到一个向量里）。
求矩阵梯度时，需要考虑 $\mathbb X$ 是放在左边还是右边。这里可以直接尝试：$\mathbb X$ 是(n,p)维矩阵，$\mathbf Y$ 是(p,1)维向量，所以X不能出现在右边（不符合矩阵乘法）；如果放在左边，需要将X转置。
![](../images/1B314286_image 6.png)


## **5. Geometric Interpretation of Linear Regression** 线性回归的几何解释

在进行Y和beta的几何解释时，需要将其放在一个平面上（这两个向量维度不同，无法直接比较）

$X\beta^*$ 在 $X$ 的线性张成（linear span)里。 真实值 $Y$ 是距离这个超平面距离最短的（orthogonal projection，正交投影）。
![](../images/1B314286_image 7.png)

数学证明：
Y的正交投影是 $\mathbf PY$, $\mathbf P$ 是一个(n,n)矩阵，并且 $\mathbf P^2 = \mathbf P$ 。
证明： $\mathbf X\hat\beta = \mathbf PY$ 
![](../images/1B314286_image 8.png)
![](../images/1B314286_image 9.png)

![](../images/1B314286_image 11.png)

## **6. Linear Regression with Deterministic Design** 具有确定性设计的线性回归

为了进行统计推断，我们需要对模型进行更多的假设：
* 设计矩阵 $\mathbb X$ 是确定性的（意味着 $\mathbb X$ 不再是一个随机变量），并且rank = p；
* 模型是同方差的，意味着噪声 $\epsilon_1, \dots, \epsilon_n$ 是iid的；
* 噪声向量 $\epsilon \sim \mathcal N(0, \sigma^2I_n)$ 

这样我们可以知道 $Y \sim \mathcal N(\mathbb X\beta^*, \sigma^2I_n)$ ，并且在模型 $\mathbf Y = \mathbb X\beta + \epsilon$ 的右边，只有一个随机变量：噪声。并且 $Y$ 仍然是随机的。
![](../images/1B314286_image 10.png)

### Deterministic Design
根据上述假设，我们可以计算 LSE $\hat\beta$ 也是一个随机变量，并且他的期望等于：
* $(\mathbb X^T \mathbb X)^{-1} \mathbb X^T E[Y]$
* 进一步化简，由于 $E[Y] = \mathbb X\beta$ ，带入上面的公式化简，得到 $\beta$。 

### Uniform Noise
现在将噪声从正态分布变为 $\epsilon \sim Unif[-1,1]^n$ 。那么：
* 模型仍然是同方差的，因为噪声的方差为1/3；
* Y仍然为随机变量；
* LSE $\hat \beta$ 服从均匀分布。
> 因为 $\hat \beta = (\mathbb X^T \mathbb X)^{-1} \mathbb X^T Y = \beta + (\mathbb X^T \mathbb X)^{-1} \mathbb X^T\epsilon$ ，所以决定这个分布的仍然是 $\epsilon$ 的分布

## **7. Deterministic Design with Gaussian Noise** 具有高斯噪声的确定性设计
### Review of Multi-Dimensional Gaussians
![](../images/1B314286_image 12.png)
这道题的解法就是从定义入手，需要先求解E[Y]。
$E[Y] = E[MX] = ME[X] = 0$ 
$\Sigma_Y = E[(Y-E[Y])(Y-E[Y])^T] = E[YY^T]$
带入 $Y=MX$, 有 $E[MX(MX)^T] = E[MXX^TM^T] = M\cdot E(XX^T)\cdot M^T$
因为 $E[XX^T] = \Sigma_X = E[(X-E[X])(X-E[X])^T]$
所以最后有: $\Sigma_Y = M\Sigma_x M^T$

### **The Least Square Estimator is the MLE in Deterministic Design**

在假设噪声服从正态分布的时候， **LSE = MLE**。
推导过程见PPT：首先写出 Y_i的PDF，然后LN，再Log，可以发现优化目标与LSE是一致的。
但当假设噪声服从其他分布（例如拉普拉斯分布时），这就不再成立。

![](../images/1B314286_image 13.png)
![](../images/1B314286_image 14.png)


## **8. Distribution of the Least Square Estimator** 最小均方估计量的分布

### $\hat\beta$ 的分布

$\hat \beta$ 也是一个正态分布
由: $\hat \beta = (X^TX)^{-1}X^TY =  (X^TX)^{-1}X^T[X\beta^*+\epsilon]$ ，有：
$(X^TX)^{-1}X^T[X\beta^*+\epsilon] = (X^TX)^{-1}X^TX\beta^*+(X^TX)^{-1}X^T\epsilon$  
$=\beta^* + (X^TX)^{-1}X^T\epsilon$
后者是一个正态分布，所以 $\hat \beta$ 也是一个正态分布。

我们现在讨论 $(X^TX)^{-1}X^T\epsilon$ 的性质。
他的期望为0，方差化简要用到线性变换的方差公式：
> 如果A是一个常数矩阵（非随机），z是一个随机向量，那么:
> $Var(Az) = A\ Var(z)\ A^T$
所以方差为： $(X^TX)^{-1}X^T(\sigma^2I_n)X(X^TX)^{-1}$  （这里有一个trick: $(X^TX)^{-1}$ 的转置，逆和转置可以交换，所以等于  $((X^TX)^T)^{-1}$，又因为 $(X^TX)$ 是对称矩阵，转置等于自身。所以有了上面的形式。
再对方差化简，有 $\sigma^2(X^TX)^{-1}$。
![](../images/1B314286_image 15.png)

现在考虑 $(X^TX)^{-1}$  代表什么含义？
假设这是一个单变量模型，那么 $X^TX$ 是一个内积，衡量不同的样本点X的集中度距离。如果样本越集中（即X^TX越小，他的逆越大），那么回归方程的斜率越难以确定。反之，样本越发散，斜率就越容易确定。
![](../images/1B314286_image 16.png)


## **9. Example: Assessing the performance of planes**
略，一道简单的练习题


## **10. Quadratic Risk and Variance** 二次风险与方差

### 计算 $E\left\Vert \hat \beta - \beta^*\right\Vert^2$ 
首先需要用到一个关于trace的技巧：
> 对一个向量x来说， $||x||^2 = x^Tx$ ， 这是一个标量，也可以看成是一个(1,1)的矩阵。
> 拓展到矩阵维度， $||X||^2 = tr(X^TX)  = tr(XX^T)$。 矩阵形式的L2范数就是Frobenius范数。
> 标准的Frobenius范数是指 $A \in \mathbb R^{m\times n}, \ ||A||_F = \sqrt{\sum_i^n\sum_j^m a^2_{ij}}$ 。在这道题里即为 $||X||^2 = \sum_{i,j}^px_{ij}^2$ ，也是一个标量。
> trace的期望等于期望的trace。

所以可以开始变形：
$E\left\Vert \hat \beta - \beta^*\right\Vert^2 = E[tr(\hat \beta - \beta^*)(\hat \beta - \beta^*)^T] = tr(E[(\hat \beta - \beta^*)(\hat \beta - \beta^*)^T]$
注意到由于 $E[\hat \beta - \beta^*]=0$, 所以上面的期望等同于 $Cov(\hat\beta-\beta^*)$ 协方差矩阵，也即等于 $\sigma^2(X^TX)^{-1}$ 。

所以，有 $E\left\Vert \hat \beta - \beta^*\right\Vert^2 = \sigma^2tr((X^TX)^{-1})$ 。

![](../images/1B314286_image 17.png)

### The Quadratic Risk

我们考虑两种误差：
* quadratic risk of $\hat \beta$: $\mathbb E[||\hat\beta -\beta||^2_2]$ 。 衡量估计量 $\hat\beta$  与真实值 $\beta$ 的差异。
* prediction error $\mathbb E[||\mathbf Y-\mathbb X\hat\beta||^2_2]$ 。 衡量预测值 $\mathbf {\hat Y} = \mathbb X\hat\beta$ 与真实值 $\mathbf Y$ 的差异。

随着 $\sigma^2$ 增大，两种误差都会上升。

## **11. Prediction Error** 预测误差

### **Prediction Error**
计算预测误差时用到了投影矩阵，这一段不太熟悉对应的线性代数知识

![](../images/1B314286_image 18.png)

打开norm的平方，这里也用到了一个线性代数知识 $||u+v||^2 = ||u||^2+||v||^2+2*u^Tv$ 

![](../images/1B314286_image 19.png)

![](../images/1B314286_image 20.png)

### Estimating the variance
![](../images/1B314286_image 21.png)

求解 $\hat\sigma^2$ 。
注意套用公式的时候，n = 1000, p = 2（包含截距项）

### **Properties of LSE**

注意 $\hat\sigma^2$ 的公式右边就不再有期望符号了，因为这个时候我们是带入具体的数据进行计算，但是一个确定的数，不需要再加上E[]。期望E[]只在理论推导的时候有作用。
![](../images/1B314286_image 22.png)


## **12. Significance Tests** 显著性检验

### **Significance Tests**

令 $\gamma_j$ 是 $(\mathbb X^T\mathbb X)^{-1}$ 的第j个对角线系数（diagonal coefficient）。
如果我们知道 $\sigma^2$, 那么对 $\hat\beta_j$ 可以变形为一个标准正态分布。

![](../images/1B314286_image 23.png)

但我们不知道 $\sigma^2$ ，所以必须使用无偏估计量来plug in。
这个检验统计量的分布就不再是标准正态分布，而是一个T分布了。
![](../images/1B314286_image 24.png)


![](../images/1B314286_image 25.png)


### Building a hypothesis test
一道练习题，可以在复习一下

### Statistics for the LSE


### Designing the test


## **13. Bonferroni's Test and Remarks**

### **Bonferroni's Test**
在多元线性回归里，因为同时存在多组待估计的参数 $\hat\beta_j$ , 所以存在多重假设检验问题。
对多重假设检验（实际违阳性率过高），有两种解决的思路。

一是利用统计学通用的多重检验方法：Bonferroni’s Test, BH方法。这个在生物统计上用的比较多。
二是用计量经济学的方法： F检验。
> F检验：检验所有待估计参数不全为零。即H0假设为：
> $\beta_0= \beta_1 = \dots_ = \beta_j = 0$

![](../images/1B314286_image 26.png)

**核心区别对比**
| 维度        | F检验                                      | Bonferroni校正              | BH方法（FDR控制）        |
|:---------:|:----------------------------------------:|:-------------------------:|:------------------:|
| 检验目标      | 检验一组系数联合是否显著                             | 控制多个独立检验的FWER             | 控制显著结果中假阳性的比例      |
| 假设形式      | H_0:<br>\beta_1=\beta_2=\cdots=\beta_k=0 | 分别检验各H_0^{(j)}: \beta_j=0 | 同Bonferroni        |
| 统计量       | 基于模型拟合优度比较（RSS）                          | 调整单次检验的p值阈值（\alpha/m）     | 按p值排序动态调整阈值        |
| 错误率控制     | 控制整体拒绝H₀的犯错概率 （FWER）                     | 严格控制FWER（\leq \alpha）     | 控制FDR（假阳性占显著结果的比例） |
| 适用场景      | 变量组、模型整体显著性                              | 独立或弱相关的多重检验               | 高维探索性分析（如基因组学）     |
| 功效（Power） | 较高（联合利用变量间信息）                            | 低（过度保守）                   | 中等（权衡严格性与发现能力）     |


### **Closing Remarks**

* 线性回归只展示相关性，不是因果性；
* 噪声正态：噪声服从正态分布是模型的假设，实际中不一定正确。可以使用goodness of fit test或KS/QQ-PLOT去检验噪声是否服从正态分布；
* 确定性设计：如果 $\mathbb X$ 不是确定性的（即 $\mathbb X$ 也为一个随机矩阵），上面讨论的所有性质可以被视为：在 $\mathbb X$ 的条件下，如果噪声假设为高斯分布，condintionally on $X$. 
![](../images/1B314286_image 27.png)

