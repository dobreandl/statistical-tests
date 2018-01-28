from scipy.stats import spearmanr

'''
Calculates a Spearman rank-order correlation coefficient and the p-value to test for non-correlation.


The p-value roughly indicates the probability of an uncorrelated system producing datasets that have a Spearman correlation at least as extreme as the one computed from these datasets. The p-values are not entirely reliable but are probably reasonable for datasets larger than 500 or so.

Parameters:	
x, y : 1D array_like

Returns:	
corr : float

p-value : float

The two-sided p-value for a hypothesis test whose null hypothesis is that two sets of data are uncorrelated, has same dimension as corr.
'''

def computeSpearman(x,y):
    corr, p_value = spearmanr(x, y)
    return corr, p_value

def testSpearman():
    
    x = [56, 75, 45, 71, 62, 64, 58, 80, 76, 61]
    y = [66, 70, 40, 60, 65, 56, 59, 77, 67, 63]
    corr, p_value = computeSpearman(x,y)
    print (corr)
    print (p_value)

testSpearman()
