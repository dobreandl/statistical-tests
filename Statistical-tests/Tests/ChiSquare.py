'''
Created on Jan 23, 2018

@author: dobreandragos
'''


from scipy.stats import chisquare, chi2

'''
Computes the chi square value and returns if the null hypothesis should be accepted or not

The acceptance of the hypothesis means that the current values and the expected ones match
for the given accept/reject probability.

Parameters
    ----------
    currentValues : array
        Observed frequencies in each category.
    expectedValues : array
        Expected frequencies in each category. 
    acceptRejectProbability : float
        Value between 0 and 1 which denotes the grade of confidence of accepting/rejecting the
        hypotethis

    Returns
    -------
    chisq : float
        The chi-squared test statistic.
    criticalPoint : float
        The critical point for the data provided and the acceptRejectProbability
    accept: boolean
        Denotes if the hypothesis is accepted or not
'''
def chi_compute(currentValues, expectedValues, acceptRejectProbability):
    degreesOfFreedom = len(currentValues) - 1
    
    criticalPoint = chi2.isf(q=(1 - acceptRejectProbability), df=degreesOfFreedom)
    
    chisq, _ = chisquare(currentValues, expectedValues)
    
    return chisq, criticalPoint, chisq < criticalPoint


'''
Tests for the chi_compute
'''

def test_chi_compute():
    _, _, accepted = chi_compute([28,22], [25,25], 0.95)
    
    assert accepted == True
    
    _, _, accepted = chi_compute([10,40], [25,25], 0.95)
    
    assert accepted == False 

'''
Demonstrates the chi_compute function for testing a coin flip results
'''
def chi_compute_usage_example():
    numberOfFlips = 50 # 50 coins flips
    acceptRejectProbability = 0.95
    currentHeadFlips = 28 # number of flips which resulted into a head result
    
    currentValues = [numberOfFlips - currentHeadFlips, numberOfFlips - currentHeadFlips] # 28 Heads and 22 tails
    expectedValues = [numberOfFlips / 2, numberOfFlips / 2]
    
    chisq, criticalPoint, accepted = chi_compute(currentValues, expectedValues, acceptRejectProbability)
    
    print("ChiSq value: "+ str(chisq) + " critical point: " + str(criticalPoint) + " accepted: "+ str(accepted))
    
    
chi_compute_usage_example()
    
    
    