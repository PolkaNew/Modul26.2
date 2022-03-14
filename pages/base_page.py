from urllib.parse import urlparse


class BasePage(object):
    # Конструктор класса - специальный метод с ключевым словом __init__
    # Нам нужны объекты веб-драйвера, адрес страницы и время ожидания элементов
    def __init__(self, driver, url, timeout=10):
        self.driver = driver
        self.url = url
        self.driver.implicitly_wait(timeout)

    def get_relative_link(self):
        url = urlparse(self.driver.current_url)
        return url.path
