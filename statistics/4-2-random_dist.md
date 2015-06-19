[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

Exercise 4.2 asks to generate 1000 numbers with random.random and plot their PMF and CDF in order to see if the random numbers have a uniform distribution.

Generate 1000 random numbers: 
```python
rans = [random.random() for x in range(1000)]
```
Plot PMF:
```python
ranpmf = thinkstats2.Pmf(rans)
thinkplot.Pmf(ranpmf, linewidth=0.1)
thinkplot.Show(xlabel = "value", ylabel = "probability")
```
![alt text](https://github.com/trishaandrews/dsp/blob/master/statistics/img/4-2_pmf.resized.png "4-2 PMF plot")

Plot CDF:
```python
rancdf = thinkstats2.Cdf(rans)
thinkplot.Cdf(rancdf)
thinkplot.Show(xlabel = "value", ylabel = "CDF")
```
![alt text](https://github.com/trishaandrews/dsp/blob/master/statistics/img/4-2_cdf.resized.png "4-2 CDF plot")

The number of lines makes it difficult to interpret the PMF plot, but the linear slope of the CDF plot shows that the distribution of the random.random numbers is indeed uniform.
