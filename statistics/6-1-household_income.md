[Think Stats Chapter 6 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2007.html#toc60) (household income)

Exercise 6.1 wants us to examine data from a survey on household income. The data lists the number of respondents whose income falls between given household income ranges, so first we must interpolate the data to create a pseudo-sample that  places the same number of respondents in each income range as the original sample, but also distributes them evenly on a log10 scale within each range. It is then possible to calculate the mean, median, skewness, and Pearson's skewness of that pseudo-sample. In this way, we can tell what fraction of households reports a taxable income below the mean. However, interpolation to create the pseudo-sample requires an assumed upper bound on income, so it is also useful to determine how the results depend on that assumed upper bound.

First, I interpolated the data by using the given thinkstats InterpolateSample method.
```python
def InterpolateSample(df, log_upper=6.0):
    # compute the log10 of the upper bound for each range
    df['log_upper'] = np.log10(df.income)

    # get the lower bounds by shifting the upper bound and filling in
    # the first element
    df['log_lower'] = df.log_upper.shift(1)
    df.log_lower[0] = 3.0

    # plug in a value for the unknown upper bound of the highest range
    df.log_upper[41] = log_upper

    # use the freq column to generate the right number of values in
    # each range
    arrays = []
    for _, row in df.iterrows():
        vals = np.linspace(row.log_lower, row.log_upper, row.freq)
        arrays.append(vals)

    # collect the arrays into a single sample
    log_sample = np.concatenate(arrays)
    return log_sample
```
Then, I used that sample to to compute the mean, median, standard deviation, skewness, and Pearson skewness.
```python
def main(lu):
    df = hinc.ReadData()
    log_sample = InterpolateSample(df, log_upper=lu)

    sample = np.power(10, log_sample)
    mean = sample.mean()
    std = sample.std()
    median = thinkstats2.Median(sample)
    cdf = thinkstats2.Cdf(sample)
    print('log_upper =', lu)
    print('mean:', mean)
    print('std:', std)
    print('median:', median)
    print('skewness:', thinkstats2.Skewness(sample))
    print('pearson skewness:', thinkstats2.PearsonMedianSkewness(sample))
    print('fraction of people reporting household income below the mean:', cdf[mean])
```
Results if max income is assumed to be 1,000,000:
```
log_upper = 6
mean: 74278.7075312
std: 93946.9299635
median: 51226.4544789
skewness: 4.94992024443
pearson skewness: 0.736125801914
fraction of people reporting household income below the mean: 0.660005879567
```
**66% of households report income below the mean with max income = 1,000,000**

Results if max income is assumed to be 10,000,000:
```
log_upper = 7
mean: 124267.397222
std: 559608.501374
median: 51226.4544789
skewness: 11.6036902675
pearson skewness: 0.391564509277
fraction of people reporting household income below the mean: 0.856563066521
```
**86% of households report income below the mean with max income = 10,000,000**

When the upper bound income is raised, the mean increases, the standard deviation increases a lot, and the skewness also increases. However, the Pearson skewness actually decreases. This is probably due to the fact that the standard deviation is in the denominator in the Pearson skewness calculation, and the standard deviation increased significantly with the increased maximum income.
