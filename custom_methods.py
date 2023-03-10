from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait as Wait


class UIHelpers:
    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def wait_element_to_be_clickable(self, locator):
        return Wait(self.driver, 10).until(EC.element_to_be_clickable(locator))

    def wait_element_to_be_visibility(self, locator):
        return Wait(self.driver, 10).until(EC.visibility_of_element_located(locator))

    def get_web_element(self, xpath=None, css=None):
        if xpath is not None:
            self.driver.find_element_by_xpath(xpath)
        elif css is not None:
            self.driver.find_element_by_css(css)

