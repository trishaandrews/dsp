[Think Stats Chapter 9 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2010.html#toc90) (resampling)

For Exercise 9.2, write a class named DiffMeansResample that inherits from DiffMeansPermute and overrides RunModel to implement resampling, rather than permutation. The simplest way to implement resampling is to draw a sample with replacement from the observed values, as in Section 9.10.

Use this model to test the differences in pregnancy length and birth weight. How much does the model affect the results?

**Code**
```python
import first
import hypothesis
import thinkstats2

import numpy as np

class DiffMeansResample(hypothesis.DiffMeansPermute):
    
    def RunModel(self):
        group1 = np.random.choice(self.pool, self.n, replace=True)
        group2 = np.random.choice(self.pool, self.m, replace=True)
        return group1, group2
  

def RunPValTests(data):
    resample = DiffMeansResample(data)
    print 'resample p-value =', resample.PValue(iters=10000)

    permute = hypothesis.DiffMeansPermute(data)
    print 'permute p-value =', permute.PValue(iters=10000)

def main():
    thinkstats2.RandomSeed(18)

    live, firsts, others = first.MakeFrames()
    
    print "\npreglength"
    data = firsts.prglngth.values, others.prglngth.values
    RunPValTests(data)
    
    print "\nbirthweight"
    data = (firsts.totalwgt_lb.dropna().values, 
            others.totalwgt_lb.dropna().values)
    RunPValTests(data)
```
**Results**
```
preglength
resample p-value = 0.1674
permute p-value = 0.1717

birthweight
resample p-value = 0.0
permute p-value = 0.0
```

In this case, using resampling versus permutation to model the null hypothesis did not result in a major difference in p-values. The p-values for the pregnancy length variable were only different by 0.0043, and the p-values for the birthweight variable were exactly the same. Still, since the resample and permutation models are implemented differently and rely on different underlying assumptions, it is possible that they would not always be the same. As such, it might be a good idea to use both models in order to have a more complete idea of how the data is behaving.
