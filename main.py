from selenium import webdriver
from selenium.webdriver.chrome.options import Options

DRIVER_PATH = './chromedriver'

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

browser = webdriver.Chrome(DRIVER_PATH, chrome_options=options)
browser.get('https://google.com')

print(browser.title)
