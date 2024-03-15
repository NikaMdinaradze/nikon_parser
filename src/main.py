from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json

from scrapers import scrape_nikon_preview, scrape_camera_images, scrape_cameras_specs

chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=chrome_options)

cameras = []
categories = ["compact-digital-cameras", "dslr-cameras", "mirrorless-cameras"]
for category in categories:
    cameras_preview = scrape_nikon_preview(category, driver)
    cameras.extend(cameras_preview)

for camera in cameras:
    camera["brand"] = "Nikon"
    camera['images'] = scrape_camera_images(camera["detailed_link"], driver)
    camera['specs'] = scrape_cameras_specs(camera["detailed_link"], driver)
driver.quit()


def save_as_json():
    for camera in cameras:
        with open('nikon_preview.json', 'a') as json_file:
            json.dump(dict(camera), json_file, indent=4)
            json_file.write(",\n")


save_as_json()
