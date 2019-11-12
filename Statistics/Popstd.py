from math import sqrt
from PopulationMean import mean

def stddev():
    """calculates standard deviation"""
    lst = [1, 2, 3, 4, 5, 6]
    sum = 0
    mn = mean(lst)
    for i in lst:
        xbar = i - mn
        xbarsq = xbar*xbar
        #power = pow((lst[i]-mn),2)
        sum = sum + xbarsq
    return sqrt(sum/5)