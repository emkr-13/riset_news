from selenium import webdriver

FIREFOX_BINARY_PATH = '/usr/bin/firefox'
FIREFOX_DRIVER_PATH = '/snap/bin/geckodriver'

firefox_options = webdriver.FirefoxOptions()
firefox_options.binary_location = FIREFOX_BINARY_PATH

firefox_driver = webdriver.Firefox(executable_path=FIREFOX_DRIVER_PATH, options=firefox_options)

firefox_driver.get('https://www.google.com')
print(firefox_driver.title)

firefox_driver.quit()
