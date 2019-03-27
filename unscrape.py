import requests
import time
import sys
import pathlib
from selenium import webdriver
from PIL import Image
from io import BytesIO

# Get geckodriver and add to your project folder:
# https://github.com/mozilla/geckodriver/releases/latest

# If you are using this script to scrape Unsplash, please see the Terms & Conditions - https://unsplash.com/terms
# This script was meant as a tutorial/learning project and should only be used as an example
# Therefore, I have altered the website's URLs in this script, use responsibly.

url = "https://some-website-with-photos.com/search/photos/" + sys.argv[1] if len(sys.argv) > 1 else "https://some-website-with-photos.com"
result_folder = "./images-" + sys.argv[1] + "/" if len(sys.argv) > 1 else "./images/"
scroll = (int(sys.argv[2]) if sys.argv[2].isdigit() else 1000) if len(sys.argv) > 2 else 1000
selector = "#gridMulti img"
driver = webdriver.Firefox(executable_path=r'geckodriver.exe')

driver.get(url)
driver.execute_script("window.scrollTo(0,"+str(scroll)+");")
time.sleep(5)
image_elements = driver.find_elements_by_css_selector("#gridMulti img")
pathlib.Path(result_folder).mkdir(parents=True, exist_ok=True)

for image_element in image_elements:
    image_url = image_element.get_attribute("src").split("?")[0]
    image_object = requests.get(image_url)
    image_name = image_url.split("/")[-1]
    image = Image.open(BytesIO(image_object.content))
    image.save(result_folder + image_name + "." + image.format, image.format)

driver.quit()
