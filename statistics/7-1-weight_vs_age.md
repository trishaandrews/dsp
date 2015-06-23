[Think Stats Chapter 7 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2008.html#toc70) (weight vs. age)

For Exercise 7.1, we are supposed to characterize the relationship between child birth weight versus mother's age by making a scatter plot, plotting the percentiles of birth weight versus mother's age, and computing Pearson's and Spearman's correlations on the variables.

**Code:**
```python
def ScatterPlot(ages, weights, alpha=1.0, filename="7-1_scatter"):

    thinkplot.Scatter(ages, weights, alpha=alpha)
    thinkplot.Config(xlabel="Mother's Age (years)",
                     ylabel='Birth Weight (lbs)',
                     xlim=[10, 45],
                     ylim=[0, 15],
                     legend=False)

    thinkplot.Save(root=filename, 
                   legend=False,
                   formats=['jpg'])
                   
def BinnedPercentiles(df, filename='7-1_binpercent'):

    bins = np.arange(10, 48, 3)
    indices = np.digitize(df.agepreg, bins)
    groups = df.groupby(indices)

    ages = [group.agepreg.mean() for i, group in groups][1:-1]
    cdfs = [thinkstats2.Cdf(group.totalwgt_lb) for i, group in groups][1:-1]

    thinkplot.PrePlot(3)
    
    for percent in [75, 50, 25]:
        weights = [cdf.Percentile(percent) for cdf in cdfs]
        label = '%dth' % percent
        thinkplot.Plot(ages, weights, label=label)
        
    thinkplot.Save(root=filename,
                   formats=['jpg'],
                   xlabel="Mother's Age (years)",
                   ylabel='Birth Weight (lbs)')

def main():
    
    live, firsts, others = first.MakeFrames()
    live = live.dropna(subset=['agepreg', 'totalwgt_lb'])

    ages = live.agepreg
    weights = live.totalwgt_lb

    ScatterPlot(ages, weights, alpha=0.1)
    BinnedPercentiles(live)
    
    print("Pearson's Corr:", thinkstats2.Corr(ages, weights))
    print("Spearman's Corr:", thinkstats2.SpearmanCorr(ages, weights))
```

To solve this problem, the live birth data is first extracted from the data as a whole. I then plotted the data on a scatter plot in order to check for any easily recognizable relationships between the age and weight variables. Next, I plotted the weight percentiles versus age to help visualize the possible relationships that might be too subtle to recognize in a scatter plot. I finally calculated values for Pearson's and Spearman's correlations in order to quantify the relationship between the age and weight variables.

**Scatter plot:**  
![alt text](https://github.com/trishaandrews/dsp/blob/master/statistics/img/7-1_scatter_small.jpg "7-1 scatter plot")

Judging by the scatter plot, there is minimal relationship between the mother's age and the birth weight. This is because the scatter plot is virtually horizontal.

**Weight percentile plot:**  
![alt text](https://github.com/trishaandrews/dsp/blob/master/statistics/img/7-1_binpercent_small.jpg "7-1 weight percentile plot")

The weight percentiles plot shows a slight increase in birth weight for mothers between the ages of 15 and 25, at which point the birth weights seem to plateau. This indicates that there is a possible non-linear correlation between these variables.

**Correlation values:**
```
Pearson's Corr: 0.0688339703541
Spearman's Corr: 0.0946100410966
```
Pearson's correlation value of 0.07 is quite small. This indicates that either there is little correlation between the values, or that the relationship between them is not linear. Since Spearman's correlation is 0.09, it is likely that there is either a slight non-linear relationship, or, since this value is still quite small, it is possible that there are some outliers that are influencing the data.

