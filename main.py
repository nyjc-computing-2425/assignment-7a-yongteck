# Write a function to convert numbers to text numerals
import math

def text_numeral(num):
    """
    a function that takes in a number and outputs in spelled out form
    ----------
    int num
        the number to be converted
    ----------
    string output
        the number spelled out        
    """
    nums_r = [i for i in NUM_WORD]
    nums_r.reverse()
    track = []
    for i in nums_r:
        while num >= i:
            num -= i
            track.append(NUM_WORD[i])
        if num == 0:
            break
    if len(track)>1:
        track[0] += " "
    return "".join(track)

    
NUM_WORD = {
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
