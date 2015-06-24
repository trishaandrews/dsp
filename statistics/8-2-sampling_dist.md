[Think Stats Chapter 8 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2009.html#toc77) (scoring)

Exercise 8.2 asks to simulate an experiment of sample size n = 10 and exponential distribution λ = 2. Next, use this simulation to plot the sampling distribution of the estimate L and compute its standard error and the 90% confidence interval. Finally, plot the standard error versus n for several n values.

**Complete code:**
```python
import thinkstats2
import thinkplot
import math
import numpy as np

def RMSE(estimates, actual):
    e2 = [(estimate-actual)**2 for estimate in estimates]
    mse = np.mean(e2)
    return math.sqrt(mse)

def Estimate(lam=2, n=10, m=1000):
    estimates = []
    for j in range(m):
        xs = np.random.exponential(1.0/lam, n)
        bigL = 1.0 / np.mean(xs)
        estimates.append(bigL)
    stderr = RMSE(estimates, lam)
    cdf = thinkstats2.Cdf(estimates)
    ci = cdf.Percentile(5), cdf.Percentile(95)
    return stderr, cdf, ci

def VertLine(x, y=1):
        thinkplot.Plot([x, x], [0, y], color='0.8', linewidth=3)
        
def PlotCDF(cdf, name, ci):
    VertLine(ci[0])
    VertLine(ci[1])
    thinkplot.Cdf(cdf)
    thinkplot.Save(root=name,
                   xlabel='Estimate (L)',
                   ylabel='CDF',
                   title='Sampling distribution',
                   formats=['jpg'])

def PlotN(ns, stderrs):
    thinkplot.Plot(ns, stderrs)
    thinkplot.Save(root="8-2_stderr",
                   xlabel="Sample Size n",
                   ylabel="Standard Error",
                   formats=["jpg"])
                                      
def main():
    thinkstats2.RandomSeed(17)
    ns = [10, 20, 50, 100, 200, 500, 700, 1000]
    stderrs = []
    for num in ns:
        stderr, cdf, ci = Estimate(n=num)
        stderrs.append(stderr)
        if num == 10:
            name = "8-2_estimate%d" %num
            PlotCDF(cdf, name, ci)
            print 'standard error for n=%d:' % num, stderr
            print 'confidence interval:', ci
        print num, stderr, ci
    PlotN(ns, stderrs)

if __name__ == '__main__':
    main()
```
**n=10**  
Plot of estimate L distribution:
![alt text](https://github.com/trishaandrews/dsp/blob/master/statistics/img/8-2_estimate10_small.jpg "Estimate L distribution for n=10")
```
standard error for n=10: 0.896717911545
confidence interval: (1.2901330772324622, 3.8692334892427911)
```
**Increasing n values**  
Plot of standard error vs n:  
![alt text](https://github.com/trishaandrews/dsp/blob/master/statistics/img/8-2_stderr_small.jpg "Standard Error vs n")
```
n     Standard Error   Confidence Interval  
10    0.896717911545   (1.2901330772324622, 3.8692334892427911)  
20    0.528783522831   (1.4287635560452996, 3.0939716416424741)  
50    0.301734042599   (1.6048647229013595, 2.576529353610074)  
100   0.211273665104   (1.7056255693481341, 2.3798521914244186)  
200   0.139693064609   (1.7773552021569714, 2.2377275665415293)  
500   0.083883593127   (1.8549261658789429, 2.1359791048867249)  
700   0.0760130414839  (1.8844422959542795, 2.1376054580619512)  
1000  0.0631416450019  (1.9018265216150141, 2.1115028223983088)  
```
The standard error decreases drastically until roughly n=200, at which point the rate of decrease in standard error slows. By n=1000, the standard error is quite low and the confidence interval is very close to the true λ value, which is 2 in this problem.


