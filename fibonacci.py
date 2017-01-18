# Class that provides function(s) related to calcuations of
# Fibonacci numbers.
#
# author: R. Cody Erben (erben22@gmail.com)
# date: 01/15/2017
#
# TODO: Study up on Python coding styles and apply here.
# TODO: Add some additional error handling:
#       - How do I handle desiredSequence and ensuring it is an integer.
# TODO: Overflow handling?
# TODO: Can I cleanup the calculation


class Fibonacci:
    def __init__(self, desiredSequence):
        self.desiredSequence = desiredSequence

    def calculate(self):
        prevValue = 0
        fibonacciValue = 1

        for _ in range(1, self.desiredSequence):
            temp = fibonacciValue
            fibonacciValue += prevValue
            prevValue = temp
        else:
            return fibonacciValue
