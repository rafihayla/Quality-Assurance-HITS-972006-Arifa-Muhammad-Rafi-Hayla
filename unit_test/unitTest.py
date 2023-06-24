import unittest
from ...Assignment import distinctSubsequences

class TestSolution(unittest.TestCase):
    def test_where_there_are_multiple_occurrences_of_the_target_string_within_the_source_string(self):
        solution = distinctSubsequences.Solution()
        S = "aabb"
        T = "ab"
        self.assertEqual(solution.numDistinct(S, T), 4)

    def test_where_the_target_string_has_repeated_characters(self):
        solution = distinctSubsequences.Solution()
        S = "abcabc"
        T = "abc"
        self.assertEqual(solution.numDistinct(S, T), 4)

    def test_where_the_target_string_is_the_same_as_the_source_string(self):
        solution = distinctSubsequences.Solution()
        S = "aabbcc"
        T = "aabbcc"
        self.assertEqual(solution.numDistinct(S, T), 1)

    def test_where_the_target_string_consists_of_a_single_character_that_appears_multiple_times_in_the_source_string(self):
        solution = distinctSubsequences.Solution()
        S = "aaa"
        T = "a"
        self.assertEqual(solution.numDistinct(S, T), 3)

if __name__ == "__main__":
    unittest.main()