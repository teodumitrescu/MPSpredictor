class Pixel:

    def __init__(self, value, groundType, thresholds):
        self.value = value
        self.groundType = groundType
        self.thresholds = thresholds
    
    def fmeans(self):
        lastThreshold = self.thresholds[-1]
        TP = 1 -  max(lastThreshold, self.value)
        FP = self.value - lastThreshold if lastThreshold < self.value else 0
        TN = lastThreshold if lastThreshold < self.value else self.value
        FN = lastThreshold - self.value if lastThreshold > self.value else 0
        return TP / (TP + 0.5 * (FP + FN)) 
