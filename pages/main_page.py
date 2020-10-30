from  pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class MainPage(Page):
    IMAGE_INSTAGTAM_LINK = (By.CSS_SELECTOR, 'a[title="Instagram"]')
    IMAGE_LINKEDIN_LINK = (By.CSS_SELECTOR, 'a[title="Linkedin"]')
    IMAGE_TWITTER_LINK = (By.CSS_SELECTOR, 'a[title="Twitter"]')
    IMAGE_FACEBOOK_LINK = (By.CSS_SELECTOR, 'a[title="Facebook"]')

    TITLE = (By.TAG_NAME, 'title')
    def main_open(self):
        self.open_page()

    def view_and_click_network_link(self, network_name):
        if network_name == "Instagram":
            LOCATOR = self.IMAGE_INSTAGTAM_LINK
        elif network_name == 'Facebook':
            LOCATOR = self.IMAGE_FACEBOOK_LINK
        elif network_name == 'LinkedIn':
            LOCATOR = self.IMAGE_LINKEDIN_LINK
        elif network_name == 'Twitter':
            LOCATOR = self.IMAGE_TWITTER_LINK
        else:
            print('Invalid locator, using Instagram')
            LOCATOR = self.IMAGE_INSTAGTAM_LINK
        e = self.wait_for_element_to_appear(*LOCATOR)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", e)
        self.wait_for_element_to_be_clickable_click(*LOCATOR)
        self.driver.wait.until(EC.new_window_is_opened)
        self.driver.switch_to_window(self.driver.window_handles[1])

    def verify_title_text(self, title_text):
        actual_text = self.driver.title
        assert title_text in actual_text, f'Nope, try again. Got {actual_text}, but was waiting for {title_text}'
        self.driver.close()
        self.driver.switch_to_window(self.driver.window_handles[0])