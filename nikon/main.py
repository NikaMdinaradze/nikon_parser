from selenium import webdriver
from mongo import nikon_collection
import json

from nikon.scrapers import scrape_nikon_preview, scrape_camera_images

driver = webdriver.Chrome()

cameras = []
categories = ["compact-digital-cameras"]
for category in categories:
    cameras_preview = scrape_nikon_preview(category, driver)
    cameras.extend(cameras_preview)

for camera in cameras:
    camera["images"] = scrape_camera_images(camera["detailed_link"], driver)
driver.quit()


def save_as_json():
    for document in cameras:
        with open('nikon_preview.json', 'a') as json_file:
            json.dump(dict(document), json_file, indent=4)
            json_file.write(",\n")


save_as_json()
