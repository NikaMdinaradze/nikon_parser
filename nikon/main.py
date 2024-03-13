from selenium import webdriver
from mongo import nikon_collection
import json

from nikon.scrapers import scrape_nikon_preview

driver = webdriver.Chrome()

cameras = []
categories = ["compact-digital-cameras", "dslr-cameras", "mirrorless-cameras"]
for category in categories:
    cameras_preview = scrape_nikon_preview(category, driver)
    cameras.extend(cameras_preview)

driver.quit()


def save_as_json():
    cursor = nikon_collection.find()
    for document in cursor:
        document['_id'] = str(document['_id'])
        with open('results/nikon_preview.json', 'a') as json_file:
            json.dump(dict(document), json_file, indent=4)
            json_file.write(",\n")
