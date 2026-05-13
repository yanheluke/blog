---
title: "(Optional) Recitation 1. Modes of Convergence 收敛性的模式"
date: 2025-08-10
course: 18.6501x
bear_pk: 27FB8276-101E-4F51-B97E-43D6E494DDD4
---

# (Optional) Recitation 1. Modes of Convergence 收敛性的模式
#Courses/MITx/18.6501x

## 1. Modes of Convergence
$X_n$ 是一个随机变量序列，如果他与随机变量 $X$ 具有以下关系，认为 $X_n \rightarrow X$ 具有收敛性。
### Convergence almost surely 几乎处处收敛
definition：
$$
\begin{align}
X_n \xrightarrow[n\rightarrow\infty]{a.s}X,\ \text{iff } \mathbf P(X_n\xrightarrow[n\rightarrow\infty]{}X) = 1\\ 等价于： \lim_{n\rightarrow\infty}X_n = X 
\end{align}
$$
### Convergence in probability 依概率收敛
definition:
$$
\begin{align}
 X_n \xrightarrow[n\rightarrow\infty]{p}X,\quad \text{iff } \forall \epsilon > 0, \ \mathbf P(|X_n -X| > \epsilon) \xrightarrow[n\rightarrow\infty]{} 0\\ 等价于： \lim_{n\rightarrow\infty}P(|X_n-X|>\epsilon) = 0 
\end{align}
$$
### Convergence in distribution 依分布收敛
definition:
$$
\begin{align}
 X_n \xrightarrow[n\rightarrow\infty]{d}X,\quad \text{iff } F_{X_n}(x) \xrightarrow[n\rightarrow\infty]{}F_X(x) \\ 等价于： \lim_{n\rightarrow\infty}F_{X_n}(x) = F_X(x) 
\end{align}
$$

## 2. Example 1 证明几乎处处收敛
定义 $U \sim \text{Unif}[0,1], \ X_n = U + U^n$.
证明： $X_n \xrightarrow[a.s]{n\rightarrow\infty} U$。
证明这个性质需要用到全概率定理（law of total probability):

> Law of Total Probability
> $S$ 是样本空间（sample space)，将其分为两个互斥空间: $S = S_1\coprod S_2$.
> for any given event A:
> $P(A) = P(A|S_1)P(S_1) + P(A|S_2)P(S_2)$

现在分阶段讨论U的收敛性：
1 U < 1: $$P(X_n
