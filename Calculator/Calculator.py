from PopulationMean import mean
from Median import median 
class Calculator:
    result = 0

    def __init__(self):
        pass

    def populationmean(self, a):
        self.result = mean(a)
        return self.result

    def popmedian(self, a):
        self.result = median(a)
        return self.result

