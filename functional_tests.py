from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=chrome_options)

browser = driver
browser.get('http://localhost:8000')

assert 'Congratulations!' in browser.title
print('OK')