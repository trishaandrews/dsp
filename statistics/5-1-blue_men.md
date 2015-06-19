[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

For Exercise 5.1, given that the distribution of men's heights is roughly normal, with µ = 178 cm and σ = 7.7 cm, we are supposed to determine what percentage of males are between 5'10" and 6'1" and therefore eligible to join the Blue Man Group.

First, I used Google to convert the imperial height requirements into metric, and determined that the Blue Man Group height range is between 177.8 cm and 185.4 cm.

Next, I used the given mu and sigma values along with the 5.1 example code to create a normal distribution of men's heights. I could then use that distribution to calculate the percentage of men who weren't too tall to be Blue Men and the percentage of men who were too short to be Blue Men. The difference between these values is the percent, as a decimal, of men in the eligible height range for being a Blue Man. The resulting value is about 0.3421, so roughly 34.2% of men are capable of becoming Blue Men.
```python
mu = 178
sigma = 7.7
dist = scipy.stats.norm(loc=mu, scale=sigma)

high = dist.cdf(185.4)
low = dist.cdf(177.8)
bluemen = high-low

print bluemen 
```

