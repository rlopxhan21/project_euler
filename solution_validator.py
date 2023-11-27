"""
Module to validate solution by asserting result to expected result
"""


class SolutionValidator:
    """
    Wrapper class that loops through all the test cases and validates it.
    """
    def __init__(self, solution: object, *args) -> None:
        self.solution = solution
        self.no_of_passed_test = 0
        self.no_of_test_case = len(args)

        # Only args and kwargs should be defined in __init__
        test_variable = self.solution.__init__.__code__.co_names

        for index, (test_variable, result) in enumerate(args):
            try:
                print(self.test_validation(index, test_variable, result))
            except TypeError as execption:
                print(execption)

        print(self.test_statistics())

    def test_validation(self, *args):
        """
        Func to assert result and expected result and return passsed or failed
        """
        try:
            # returning func should always be named as main
            result = self.solution(*args[1]).main() or None
        except AttributeError as exception:
            return f"*** AttributeError: {exception}. - Test case {args[0] + 1}"
        except TypeError as exception:
            return f"*** TypeError: {exception} - Test case {args[0] + 1}"

        expected_result = args[2]
        if result == expected_result:
            test_result_message = "+ Passed"
            self.no_of_passed_test += 1
        else:
            test_result_message = "- Failed"

        return f"{test_result_message} - Test Case {args[0] + 1}"

    # pylint: disable=C0116
    def test_statistics(self):
        no_of_failed_test = self.no_of_test_case - self.no_of_passed_test
        return (
            "-------------------------------------- | "
            f"Test Passed: {self.no_of_passed_test}, "
            f"Test Failed: {no_of_failed_test}, "
            f"Total Test Cases: {self.no_of_test_case} "
            "| -------------------------------------- "
            )
