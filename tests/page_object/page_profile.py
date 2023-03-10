from custom_methods import UIHelpers
from selenium.webdriver.common.by import By


class ProfilePage(UIHelpers):
    user_name = (By.CSS_SELECTOR, 'span.user-name__first-patronymic')
    user_last_name = (By.CSS_SELECTOR, 'span.user-name__last-name')
    user_email = (By.CSS_SELECTOR, 'div:nth-child(2) > div > span.dots-table-item__right > span')

    def take_text(self, xpath=None, css=None):
        self.wait_element_to_be_visibility(xpath, css)
        inside_element = self.get_web_element(xpath, css)
        return inside_element.text
