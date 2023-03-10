from hamcrest import assert_that, equal_to

from page_object.login_page import HomePage
# from page_object.page_profile import ProfilePage
from tests.page_object.page_profile import ProfilePage

email_login = 'katya_pmi72@bk.ru'
password = 'qweQWE123'
name = 'Анна'
last_name = 'Иванова'


class TestHomePage:
    def test_login(self, driver):
        home_page = HomePage(driver)
        profile_page = ProfilePage(driver)
        home_page.open(HomePage.base_url)
        home_page.click_to_element(HomePage.post_tab)
        home_page.input_text(HomePage.field_username, email_login)
        home_page.input_text(HomePage.field_password, password)
        home_page.click_to_element(HomePage.button_login)

        assert_that(profile_page.take_text(profile_page.user_name), equal_to(name))
        assert_that(profile_page.take_text(profile_page.user_last_name), equal_to(last_name))
        assert_that(profile_page.take_text(profile_page.user_email), equal_to(email_login))
