import numpy as np
import statistics as stats
import math
import random

class FunctionPicker:
    def function_mean(self, array):
        return np.mean(array)

    def function_geo_mean(self, array):
        return stats.geometric_mean(array)

    def function_harmonic_mean(self, array):
        return stats.harmonic_mean(array)

    def function_square_mean(self, array):
        square_sum = 0

        for value in array:
            square_sum = square_sum + value * value
        
        return math.sqrt(square_sum / len(array))

    def function_min(self, array):
        return min(array)

    def function_max(self, array):
        return max(array)

    def function_median(self, array):
        return stats.median(array)

    def random_applier(self, array, function_number):
        match function_number:
            case 0:
                return self.function_mean(array)
            
            case 1:
                return self.function_geo_mean(array)

            case 2:
                return self.function_harmonic_mean(array)

            case 3:
                return self.function_square_mean(array)

            case 4:
                return self.function_min(array)

            case 5:
                return self.function_max(array)

            case 6:
                return self.function_median(array)

if __name__ == "__main__":
    function_picker = FunctionPicker()
    function_number = random.randint(0, 6)
    print(function_picker.random_applier([0.633333, 0.570588, 0.567427, 0.868627, 0.865466, 0.892157, 0.629412], function_number))