"""
Tests various cases of making palindrome via swaps.
"""

import unittest
from make_palindrome import make_palindrome

class MakePalindromeTestCase(unittest.TestCase):
    """
    Class to unittest various palindrome cases.
    """
    def test_empty_palindrome(self):
        """
        Empty string is already a palindrome.
        :return:
        """
        self.assertEqual(make_palindrome(""), "")

    def test_single_letter_palindrome(self):
        """
        Single letter is already a palindrome.
        :return:
        """
        self.assertEqual(make_palindrome("a"), "a")

    def test_sample_palindrome(self):
        """
        Tests palindrome, provided with the task.
        :return:
        """
        self.assertEqual(make_palindrome("aabb"), "abba")

    def test_failed_palindrome_1(self):
        """
        Unable to make palindrome with two letters with odd count.
        :return:
        """
        self.assertEqual(make_palindrome("ab"), None)

    def test_failed_palindrome_2(self):
        """
        Unable to make palindrome with two letters with odd count.
        :return:
        """
        self.assertEqual(make_palindrome("aaabbb"), None)

    def test_failed_palindrome_3(self):
        """
        Unable to make palindrome with four letters with odd count.
        :return:
        """
        self.assertEqual(make_palindrome("aaaabbbbwxyz"), None)

    def test_already_even_palindrome(self):
        """
        Already a palindrome, returns the same string.
        :return:
        """
        self.assertEqual(make_palindrome("abba"), "abba")

    def test_even_palindrome_1(self):
        """
        Tests even length palindrome.
        :return:
        """
        self.assertEqual(make_palindrome("testtest"), "testtset")

    def test_even_palindrome_2(self):
        """
        Tests even length palindrome.
        :return:
        """
        self.assertEqual(make_palindrome("aaaabbbbcccc"), "aaccbbbbccaa")

    def test_even_palindrome_3(self):
        """
        Tests even length palindrome.
        :return:
        """
        self.assertEqual(make_palindrome("ccababaacc"), "ccaabbaacc")

    def test_already_odd_palindrome(self):
        """
        Already a palindrome, returns the same string.
        :return:
        """
        self.assertEqual(make_palindrome("abcba"), "abcba")

    def test_odd_palindrome_1(self):
        """
        Tests odd length palindrome.
        :return:
        """
        self.assertEqual(make_palindrome("testtestz"), "testztset")

    def test_odd_palindrome_2(self):
        """
        Tests odd length palindrome.
        :return:
        """
        self.assertEqual(make_palindrome("aaaabbbbcccca"), "abacbcacbcaba")

    def test_odd_palindrome_3(self):
        """
        Tests odd length palindrome.
        :return:
        """
        self.assertEqual(make_palindrome("cabaabaca"), "acababaca")

if __name__ == '__main__':
    unittest.main()
