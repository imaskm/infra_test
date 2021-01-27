import unittest
from main import is_palindrome


class Main(unittest.TestCase):

    def test_is_palindrome_positive_with_integer(self):
        self.assertEqual(is_palindrome(121), True)
        self.assertEqual(is_palindrome(12121), True)

    def test_is_palindrome_negative_with_integer(self):
        self.assertEqual(is_palindrome(12122), False)
        self.assertEqual(is_palindrome(121255), False)

    def test_is_palindrome_negative_with_string(self):
        self.assertEqual(is_palindrome("asdfgh"), False)
        self.assertEqual(is_palindrome("asddsdsfgh"), False)
        self.assertEqual(is_palindrome("ty"), False)

    def test_is_palindrome_positive_with_string(self):
        self.assertEqual(is_palindrome("nitin"), True)
        self.assertEqual(is_palindrome(""), True)
        self.assertEqual(is_palindrome("t"), True)
        self.assertEqual(is_palindrome("tt"), True)


if __name__ == '__main__':
    unittest.main()







