"""
This module contains a function which takes the input string and
tries to produce a lexicographically smallest palindrome
using the least number of swaps.
"""

from collections import defaultdict
from typing import DefaultDict

def make_palindrome(s: str) -> str | None:
    """
    Takes a string and, if possible, transforms it into a palindrome via swapping the letters.
    Attempts to do the transformation using the least number of swaps.
    Returns the lexicographically smallest palindrome fulfilling the previous criteria.

    :param s: The initial scrambled word, can be a palindrome.
    :return: Returns the resulting palindrome string, or None if it's impossible.
    """

    # Counts the letters of the input string.
    # Returns None if there are more than one odd-numbered letters (palindrome is impossible).
    # Saves the letter which is supposed to be in the center,
    # in the case of odd number of characters.
    letter_counts: DefaultDict[str, int] = defaultdict(int)
    center_letter = "_"
    for letter in s:
        letter_counts[letter] += 1
    odd_count = 0
    for letter in letter_counts:
        if letter_counts[letter] % 2 == 1:
            odd_count += 1
            center_letter = letter
    if odd_count > 1:
        return None

    # Empty or one character string is always a palindrome.
    if len(s) <= 1:
        return s

    arr = list(s)

    # If string length is odd, puts one of the letters with odd count in the center of palindrome.
    # Attempts to produce the lexicographically smallest palindrome.
    if len(s) % 2 == 1:
        if center_letter == arr[len(s) // 2]:
            pass # Odd-numbered letter is already in the center.
        elif center_letter != arr[len(s) // 2]:
            find_pointer = 0
            while find_pointer < len(s):
                if arr[find_pointer] == center_letter and \
                        arr[len(s) - find_pointer - 1] == arr[len(s) // 2]:
                    break
                find_pointer += 1
            if find_pointer == len(s):
                find_pointer = 0
                while find_pointer < len(s):
                    if arr[find_pointer] == center_letter:
                        break
                    find_pointer += 1
            arr[find_pointer], arr[len(s) // 2] = arr[len(s) // 2], arr[find_pointer]

    # Uses the two pointer technique.
    # Start with the beginning and the end of the string.
    # If two letters are equal, go further inside.
    # If they are not equal, attempt to find and swap
    # the corresponding letter somewhere else in the string.
    begin_pointer = 0
    end_pointer = len(s) - 1
    while end_pointer - begin_pointer > 1:
        if arr[begin_pointer] == arr[end_pointer]:
            pass
        elif arr[begin_pointer] < arr[end_pointer]:
            find_pointer = end_pointer - 1
            while arr[begin_pointer] != arr[find_pointer] or \
                    (len(s) %2 == 1 and find_pointer == len(s) // 2):
                find_pointer -= 1
            arr[end_pointer], arr[find_pointer] = arr[find_pointer], arr[end_pointer]
        else:
            find_pointer = begin_pointer + 1
            while arr[end_pointer] != arr[find_pointer] or\
                    (len(s) %2 == 1 and find_pointer == len(s) // 2):
                find_pointer += 1
            arr[begin_pointer], arr[find_pointer] = arr[find_pointer], arr[begin_pointer]
        begin_pointer += 1
        end_pointer -= 1

    return "".join(arr)
