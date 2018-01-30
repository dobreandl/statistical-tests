from collections import namedtuple
import numpy as np
from scipy.stats import rankdata, distributions

RanksumsResult = namedtuple('RanksumsResult', ('statistic', 'pvalue'))


def ranksums(groupA, groupB):
    """
    Compute the Wilcoxon rank-sum statistic for two samples.
    The Wilcoxon rank-sum test tests the null hypothesis that two sets
    of measurements are drawn from the same distribution.  The alternative
    hypothesis is that values in one sample are more likely to be
    larger than the values in the other sample.
    This test should be used to compare two samples from continuous
    distributions.
    Parameters
    ----------
    groupA,groupB : array_like
        The data from the two samples
    Returns
    -------
    statistic : float
        The test statistic under the large-sample approximation that the
        rank sum statistic is normally distributed
    pvalue : float
        The two-sided p-value of the test
    References
    ----------
    .. [1] http://en.wikipedia.org/wiki/Wilcoxon_rank-sum_test
    """
    groupA, groupB = map(np.asarray, (groupA, groupB))
    n1 = len(groupA)
    n2 = len(groupB)
    alldata = np.concatenate((groupA, groupB))
    ranked = rankdata(alldata)
    groupA = ranked[:n1]
    # s is sum of ranks for smaller group
    s = np.sum(groupA, axis=0)
    # expected is mean rank sum (expected value)
    expected = n1 * (n1 + n2 + 1) / 2.0
    # d is standard deviation
    d = np.sqrt(n1 * n2 * (n1 + n2 + 1) / 12.0)
    # z is test statistic
    z = (s - expected) / d
    prob = 2 * distributions.norm.sf(abs(z))
    return RanksumsResult(z, prob)