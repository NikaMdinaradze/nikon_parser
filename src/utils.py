from scrapers import scrape_cameras_specs
import json

def get_unique_specifications(cameras, driver):
    unique_specifications = set()
    for camera in cameras:
        specifications = scrape_cameras_specs(camera['detailed_link'], driver)
        for specification in specifications:
            for specification_name in specification:
                unique_specifications.add(specification_name)
    return unique_specifications


def save_as_json(cameras):
    for camera in cameras:
        with open('nikon.json', 'a') as json_file:
            json.dump(dict(camera), json_file, indent=4)
            json_file.write(",\n")

def save_unique_specifications(cameras, driver):
    specifications = get_unique_specifications(cameras, driver)
    with open("nikon_specifications.txt", "w") as f:
        for specification in specifications:
            f.write(f"{specification}\n")
