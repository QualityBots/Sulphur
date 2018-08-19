from selenium import webdriver

browser = webdriver.Safari()
browser.get('http://seleniumhq.org/')
browser.quit()