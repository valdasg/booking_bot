# This file will include class with instance methods.
# That will be responsible to interact with website
# After we have some results, to apply filters
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class BookingFiltration:
    def __init__(self, driver: WebDriver):  # assign type to enable auto completions, see import of WebDriver
        self.driver = driver

    def apply_star_rating(self, *star_values):  # '*' sets arbitrary argument, allowing multiple arguments
        star_filtration_box = self.driver.find_element(
            By.CSS_SELECTOR, 'div[data-filters-group="class"]'
        )
        star_child_elements = star_filtration_box.find_elements(
            By.CSS_SELECTOR, '*'  # Find all child elements
        )

        for star_value in star_values:  # Allow many args, ex. 5, 4 stars
            for star_element in star_child_elements:  # Loop through child elements and find values == args

                if str(star_element.get_attribute(
                        'data-filters-item')).strip() == f'class:class={star_value}':  # Ex. <h1>Jim</h1> gets Jim,
                    # also convert to string and get rid of spaces
                    star_element.click()

    def sort_price_lowest_first(self):
        element = self.driver.find_element(
            By.CSS_SELECTOR, 'li[data-id="price"]'
        )
        element.click()



