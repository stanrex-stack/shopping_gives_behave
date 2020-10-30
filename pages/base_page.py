from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.select import Select
from time import sleep

from features.logger import logger


class Page:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://www.shoppinggives.com/'
        self.driver.wait = WebDriverWait(self.driver, 10)
        self.alerts = Alert(self.driver)

    def open_page(self, url = ''):
        logger.info(f'Opened page {url}')
        self.driver.get(self.base_url + url)

    def click(self, *locator):
        logger.info(f'found element {locator}')
        self.driver.find_element(*locator).click()

    def input(self, text: str, *locator):
        input_field = self.driver.find_element(*locator)
        input_field.send_keys(text)

    def verify_element_text(self, expected_text: str, *locator):
        self.driver.wait.until(EC.visibility_of_element_located(locator))
        actual_text = self.driver.find_element(*locator).text
        assert expected_text in actual_text, f'Expexcted {expected_text}, but got {actual_text}'

    def wait_for_element_to_be_clickable_click(self, *locator, error_message=''):
        element_to_click = self.driver.wait.until(EC.element_to_be_clickable(locator),
                               f'Element NOT clickable by {locator}\n{error_message}')
        try:
            element_to_click.click()
        except WebDriverException:
            sleep(0.3)  # Wait before retry
            element_to_click.click()

    def wait_for_element_to_be_clickable(self, *locator, error_message=''):
        self.driver.wait.until(EC.element_to_be_clickable(locator),
                               f'Element NOT clickable by {locator}\n{error_message}')
        return self.driver.find_element(*locator)

    def wait_for_element_to_appear(self, *locator, error_message=''):
        self.driver.wait.until(EC.visibility_of_element_located(locator),
                               f'Element by {locator} did not appear\n{error_message}')
        return self.driver.find_element(*locator)

    def wait_for_element_to_be_located(self, *locator):
        self.driver.wait.until(EC.presence_of_element_located(locator))
        return self.driver.find_element(*locator)

    def wait_for_all_elements_located(self, *locator):
        sleep(0.5)  # Wait for page to load
        self.driver.wait.until(EC.presence_of_all_elements_located(locator))

    def wait_for_certain_amount_of_elements(self, expected_amount, *locator):
        self.driver.wait.until(lambda driver: len(driver.find_elements(*locator)) == expected_amount)
