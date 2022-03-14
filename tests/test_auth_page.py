from pages.auth_page import AuthPage
import time


def test_auth_page(selenium):
    page = AuthPage(selenium)
    page.enter_email("email@gmail.com")
    page.enter_pass("123")
    page.btn_click()

    # != или == будет зависеть от того, верные или неверные данные мы вводим
    assert page.get_relative_link() != '/all_pets', 'login_error'

    time.sleep(4)
