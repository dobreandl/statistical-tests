__author__ = 'aenescu'

from scipy.stats import ttest_rel

'''

Parameters:
    a, b : array_like

        The arrays must have the same shape, except in the dimension corresponding to axis (the first, by default).

    axis : int or None, optional

        Axis along which to compute test. If None, compute over the whole arrays, a, and b.

    equal_var : bool, optional

        If True (default), perform a standard independent 2 sample test that assumes equal population variances [R704].
        If False, perform Welchs t-test, which does not assume equal population variance [R705].

New in version 0.11.0.

    nan_policy : {propagate, raise, omit}, optional

        Defines how to handle when input contains nan. propagate returns nan, raise throws an error,
        omit performs the calculations ignoring nan values. Default is propagate.

Returns:
    statistic : float or array

        The calculated t-statistic.

    pvalue : float or array

        The two-tailed p-value.

'''

def paired_compute(a, b):
    t, p = ttest_rel(a, b)

    return t, p


'''
Demonstrates the paired_compute function for testing two sets of marks
'''
def paired_compute_usage_example():
    a = [22, 25, 17, 24, 16, 29, 20, 23, 19, 20, 15, 15, 18, 26, 18, 24, 18, 25, 19, 16]
    b = [18, 21, 16, 22, 19, 24, 17, 21, 23, 18, 14, 16, 16, 19, 18, 20, 12, 22, 15, 17]

    t, p = paired_compute(a, b)

    print("t-value: "+ str(t) + " p-value: " + str(p))


paired_compute_usage_example()
