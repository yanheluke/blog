---
title: "Lecture 14. Multiple Hypothesis Testing 多重假设检验"
date: 2025-08-10
course: 18.6501x
cover: "73AE224C_image.png"
bear_pk: 73AE224C-6305-4AA1-9D28-4462B75507CE
---

# Lecture 14. Multiple Hypothesis Testing 多重假设检验
#Courses/MITx/18.6501x


## 1. Objectives
### Multiple Hypothesis Testing
At the end of this lecture, you will be able to do the following:
* Understand and avoid the pitfalls of multiple hypothesis testing
* Use the Bonferroni method to control the Family Wise Error Rate (FWER)
* Use the Benjamini-Hochberg method to control the False Discovery Rate (FDR)

## 2. The dead salmon experiment
## 3. The problem with multiple hypothesis testing
![](../images/73AE224C_image.png)![](../images/73AE224C_image 2.png)
![](../images/73AE224C_image 3.png)

### 练习题
TBC
这道题挺有意思的
## 4. Errors in multiple hypothesis testing

多重检验时会出现什么问题？
即使每个试验都严格遵守了T-test，但是每个独立实验的假阳性率加总到一起也是一个巨大的数字，会导致我们做出假阳性的结果。

![](../images/73AE224C_image 4.png)

In the setting of multiple testing, we can control the two following metrics for false significance:
* **Family-wise error rate (FWER)** : the probability of making at least one false discovery, or type I error;
* **False discovery rate (FDR)** : the expected fraction of false significance results among all significance results.

⠀**Family-wise error rate (FWER)**
For a series of tests in which the $i$ th test uses a null hypothesis $H_0^i$ , let the total number of each type of outcome be as follows:
![](../images/73AE224C_image 5.png)

Then the family-wise error rate (FWER) is the probability of making at least one false discovery, or type I error;
$$
 \text{FWER} = \mathbf P(V\geq 1). 
$$
where $V$ is the total number of type I errors as in the table above, i.e., $V=\sum_{i=1}^{m_0}\Psi_i$ where $\{\Psi\}$ is the set of $m_0$ tests for which $H_0$ is true.
In scenarios in which any false claims of discovery may lead to serious consequences, such as for drug approval, we want to control $\text{FWER}$.

$\text{FWER}$ **with no corrections**
Recall from the lecture the paired test in which treatment effects are measured on 100 variables for 1000 people, and the treatment itself is a placebo (of being given water). If we perform $m$ independent tests each at significant level $\alpha$, then the $\text{FWER}$  is
$$
 \text{FWER} = \mathbf P(V\geq1) = 1- \mathbf P(V=0) = 1-(1-\alpha)^m \approx 1 \quad \text{for large}\ m. 
$$
In other words, if we set the significance level of each test without taking into account the large number of tests performed, it is highly likely that the series of tests will lead to at least one false discovery. This often leads to puzzling claims such as water has treatment effect on important health parameters, or eating pizza reduces the risk of cancer.

**False Discovery Rate (FDR)**
Sometimes, controlling  $\text{FWER}$ (the probability of making one or more false discoveries) may be too strict for any discovery to be reported. Instead, we can then control the expected proportion of false discoveries among all discoveries made, the false discovery rate (FDR).
Recall $N_1$ is the total number of discoveries made (the total number of null hypotheses rejected), and $V$ is the number of **false** discoveries (the number of null hypotheses that were falsely rejected). Hence $V \leq N_1$ and $V/N_1$ is a ratio that is always between 0 and 1. If no null hypotheses were rejected, i.e. if $N_1 = 0$, we define the ratio $V/N_1$ to be zero to avoid a division by zero.
The **false discovery rate (FDR)** is
$$
 \text{FDR} = \mathbb E\left[\frac{V}{N_1}\right] 
$$
**FDR versus FWER (TBC)**
Compared to $\text{FWER}$, $\text{FDR}$  has **higher power** . Put another way, $\text{FWER}$ is stricter than $\text{FDR}$.
Let us examine this by considering the trivial scenario where all null hypotheses are true. In this case, any rejected null hypothesis must also be falsely rejected, hence . If any null hypothesis was rejected, then , or if none was rejected, then .
Recall the  is the probability that one or more null hypotheses were falsely rejected. In this scenario, this is the same as the probability that one or more null hypotheses were rejected, since any rejection is a false rejection. We can see now that if one or more null hypotheses were rejected, then , and so
Now consider the general case when some null hypotheses may be false. This time, when , we only know that . Define an indicator varible  which takes value  when . Then


## 5. The Bonferroni method to control FWER
![](../images/73AE224C_image 6.png)
有很多Lecture来不及写进来了。

## 6. The Benjamini Hochberg to control the FDR
![](../images/73AE224C_image 7.png)
![](../images/73AE224C_image 8.png)

**Benjamini-Hochberg Correction**
The Benjamini-Hochberg method guarantees $\text{FDR} < \alpha$ for a series of $m$ **independent** tests. The procedure is as follows:
* Sort the  $p$-values in increasing order $p^{(1)} \leq p^{(2)} \leq ...\leq p^{(i)} \leq ... \leq p^{(m)}$. • Find the maximum $k$ such that
$$
 p^{(k)} \leq \frac{k}{m}\alpha 
$$
* Reject all of $H^{(0)}_0,H^{(1)}_0, …, H^{(k)}_0$ .


For example, the table below shows the $p$-values from 5 hypothesis tests in an experiment in increasing order. We compute the adjusted p-value and compare it with significance threshold of 5%, to decide whether to reject the null hypothesis:
![](../images/73AE224C_image 9.png)
