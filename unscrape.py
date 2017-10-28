from selenium import webdriver

url = "https://unsplash.com"

driver = webdriver.Firefox(executable_path=r'geckodriver.exe')
driver.get(url)
