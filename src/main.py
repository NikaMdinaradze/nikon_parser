from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from scrapers import scrape_nikon_preview, scrape_camera_images, scrape_cameras_specs
from chatgpt import generate_description
from utils import save_unique_specifications
from mongo import collection

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
    camera["description"] = generate_description(camera)

driver.quit()

collection.insert_many(cameras)
