import unittest
import distinctSubsequences

class TestSolution(unittest.TestCase):
    
    # EQUIVALENCE PARTITIONING

    def test_case_1(self):
        solution = distinctSubsequences.Solution()
        S = "rabbbit"
        T = "rabbit"
        self.assertEqual(solution.numDistinct(S, T), 3)

    def test_case_2(self):
        solution = distinctSubsequences.Solution()
        S = "babgbag"
        T = "bag"
        self.assertEqual(solution.numDistinct(S, T), 5)

    def test_where_valid_input_strings_with_equal_lengths_with_s_and_t_are_identical(self):
        solution = distinctSubsequences.Solution()
        S = "abc"
        T = "abc"
        self.assertEqual(solution.numDistinct(S, T), 1)
    
    def test_where_valid_input_strings_with_different_lengths_with_s_is_a_substring_of_t(self):
        solution = distinctSubsequences.Solution()
        S = "bc"
        T = "abcd"
        self.assertEqual(solution.numDistinct(S, T), 0)

    def test_where_valid_input_strings_with_different_lengths_with_t_is_a_substring_of_s(self):
        solution = distinctSubsequences.Solution()
        S = "abcd"
        T = "bc"
        self.assertEqual(solution.numDistinct(S, T), 1)

    def test_where_valid_input_strings_with_different_lengths_with_s_and_t_have_common_subsequences(self):
        solution = distinctSubsequences.Solution()
        S = "abcd"
        T = "acd"
        self.assertEqual(solution.numDistinct(S, T), 1)

    def test_where_the_target_string_has_repeated_characters(self):
        solution = distinctSubsequences.Solution()
        S = "abcabc"
        T = "abc"
        self.assertEqual(solution.numDistinct(S, T), 4)

    def test_where_the_target_string_consists_of_a_single_character_that_appears_multiple_times_in_the_source_string(self):
        solution = distinctSubsequences.Solution()
        S = "aaa"
        T = "a"
        self.assertEqual(solution.numDistinct(S, T), 3)

    def test_where_there_are_multiple_occurrences_of_the_target_string_within_the_source_string(self):
        solution = distinctSubsequences.Solution()
        S = "aabb"
        T = "ab"
        self.assertEqual(solution.numDistinct(S, T), 4)

    # BOUNDARY VALUE ANALYSIS

    def test_where_minimum_input_lengths_with_s_and_r_are_identical(self):
        solution = distinctSubsequences.Solution()
        S = "a"
        T = "a"
        self.assertEqual(solution.numDistinct(S, T), 1)   

    def test_where_minimum_input_lengths_with_s_and_r_are_not_identical(self):
        solution = distinctSubsequences.Solution()
        S = "a"
        T = "b"
        self.assertEqual(solution.numDistinct(S, T), 0)   

    def test_where_maximum_input_string_lengths_with_s_and_t_are_identical(self):
        solution = distinctSubsequences.Solution()
        S = "a" * 1000
        T = "a" * 1000
        self.assertEqual(solution.numDistinct(S, T), 1)   

    def test_where_maximum_input_string_lengths_with_s_and_t_are__not_identical(self):
        solution = distinctSubsequences.Solution()
        S = "a" * 1000
        T = "b" * 1000
        self.assertEqual(solution.numDistinct(S, T), 0)

    def test_where_maximum_input_string_lengths_with_s_appears_multiple_times_and_t_is_a_single_character(self):
        solution = distinctSubsequences.Solution()
        S = "a" * 1000
        T = "a"
        self.assertEqual(solution.numDistinct(S, T), 1000)

    def test_where_maximum_input_string_lengths_with_s_is_a_single_character_and_t_appears_multiple_times(self):
        solution = distinctSubsequences.Solution()
        S = "a"
        T = "a" * 1000
        self.assertEqual(solution.numDistinct(S, T), 0)

if __name__ == "__main__":
    unittest.main()
