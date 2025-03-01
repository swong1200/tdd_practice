import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=chrome_options)


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = driver

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_todo_list(self):

# Edith has heard about a cool new online to-do app.
# She goes to check out its homepage
        self.browser.get('http://localhost:8000')

# She notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
# She is invited to enter a to-do item straight away
        self.fail('Finish the test!')
# She types "Buy peacock feathers" into a text box
# (Edith's hobby is tying fly-fishing lures)

# When she hits enter, the page updates, and now the page lists
# "1: Buy peacock feathers" as an item in a to-dp list

# There is still a text box inviting her to add another item.
# She enters "use peacock feathers to make a fly" (Edith is very mehtodical)

# the page updates agina, an dnow shows both items on her lists

# Satisfied, she goes back to sleep

if __name__ == '__main__':
    unittest.main()