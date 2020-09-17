class BasicCalculator:
    def __init__(self):
        return

    def sum(self, num1, num2): return num1 + num2

    def sub(self, num1, num2): return num1 - num2

    def mul(self, num1, num2): return num1 * num2

    def div(self, num1, num2): return num1 / num2

class AdvancedCalculator(BasicCalculator):
    def __init__(self):
        return

    def pow(self, num, power):
        foo = num
        while power > 0:
            print(power)
            num *= foo
            power -= 1
        return num

    def square(self, num): return pow(self, num, 2)
    
    def cube(self, num): return pow(self, num, 3)

class ScientificCalculator(AdvancedCalculator):
    def __init__(self):
        return

    def average(self, *nums):
        sum = 0
        count = 0
        for num in nums:
            count += 1
            sum += num
        return int(sum / count)

