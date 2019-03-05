# Maximum Subarray Sum

Origin Challenge: [Maximum Subarray Sum](https://www.hackerrank.com/challenges/maximum-subarray-sum)

**Problem Description**

- Given a array $a$ of size $n$ and a number $m$, calculate the maxmimum of $subarray(i,j)\%m$.
- A subarray of $a$ is a contiguous segment from $a[i]$ through $a[j]$ where $0\le i \le j \lt j$.

**Relative Math formula**

$$(a+b)\%M=(a\%M+b\%M)\%M$$(1)
$$(a-b)\%M=(a\%M-b\%M+M)\%M$$(2)

define $prefix(i)=(a[0]+\dots+a[i])\%n$, according to (1), $preix[j]$ is given by

$$
\begin{matrix}
prefix(i+1) & = & (a[0]+\dots+a[i]+a[i+1])\%M \\
& = & ((a[0]+\dots+a[i])\%M+a[i+1]\%M)\%M \\
& = & (prefix(i)+a[i+1]\%M)\%M
\end{matrix}
$$

<br/>

$$
\begin{matrix}
(a[i]+\dots+a[j])\%M &=& (a[0]+\dots+a[j]-(a[0]+\dots+a[i-1])+M)\%M \\
&=& ((a[0]+\dots+a[j])\%M-(a[0]+\dots+a[i-1])\%M+M)\%M \\
&=& (prefix(j)-prefix(i-1)+M)\%M
\end{matrix}
$$

**Keys**

Given $subarray(i,j)\%M=(prefix(j)-prefix(i-1)+M)\%M$, if $prefix(i-1) \lt prefix(j)$ note that:

$$
(prefix(j)-prefix(i-1)+M)\%M\lt prefix(j)
$$

The key is to find the first $prefix(i-1)$ which is greater that $prefix(j)$

**Steps**

- calculate $prefix(i)$ for $i=1:n$
- sort $prefix(i)$
- loop through $prefix(i)$, find the first $j$ such that $j \lt i,prefix(j) \gt prefix(i)$.
  $result = max(result, (prefix(j)-prefix(i-1)+M)\%M)$  
  One can use an ordered list to store $prefix(0:i-1)$ and use `bisect_right` to find the first (cheapest) element greater that $prefix(i)$.

**Reference**  
[1][what is the logic used in the hackerrank maximise sum](https://www.quora.com/What-is-the-logic-used-in-the-HackerRank-Maximise-Sum-problem)  
[2][code reference](https://www.hackerrank.com/challenges/maximum-subarray-sum/forum/comments/484515)  
[3][my code](https://www.hackerrank.com/challenges/maximum-subarray-sum/submissions/code/100944423)
