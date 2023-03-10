from custom_methods import UIHelpers
from selenium.webdriver.common.by import By


class HomePage(UIHelpers):
    base_url = "https://b2c.passport.rt.ru"
    title = (By.CSS_SELECTOR, '.card-container__title')
    post_tab = (By.CSS_SELECTOR, 'div#t-btn-tab-mail')
    post_tab_phone = (By.CSS_SELECTOR, 'div#t-btn-tab-phone')
    post_tab_login = (By.CSS_SELECTOR, 'div#t-btn-tab-login')
    post_tab_ls = (By.CSS_SELECTOR, 'div#t-btn-tab-ls')
    #field_username_phone = (By.CSS_SELECTOR, 'input#username') ??????
    field_username = (By.CSS_SELECTOR, 'input#username')
    field_password = (By.CSS_SELECTOR, 'input#password')
    button_login = (By.CSS_SELECTOR, 'button#kc-login')

    def click_to_element(self, locator):
        self.wait_element_to_be_clickable(locator).click()

    def input_text(self, locator, text):
        self.wait_element_to_be_clickable(locator).send_keys(text)


