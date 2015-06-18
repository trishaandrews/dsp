[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

Exercise 2.4 wants to investigate whether first babies are heavier or lighter than other babies by using Cohen's *d* to quantify the weight difference. To solve the problem, I computed the mean weight and variance for first babies and other babies. Then, I computed Coen's *d*, which is the effect size. It is calculated from the mean values and the "pooled standard deviation", which comes from the sample size and variance. It turns out that the mean weight for first babies is slightly less than that for other babies. The calculated Cohen's *d* value of -0.089 confirms this, showing that the first group, or first babies, are 0.089 standard deviations smaller than the second group, or other babies. In comparison to the difference in pregnancy length, which had an effect size of 0.029, the effect size of difference in weight is roughly three times larger. However, both values are still quite small. The chapter uses a value of 1.7, for the difference in height between men and women, as an example of a more significant effect size.

```python
def WeightDifference(firsts, others):
    
    mean1 = firsts.totalwgt_lb.mean()
    mean2 = others.totalwgt_lb.mean()
    
    var1 = firsts.totalwgt_lb.var()
    var2 = others.totalwgt_lb.var()
    
    diff = mean1 - mean2
    n1, n2 = len(firsts), len(others)
    
    pooled_var = (n1 * var1 + n2 * var2)/(n1 + n2)
    d = diff/math.sqrt(pooled_var)
    
    return d
```
