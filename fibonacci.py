"""Class that provides function(s) related to calcuations of
    Fibonacci numbers.

TODO: Add some additional error handling:
        - How do I handle desiredSequence and ensuring it is an integer.
TODO: Overflow handling?
TODO: Can I cleanup the calculation
"""


class Fibonacci:
    """This class provides Fibonacci sequence information."""

    def __init__(self, desired_sequence):
        """Initialization of the Fibonacci instance.

        Arguments:
            desired_sequence: Fibonacci sequenece to compute a value for.
        """

        self.desired_sequence = desired_sequence

    def calculate(self):
        """Implementation of the calculcation of a Fibonacci value for
            the sequenece of this instance.
        """

        if self.desired_sequence < 0:
            raise TypeError("Negative values are unsupported.")

        if self.desired_sequence == 0:
            return self.desired_sequence

        prev_value = 0
        fibonacci_value = 1

        for _ in range(1, self.desired_sequence):
            swap_value = fibonacci_value
            fibonacci_value += prev_value
            prev_value = swap_value
        else:
            return fibonacci_value
