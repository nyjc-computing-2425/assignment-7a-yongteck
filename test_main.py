import unittest

from main import *

class TestRun:
    def __init__(self,
                 testcase: unittest.TestCase,
                 ans: any,
                 func: callable,
                 call_args: tuple[any] = tuple()) -> None:
        self.testcase = testcase
        self.func = func
        self.call_args = call_args
        self.ans = ans
        self.result = func(*call_args)
    
    def callstr(self) -> str:
        return (
            f"{self.func.__name__}"
            f"({', '.join(repr(self.call_args) for arg in self.call_args)})"
        )
    
    def test(self) -> None:
        callstr = self.callstr()
        if self.ans is not None:
            self.testcase.assertIsNotNone(
                self.result,
                msg=f"{callstr} returned None"
            )
        self.testcase.assertIsInstance(
            self.result, type(self.ans),
            msg=f"{callstr} returned {type(self.result)}, expected {type(self.ans)}"
        )
        self.testcase.assertEqual(
            self.result, self.ans,
            msg=f"{callstr}: Got {self.result!r}, expected {self.ans!r}"
        )
        # Check docstring
        self.testcase.assertTrue(hasattr(self.func, "__doc__"), msg=f"{callstr} has no docstring")
        self.testcase.assertTrue(self.func.__doc__, msg=f"{callstr} has no docstring")

ans_NUM_WORD = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety"
}


class TestAssignment(unittest.TestCase):

    def test_part1(self):
        for key, word in ans_NUM_WORD.items():
            self.assertIsInstance(word, str,
                                  msg=f"NUM_WORD word {word!r}: Expected str, got {type(word)}")
            self.assertIsInstance(key, int,
                                  msg=f"NUM_WORD key {key!r}: Expected int, got {type(key)}")
            self.assertEqual(ans_NUM_WORD[key], word,
                             msg=f"NUM_WORD value for {key!r}: Expected {ans_NUM_WORD[key]!r}, got {word!r}")

    def test_value15(self):
        case = TestRun(self, ans="fifteen", func=text_numeral, call_args=(15,))
        case.test()

    def test_value29(self):
        case = TestRun(self, ans="twenty nine", func=text_numeral, call_args=(29,))
        case.test()


if __name__ == '__main__':
    import os
    if not os.listdir("autograding"):
        import subprocess
        subprocess.run(["git", "submodule", "update", "--init"])
    unittest.main()
