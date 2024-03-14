from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup

from selenium_utils import wait_for_page_load
from schemas import NikonPreview, ImageURLS

BASE_URL = "https://www.nikonusa.com"


def scrape_nikon_preview(category, driver):
    url = f"{BASE_URL}/en/nikon-products/{category}/index.page"
    driver.get(url)
    wait_for_page_load(driver)

    # Show every camera on single page
    select_element = driver.find_element(By.ID, "nkn-resp-items-per-page")
    select = Select(select_element)
    select.select_by_value("-1")

    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html.parser')
    cameras = soup.find_all('li', class_='nkn-resp-filter-entry')

    validated_data = []
    for camera in cameras:
        url = BASE_URL + camera.find('a', class_='product-detail-link')['href']
        camera_dict = {
            "name": camera.find('span', itemprop='name').text.strip(),
            "price": camera.find('span', itemprop='price').text.strip(),
            "detailed_link": url,
            "category": category,
        }
        NikonPreview.parse_obj(camera_dict)  # validating
        validated_data.append(camera_dict)
    return validated_data


def scrape_camera_images(url, driver):
    driver.get(url)
    wait_for_page_load(driver)
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html.parser')
    image_container = soup.find("ol", class_="carousel-inner")
    images = image_container.find_all("img")
    image_urls = []

    for image in images:
        if 'data-pend-src' in image.attrs:
            image_urls.append(image['data-pend-src'])
        else:
            image_urls.append(image['src'])
    ImageURLS.parse_obj({"images": image_urls})
    return image_urls


def scrape_cameras_specs(url, driver):
    driver.get(url + "#tab-ProductDetail-ProductTabs-TechSpecs")
    wait_for_page_load(driver)
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html.parser')
    specs = soup.find_all("li", class_=["spec-content", "row"])
    result = []
    for spec in specs:
        key = spec.find("h4", class_=["spec-title", "col-sm-6"])
        value = spec.find("div", class_=["specs col-sm-6"])
        result.append({key.text: value.text})
    return result
