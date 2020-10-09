"""
File name: num_sum.py
Objectives: take in a 4 dgit number and return the sum of the number
Author: ochee
"""

def num_sum(num_str):
    total_sum = 0
    for digit in num_str:
        digit_int = int(digit)
        total_sum += digit_int
    return total_sum


