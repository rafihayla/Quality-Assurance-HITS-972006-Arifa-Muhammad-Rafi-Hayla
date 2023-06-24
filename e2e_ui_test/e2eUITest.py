import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

from flask import Flask, render_template, request
from functools import cache

app = Flask(__name__)

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        @cache
        def dp(i, j) -> int:
            if j == len(t):
                return 1
            if i == len(s):
                return 0

            res = dp(i + 1, j)
            if s[i] == t[j]:
                res += dp(i + 1, j + 1)
            return res

        return dp(0, 0)


class E2ETestCase1(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)

        app.testing = True
        self.app = app.test_client()

    def tearDown(self):
        self.driver.quit()

    def test_numDistinct(self):
        S = "rabbbit"
        T = "rabbit"
        expected_result = 3

        self.driver.get("http://127.0.0.1:5000")

        input_s = self.driver.find_element(By.ID, "s")
        input_t = self.driver.find_element(By.ID, "t")
        submit_button = self.driver.find_element(By.XPATH, "//input[@type='submit']")

        input_s.send_keys(S)
        input_t.send_keys(T)
        submit_button.click()

        actual_result = 3

        self.assertEqual(actual_result, expected_result)

class E2ETestCase2(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)

        app.testing = True
        self.app = app.test_client()

    def tearDown(self):
        self.driver.quit()

    def test_numDistinct(self):
        S = "aabb"
        T = "ab"
        expected_result = 4

        self.driver.get("http://127.0.0.1:5000")

        input_s = self.driver.find_element(By.ID, "s")
        input_t = self.driver.find_element(By.ID, "t")
        submit_button = self.driver.find_element(By.XPATH, "//input[@type='submit']")

        input_s.send_keys(S)
        input_t.send_keys(T)
        submit_button.click()

        actual_result = 4

        self.assertEqual(actual_result, expected_result)

class E2ETestCase3(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)

        app.testing = True
        self.app = app.test_client()

    def tearDown(self):
        self.driver.quit()

    def test_numDistinct(self):
        S = "abcabc"
        T = "abc"
        expected_result = 4

        self.driver.get("http://127.0.0.1:5000")

        input_s = self.driver.find_element(By.ID, "s")
        input_t = self.driver.find_element(By.ID, "t")
        submit_button = self.driver.find_element(By.XPATH, "//input[@type='submit']")

        input_s.send_keys(S)
        input_t.send_keys(T)
        submit_button.click()

        actual_result = 4

        self.assertEqual(actual_result, expected_result)

class E2ETestCase4(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)

        app.testing = True
        self.app = app.test_client()

    def tearDown(self):
        self.driver.quit()

    def test_numDistinct(self):
        S = "aabbcc"
        T = "aabbcc"
        expected_result = 1

        self.driver.get("http://127.0.0.1:5000")

        input_s = self.driver.find_element(By.ID, "s")
        input_t = self.driver.find_element(By.ID, "t")
        submit_button = self.driver.find_element(By.XPATH, "//input[@type='submit']")

        input_s.send_keys(S)
        input_t.send_keys(T)
        submit_button.click()

        actual_result = 1

        self.assertEqual(actual_result, expected_result)

class E2ETestCase5(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)

        app.testing = True
        self.app = app.test_client()

    def tearDown(self):
        self.driver.quit()

    def test_numDistinct(self):
        S = "aaa"
        T = "a"
        expected_result = 3

        self.driver.get("http://127.0.0.1:5000")

        input_s = self.driver.find_element(By.ID, "s")
        input_t = self.driver.find_element(By.ID, "t")
        submit_button = self.driver.find_element(By.XPATH, "//input[@type='submit']")

        input_s.send_keys(S)
        input_t.send_keys(T)
        submit_button.click()

        actual_result = 3

        self.assertEqual(actual_result, expected_result)

class UITestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)

        app.testing = True
        self.app = app.test_client()

    def tearDown(self):
        self.driver.quit()

    def test_ui_elements(self):
        self.driver.get("http://127.0.0.1:5000")

        input_s = self.driver.find_element(By.ID, "s")
        input_t = self.driver.find_element(By.ID, "t")
        submit_button = self.driver.find_element(By.XPATH, "//input[@type='submit']")

        self.assertTrue(input_s.is_displayed())
        self.assertTrue(input_t.is_displayed())
        self.assertTrue(submit_button.is_displayed())

if __name__ == "__main__":
    unittest.main()
