In this assignment, you should write your code in a **readable** way.

Your function definitions should have **appropriate docstrings**.

# Assignment 7a: Numerals to text

In formal style guides for the English language, it is recommended to spell out singular numbers in full. Applications that follow this guideline have to be able to convert numbers to text in a consistent fashion.

## Part 1

Define a Python dict, `NUM_WORD`, containing numeral-words as values, and the corresponding numerical value as the key associated with the word.

Each numeral-word should be a single word only, without hyphens.

For example:
- 1: one
- 2: two
- ...
- 11: eleven
- 12: twelve
- ...
- 20: twenty
- 30: thirty
- ...
- 90: ninety

## Part 2

A greedy algorithm is an algorithm that makes the optimal choice in each iteration.

We can use a greedy algorithm to convert numbers to text, following these rules:

1. Start from the largest numerical value in NUM_WORD
2. If the number to be converted, `n`, is greater than the current numerical value, subtract the numerical value from `n` until `n` is less than the numerical value.  
   With each subtraction, keep track of the associated word.
Keep a count of the number of subtractions required (alternatively you can also use floor division to determine the count)
4. If `n` is zero, convert each numeral-word and its corresponding count to text and return.
5. Otherwise, if `n` is not yet zero, move to the next numerical value and repeat from Step 2.

For this assignment, we will ignore the English grammatical conventions of requiring commas, "and", and hyphens between some words. This is a common way to approach problems: we often want to solve the main problem first, then add in less salient features after the main requirement is met.

### Example

`93` is broken down to:

- `ninety`: 1
- `three`: 1

Text form: `"ninety three"`

----------

Write a function, `text_numeral(num)` that takes in `num` (a positive integer below 100) and returns a `str` representing `num` in text format.

### Expected output

    >>> text_numeral(15)
    'fifteen'
    >>> text_numeral(29)
    'twenty nine'
    
# Submission

Before submission, run the tests on your final code.
