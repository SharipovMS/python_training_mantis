from selenium import webdriver
from fixture.session import SessionHelper
from fixture.james import JamesHelper
from fixture.signup import SignupHelper
from fixture.mail import MailHelper
from fixture.soap import SoapHelper
from fixture.project import ProjectHelper

class Application:
    def __init__(self, browser, config): #Запуск браузера
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.session = SessionHelper(self)
        self.james = JamesHelper(self)
        self.signup = SignupHelper(self)
        self.email = MailHelper(self)
        self.soap = SoapHelper(self)
        self.project = ProjectHelper(self)
        self.config = config
        self.base_url = config['web']['baseUrl']

    def open_page_add_new(self):
        # Открывает страницу
        wd = self.wd
        wd.get(self.base_url)

    def open_page(self):
        # Открывает страницу
        wd = self.wd
        wd.get(self.base_url)

    def destroy(self):
        self.wd.quit()

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False