import booking.constants as const
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from booking.booking_filtration import BookingFiltration
from booking.booking_report import BookingReport
from prettytable import PrettyTable


class Booking(webdriver.Chrome):
    def __init__(self, driver_path=r";C:\\SeleniumDrivers",
                 teardown=True):  # teardown is disabled
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])  # Disable chrome dev error from cmd
        super(Booking, self).__init__(options=options)  # Pass options as arg
        self.implicitly_wait(15)  # Give every method time to execute
        self.maximize_window()  # Cleaner look for testing

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get(const.BASE_URL)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def change_currency(self, currency=None):
        currency_element = self.find_element(
            By.CSS_SELECTOR, 'button[data-tooltip-text="Choose your currency"]'
        )
        currency_element.click()
        selected_currency_element = self.find_element(
            By.CSS_SELECTOR, f'a[data-modal-header-async-url-param*="selected_currency={currency}"]'
        )
        selected_currency_element.click()

    def select_place_to_go(self, place_to_go):
        search_field = self.find_element(
            By.ID, 'ss'
        )
        search_field.clear()
        search_field.send_keys(place_to_go)

        first_result = self.find_element(
            By.CSS_SELECTOR, 'li[data-i="0"]'
        )

        first_result.click()

    def select_dates(self, check_in_date, check_out_date):
        check_in_element = self.find_element(
            By.CSS_SELECTOR, f'td[data-date="{check_in_date}"]'
        )
        check_in_element.click()
        check_out_element = self.find_element(
            By.CSS_SELECTOR, f'td[data-date="{check_out_date}"]'
        )
        check_out_element.click()

    def select_adults(self, count=1):
        selection_element = self.find_element(
            By.ID, 'xp__guests__toggle'
        )
        selection_element.click()

        while True:
            decrease_adults_element = self.find_element(
                By.CSS_SELECTOR, 'button[aria-label="Decrease number of Adults"]'
            )
            decrease_adults_element.click()
            # If value reaches 1, we should get out of loop
            adults_value_element = self.find_element(
                By.ID, 'group_adults'
            )
            adults_value = adults_value_element.get_attribute('value')  # Should give back number of adults
            if int(adults_value) == 1:
                break

        increase_button_element = self.find_element(
            By.CSS_SELECTOR, 'button[aria-label="Increase number of Adults"]'
        )
        for _ in range(count - 1):
            increase_button_element.click()

    def click_search(self):
        search_button = self.find_element(
            By.CSS_SELECTOR, 'button[type="submit"]'
        )
        search_button.click()

    def handle_cookie_banner(self):
        cookie_button = self.find_element(
            By.ID, 'onetrust-accept-btn-handler'
        )
        cookie_button.click()

    def apply_filtrations(self):  # initialize instance of filtration to avoid too many methods
        filtration = BookingFiltration(driver=self)
        filtration.apply_star_rating(5, 4)

        filtration.sort_price_lowest_first()

    def report_results(self):
        hotel_boxes = self.find_element(
            By.ID, 'search_results_table'
        )
        report = BookingReport(hotel_boxes)
        table = PrettyTable(
            field_names=['Hotel name', 'Hotel price', 'Hotel Score']
        )
        table.add_rows(report.pull_deal_attributes())
        print(table)
