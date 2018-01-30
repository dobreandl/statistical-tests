from scipy.stats import wilcoxon

def computeWilcoxon(x):
    statistic,pvalue = wilcoxon(x)
    return statistic,pvalue

# https://onlinecourses.science.psu.edu/stat414/node/319
	
def testWilcoxon():
    measurement = [35.5,44.5,39.8,33.3,51.4,51.3,30.5,48.9,42.1,40.3,46.8,38.0,40.1,36.8,39.3,65.4,42.6,42.8,59.8,52.4,26.2,60.9,45.6,27.1,47.3,36.6,55.6,45.1,52.2,43.5]
    measurement[:] = [x - 45 for x in measurement]
    w,p = computeWilcoxon(measurement)
    print("w-value:",w)
    print("p-value:",p)

testWilcoxon()
