# 4) Think Stats Exercise 8.3

Problem: [Think Stats Chapter 8 Exercise 3](http://greenteapress.com/thinkstats2/html/thinkstats2009.html#toc77)

---

Since the time between goals is roughly exponential in games like hockey and soccer, estimate a team’s goal-scoring rate by observing the number of goals they score in a game.

Write a function to simulate a game by taking a goal-scoring rate, lam, in goals per game, and generating the time between goals until the total time exceeds 1 game. It should return the number of goals scored.

Write another function that simulates many games, stores the estimates of lam, then computes their mean error and RMSE.

Is this way of making an estimate biased? Plot the sampling distribution of the estimates and the 90% confidence interval. What is the standard error? What happens to sampling error for increasing values of lam?

**Code**
```python
def RMSE(estimates, actual):
    e2 = [(estimate-actual)**2 for estimate in estimates]
    mse = np.mean(e2)
    return math.sqrt(mse)
    
def MeanError(estimates, actual):
    errors = [estimate-actual for estimate in estimates]
    return np.mean(errors)
        
def SimulateGame(lam):
    goals = 0
    t = 0
    while True:
        time_between_goals = random.expovariate(lam)
        t += time_between_goals
        if t > 1:
            break
        goals += 1
    # estimated goal-scoring rate is the actual number of goals scored
    return goals

def Estimate(lam=2, m=100000):
    estimates = []
    for i in range(m):
        bigL = SimulateGame(lam)
        estimates.append(bigL)

    rmse = RMSE(estimates, lam)
    mean_e = MeanError(estimates, lam)
    
    pmf = thinkstats2.Pmf(estimates)
    cdf = thinkstats2.Cdf(estimates)
    ci = cdf.Percentile(5), cdf.Percentile(95)
    
    return rmse, mean_e, ci, pmf

def CILine(x, y=0.3):
        thinkplot.Plot([x, x], [0, y], color='0.8', linewidth=3)
 
def PlotHist(pmf, name, ci):
    CILine(ci[0])
    CILine(ci[1])
    thinkplot.Hist(pmf)
    thinkplot.Save(root=name,
                   xlabel='Estimate (L)',
                   ylabel='Probability',
                   title='Sampling distribution',
                   formats=['jpg'])
                   
def main():
    thinkstats2.RandomSeed(17)
    
    print "Varying m values"
    print "m   RMSE L     Mean Error   Confidence Interval"
    games = [10, 100, 1000, 10000, 100000, 1000000]
    for g in games:
        rmse, mean_e, ci, pmf = Estimate(m=g)
        print g, rmse, mean_e, ci
        
    print "\nVarying lam values"
    print "lam  RMSE L   Mean Error  Confidence Interval"
    for l in range(1,11):
        rmse, mean_e, ci, pmf = Estimate(lam=l)
        h_name = "8_3_lam=%d_hist" % l
        PlotHist(pmf, h_name, ci)
        print l, rmse, mean_e, ci
```
**Results**

```
Varying m values
m         RMSE L           Mean Error   Confidence Interval
10        1.37840487521   -0.5          (0, 4)
100       1.37840487521    0.02         (0, 4)
1000      1.34981480211   -0.018        (0, 4)
10000     1.41763888209   -0.0007       (0, 5)
100000    1.4104006523    -0.00381      (0, 5)
1000000   1.41324201749    0.000137     (0, 5)
```
When lambda is fixed at 2, the Standard Error, or RMSE, seems to be approximately 1.41. Since the Mean Error is small, and mostly decreases with an increase in m, this is probably an unbiased estimator.

```
Varying lam values
lam  RMSE L          Mean Error  Confidence Interval
1    1.0023073381    0.00142     (0, 3)
2    1.4091380344   -0.00381     (0, 5)
3    1.73279831487   0.00121     (1, 6)
4    2.00427044083   0.00078     (1, 8)
5    2.2331860648    0.00492     (2, 9)
6    2.44567373131  -0.00532     (2, 10)
7    2.65514406389   0.00361     (3, 12)
8    2.83127356502   0.01187     (4, 13)
9    2.99832119694   0.00963     (4, 14)
10   3.16108525668  -0.01816     (5, 15)
```
Distribution of L estimates and confidence interval for lam = 2 and lam = 10:

![alt text](https://github.com/trishaandrews/dsp/blob/master/statistics/img/8_3_lam2_hist_small.jpg "histogram and ci for lam=2")
![alt text](https://github.com/trishaandrews/dsp/blob/master/statistics/img/8_3_lam10_hist_small.jpg "histogram and ci for lam=10")

When lam values increase, the Standard Error, Mean Error, and the size of the confidence interval all increase.


