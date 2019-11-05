from PopulationMean import mean

class Calculator:
    result = 0

    def __init__(self):
        pass

    def populationmean(self, a):
        self.result = mean(a)
        return self.result

