[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

The class size paradox is the fact that if you ask students in classes how many students there are in a class, since there are more possible student respondents in larger classes than smaller ones, the data will be biased on the high side. Exercise 3.1 asked to explore the class size paradox as seen through the number of children in a family, so if children were asked how many children are in their household, presumably that data will be biased towards larger families.

In order to explore this phenomenon, I used the Pmf class provided by thinkstats2 to generate a probability mass function from the non-biased data of how many children are in a household. I then used the BiasPmf example code to generate a new pmf that would account for the bias due to the number of possible child respondents for each household. Finally, I used the provided thinkplot module to plot both the actual and biased pmfs and calculated their means with the Mean() method of the thinkstats Pmf class.

The mean for the actual pmf is 1.02 children while the mean for the biased pmf is 2.40 children, which is more than double the actual mean.

Here are both the actual and biased pmfs plotted on the same axes:

![alt text](https://github.com/trishaandrews/dsp/blob/master/statistics/img/3-1.png "3-1 actual and biased pmf")
