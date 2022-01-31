from selenium import webdriver
import os

screen_path = './full.png'

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")

driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)

driver.get('https://google.com')
driver.save_screenshot(screen_path)

with open('s.txt', 'w', encoding='utf8') as f:
  f.write('hello')

print(driver.title)
