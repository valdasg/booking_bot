# This file is going to include methods that will parse
# Specific data from deal boxes
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By


class BookingReport:
    def __init__(self, boxes_section_element: WebElement):
        self.boxes_section_element = boxes_section_element
        self.deal_boxes = self.pull_deal_boxes()

    def pull_deal_boxes(self):
        return self.boxes_section_element.find_elements(
            By.CSS_SELECTOR, 'div[data-testid="property-card"]'
        )

    def pull_deal_attributes(self):
        collection = []
        for i, deal_box in enumerate(self.deal_boxes, start=2):
            # Pulling Hotel names
            hotel_name = deal_box.find_element(
                By.CSS_SELECTOR, 'div[data-testid="title"]'
            ).get_attribute('innerHTML').strip()

            # Pulling prices
            hotel_price = deal_box.find_element(
                By.CSS_SELECTOR, 'span[class="fde444d7ef _e885fdc12"]'
            ).get_attribute('innerHTML').strip().split(';')[1]

            try:
                # Pulling hotel score
                hotel_score = deal_box.find_element(
                     By.XPATH, f'//*[@id="search_results_table"]/div[1]/div/div/div/div[5]/div[{i}]/div[1]/div[2]/div/div[1]/div/div[2]/div/div/div/div/a/span/div/div[1]'
                ).get_attribute('innerHTML').strip()
            except NoSuchElementException:
                hotel_score = ''

            collection.append(
                [hotel_name, hotel_price, hotel_score]
            )
        return collection


