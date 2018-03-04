from scipy.stats import pearsonr

"""
Computes the Pearson Correlation Coefficient
Params: x,y, -variables for which it is computed the strength of their linear association
Return : r-pearson correlation
         p - p value
"""
def computePearson(x,y):
    r,p = pearsonr(x,y)
    return r,p

def testPearson():
    age = [43,21,25,42,57,59]
    glucoseLevel = [99,65,79,75,87,81]
    r,p = computePearson(age,glucoseLevel)
    print("Pearson correlation value:",r)
    print("p-value:",p)
	
    if(p<0.05):
	    print("Null hypothesis rejected")
    else:
	    print("Null hypothesis is not rejected")

testPearson()
