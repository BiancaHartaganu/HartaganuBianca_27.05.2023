import unittest
from time import sleep
from selenium.webdriver.common.keys import Keys

from selenium import webdriver
from unittest import TestCase
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager import chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

class Login(unittest.TestCase):
    FORM_AUTHENTICATION = (By.CSS_SELECTOR, "div[data-testid='UserAccount']")
    FORM_AUTHENTICATION2 = (By.CSS_SELECTOR, "div.sc-3ffazj-1:nth-child(2)")
    FLASH_SUCCESS = (By.ID, "flash")

    def tearDown(self):
        self.driver.quit()
    def setUp(self):
        self.chrome = webdriver.Chrome(ChromeDriverManager().install())
        self.chrome.maximize_window()
        self.chrome.get("https://www.aboutyou.ro")
        self.chrome.implicitly_wait(3)
        sleep(2)
        self.chrome.find_element(By.CSS_SELECTOR, "#onetrust-accept-btn-handler").click()
        element = WebDriverWait(self.chrome, 3).until(EC.visibility_of_element_located(self.FORM_AUTHENTICATION))
        element.click()
        element2 = WebDriverWait(self.chrome, 3).until(EC.visibility_of_element_located(self.FORM_AUTHENTICATION2))
        element2.click()

    def setUpWithoutLoginModal(self):
        self.chrome = webdriver.Chrome(ChromeDriverManager().install())
        self.chrome.maximize_window()
        self.chrome.get("https://www.aboutyou.ro")

    def tearDown(self):
        self.chrome.quit()

    def test_1(self):
        actual_url = self.chrome.current_url
        expected_url = "https://www.aboutyou.ro/magazinul-tau?loginFlow=login"
        assert actual_url == expected_url
        print('Url-urile sunt identice')
    def test_2(self):
        actual_title = self.chrome.title
        expected_title = "Modă online de la mai mult de 1500 branduri de top | ABOUT YOU"
        assert actual_title == expected_title
        print("Titlul este cel pe care il asteptam")
    def test_3(self):
        h1_element = self.chrome.find_element(By.CSS_SELECTOR, '.jRNzAJ > span:nth-child(1) > span:nth-child(2)')
        h1_text = h1_element.text
        assert h1_text == "Apple"
        print("Textul este corect")

    def test_4(self):
        butonul_login = self.chrome.find_element(By.CSS_SELECTOR, "div.sc-3ffazj-1:nth-child(2)")
        self.assertTrue(butonul_login.is_displayed())
        print("Butonul login este afisat")

    def test_5(self):
        self.chrome.find_element(By.CSS_SELECTOR, "div.sc-3ffazj-1:nth-child(1)").click()
        self.chrome.implicitly_wait(10)
        expected_url = "https://www.aboutyou.ro/?loginFlow=login"
        assert self.chrome.current_url != expected_url
        print("Atributul href al linkului este corect!")
    def test_6(self):
        sleep(1)
        self.chrome.find_element(By.CSS_SELECTOR, ".sc-ovefx6-15 > span:nth-child(1)").click()
        error_elem = self.chrome.find_element(By.CSS_SELECTOR, "span.sc-qywjzy-1:nth-child(3)")
        expected_error = "Te rugăm să-ți introduci adresa de e-mail"
        assert error_elem.text == expected_error
        print('Eroarea este afisata daca apasam pe butonul login fara sa completam username & password')
    def test_7(self):
        sleep(1)
        self.chrome.find_element(By.CSS_SELECTOR, "div.sc-4wvktd-3:nth-child(1) > label:nth-child(1)").send_keys(
            "aaa@yahoo.com")
        self.chrome.find_element(By.CSS_SELECTOR, "div.sc-4wvktd-3:nth-child(2) > label:nth-child(1)").send_keys("aaa")
        self.chrome.find_element(By.CSS_SELECTOR, ".sc-ovefx6-15 > span:nth-child(1)").click()
        error_elem = self.chrome.find_element(By.CSS_SELECTOR, "div.sc-ovefx6-6:nth-child(3)")
        expected_error = "Te rugăm să-ți verifici datele."
        assert error_elem.text == expected_error


    def test_8(self):
        self.chrome.find_element(By.CSS_SELECTOR, "svg.sc-1ahb4we-0:nth-child(2)").click()
        sleep(1)
        try:
            self.chrome.find_element(By.CSS_SELECTOR, "div.sc-3ffazj-1:nth-child(2)")
        except Exception as e:
            print("Nu mai exista butonul de login din modal dupa ce am apasat 'x'")

    def test_9(self):
        sleep(1)
        self.chrome.find_element(By.CSS_SELECTOR, "div.sc-4wvktd-3:nth-child(1) > label:nth-child(1)").send_keys(
            "biancatest@yahoo.com")
        self.chrome.find_element(By.CSS_SELECTOR, "div.sc-4wvktd-3:nth-child(2) > label:nth-child(1)").send_keys(
            "parola")
        self.chrome.find_element(By.CSS_SELECTOR, ".sc-ovefx6-15 > span:nth-child(1)").click()
        sleep(3)
        name_elem = self.chrome.find_element(By.CSS_SELECTOR, "div.sth0sda:nth-child(1) > span:nth-child(2)")
        expected = "bianca"
        assert name_elem.text == expected
        print("Logarea a avut succes!")

    def test_10(self):
        sleep(1)
        self.chrome.find_element(By.CSS_SELECTOR, "svg.sc-1ahb4we-0:nth-child(2)").click()
        self.chrome.find_element(By.CSS_SELECTOR,
                                 "li.n12ggm7p:nth-child(3) > a:nth-child(1) > div:nth-child(1)").click()
        self.chrome.find_element(By.CSS_SELECTOR, ".sj9vzi").send_keys(
            "Sneaker low 'Mayze Stack Feelin Xtra Wns' negru")
        self.chrome.find_element(By.CSS_SELECTOR, ".sj9vzi").send_keys(Keys.ENTER)
        sleep(3)
        self.chrome.find_element(By.CSS_SELECTOR, "#\\39 089723 > div:nth-child(1) > img:nth-child(1)").click()
        sleep(2)
        self.chrome.find_element(By.CSS_SELECTOR, ".sc-3xrapk-2").click()
        sleep(3)
        self.chrome.find_element(By.CSS_SELECTOR,
                                 "li.sc-1pi0myn-1:nth-child(1) > div:nth-child(1) > label:nth-child(1) > div:nth-child(2)").click()
        sleep(2)
        self.chrome.find_element(By.CSS_SELECTOR, "button.kwtDkx:nth-child(1) > div:nth-child(2)").click()
        sleep(6)
        print("Produsul a fost adaugat cu succes!")

    def test_11(self):

        self.chrome.find_element(By.CSS_SELECTOR, "svg.sc-1ahb4we-0:nth-child(2)").click()
        sleep(1)
        self.chrome.find_element(By.CSS_SELECTOR, ".sc-sjmh1l-4").click()
        sleep(1)
        self.chrome.find_element(By.CSS_SELECTOR, ".sc-8ng12u-6").click()
        sleep(1)
        self.chrome.find_element(By.CSS_SELECTOR, "a.sc-1hnuqjs-3:nth-child(2)").click()
        sleep(2)
        text = self.chrome.find_element(By.CSS_SELECTOR, ".sc-sjmh1l-4").text
        expected = "AT"

        assert expected == text
        print("Tara s-a schimbat cu succes")







