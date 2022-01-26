from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

browser = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
browser.get('https://google.com')

print(browser.title)
