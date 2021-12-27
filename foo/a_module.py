def func():
    print("This is module a.")


class Person():
    def __init__(self, weights, heights):
        self.weights = weights
        self.heights = heights

    def get_bmi(self):
        return self.weights*self.heights
