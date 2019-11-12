from PopulationMean import mean
from Median import median
from Mode import mode
from Popstd import stddev
from PopVar import Popvar 
class Statistics:
    result = 0

    def __init__(self):
        pass

    def populationmean(self, a):
        self.result = mean(a)
        return self.result

    def popmedian(self, a):
        self.result = median(a)
        return self.result

    def popmode(self, a):
        self.result = mode(a)
        return self.result

    def popstddev(self):
        self.result = stddev()
        return self.result

    def popvariance(self, a):
        self.result = Popvar(a)
        return self.result
