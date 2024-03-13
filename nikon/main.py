from selenium import webdriver

driver = webdriver.Chrome()

# categories = ["mirrorless-cameras"]
# for category in categories:
#     cameras = scrape_nikon_preview(category, driver)
#     nikon_collection.insert_many(cameras)
#
# cursor = nikon_collection.find()
# for document in cursor:
#     document['description'] = scrape_dslr_cameras_description(
#         url=document["detailed_link"],
#         driver=driver
#     )
#     print(document['description'])
print()
driver.quit()

#
# def display_json():
#     cursor = nikon_collection.find()
#     for document in cursor:
#         document['_id'] = str(document['_id'])
#         with open('results/nikon_preview.json', 'a') as json_file:
#             json.dump(dict(document), json_file, indent=4)
#             json_file.write(",\n")
