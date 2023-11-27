"""
---------- PROBLEM STATEMENT -------------
If we list all the natural numbers below 10
that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below given target.
originally the target is 1000.
"""
import sys
sys.path.append("../project_euler")

# pylint: disable=C0413
from solution_validator import SolutionValidator


class Solution:
    """
    -------- MY APPROACH TO SOLVE ----------

    First finding the sum of number using sum formula of arthemetic series
    Find the intersection of two numbers using LCM and subtract it later
    """
    def __init__(self, num1: int, num2: int, target: int) -> None:
        self.num1 = num1
        self.num2 = num2
        self.target = target

    @staticmethod
    # pylint: disable=C0116
    def greatest_common_divisor(num1: int, num2: int) -> int:
        while num2:
            num1, num2 = num2, num1 % num2
        return num1

    @staticmethod
    # pylint: disable=C0116
    def least_common_multiple(num1: int, num2: int) -> int:
        return abs(num1 * num2) // Solution.greatest_common_divisor(num1, num2)

    # pylint: disable=C0116
    def main(self) -> int:
        no_of_terms_of_num1 = (self.target - 1) // self.num1
        sum_of_multiple_of_num1 = (no_of_terms_of_num1 * (self.num1 + no_of_terms_of_num1 * self.num1)) / 2

        no_of_terms_of_num2 = (self.target - 1) // self.num2
        sum_of_multiple_of_num2 = (no_of_terms_of_num2 * (self.num2 + no_of_terms_of_num2 * self.num2)) / 2

        # Sum of multiple of num1 & num2 only when it intersect
        least_common_multiple_value = self.least_common_multiple(self.num1, self.num2)
        number_of_intersection = (self.target - 1) // least_common_multiple_value
        sum_of_intersection = (number_of_intersection * (least_common_multiple_value + number_of_intersection * least_common_multiple_value)) / 2

        return int(sum_of_multiple_of_num1 + sum_of_multiple_of_num2 - sum_of_intersection)


if __name__ == "__main__":
    SolutionValidator(Solution,
                      ((3, 5, 10), 23),
                      ((3, 5, 100), 2318),
                      ((3, 5, 1000), 233168),
                      ((3, 5, 10000), 23331668),
                      )
