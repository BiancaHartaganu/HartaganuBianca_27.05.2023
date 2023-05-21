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
        self.chrome.quit()
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

    def test_1_verificare_url(self):
        actual_url = self.chrome.current_url
        expected_url = "https://www.aboutyou.ro/magazinul-tau?loginFlow=login"
        assert actual_url == expected_url

    def test_2_verificare_titlu(self):
        actual_title = self.chrome.title
        expected_title = "Modă online de la mai mult de 1500 branduri de top | ABOUT YOU"
        assert actual_title == expected_title

    def test_3_verificare_text(self):
        h1_element = self.chrome.find_element(By.CSS_SELECTOR, '.jRNzAJ > span:nth-child(1) > span:nth-child(2)')
        h1_text = h1_element.text
        assert h1_text == "Apple"


    def test_4_afisare_buton_login(self):#aici am testat daca butonul de log-in este afisat
        butonul_login = self.chrome.find_element(By.CSS_SELECTOR, "div.sc-3ffazj-1:nth-child(2)")
        self.assertTrue(butonul_login.is_displayed())
    def test_5_verificare_href_link(self):
        self.chrome.find_element(By.CSS_SELECTOR, "div.sc-3ffazj-1:nth-child(1)").click()
        self.chrome.implicitly_wait(10)
        expected_url = "https://www.aboutyou.ro/?loginFlow=login"
        assert self.chrome.current_url != expected_url

    def test_6_verificare_date_logare_eroare(self): #am verificat daca apare mesajul la introducerea gresita a datelor de login
        sleep(1)
        self.chrome.find_element(By.CSS_SELECTOR, "div.sc-4wvktd-3:nth-child(1) > label:nth-child(1)").send_keys("aaa@yahoo.com")
        sleep(1)
        self.chrome.find_element(By.CSS_SELECTOR, "div.sc-4wvktd-3:nth-child(2) > label:nth-child(1)").send_keys("aaa")
        sleep(1)
        self.chrome.find_element(By.XPATH, "//span[@class='sc-iprg3j-1 jPkEJg'][normalize-space()='Logare']").click()
        sleep(1)
        #error_elem = self.chrome.find_element(By.XPATH, "//div[@class='sc-ovefx6-6 gCMsSs']")
        expected_error = "Te rugăm să-ți verifici datele."
        sleep(1)
        self.assertEqual(expected_error, "Mesajul nu este cel asteptat")
        #assert error_elem.text == expected_error


    def test_7_verificare_buton_x(self): #am verificat daca se poate inchide fereastra de login la apasarea botunului x
        self.chrome.find_element(By.CSS_SELECTOR, "svg.sc-1ahb4we-0:nth-child(2)").click()
        sleep(1)
        try:
            self.chrome.find_element(By.CSS_SELECTOR, "div.sc-3ffazj-1:nth-child(2)")
        except Exception as e:
            print("Nu mai exista butonul de login din modal dupa ce am apasat 'x'")

    def test_8_login_cu_succes(self): #am verificat daca la introducerea datelor corecte se poate loga pe pagina
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

    def test_9_adaugare_produs_cos(self): #aici am verificat daca se poate adauga un produs in cos
        sleep(1)
        self.chrome.find_element(By.CSS_SELECTOR, "svg.sc-1ahb4we-0:nth-child(2)").click()
        self.chrome.find_element(By.CSS_SELECTOR, "li.n12ggm7p:nth-child(3) > a:nth-child(1) > div:nth-child(1)").click()

        self.chrome.find_element(By.CSS_SELECTOR, ".sj9vzi").send_keys("Sneaker low 'Mayze Stack Feelin Xtra Wns' negru")
        self.chrome.find_element(By.CSS_SELECTOR, ".sj9vzi").send_keys(Keys.ENTER)
        sleep(3)
        self.chrome.find_element(By.CSS_SELECTOR, "#\\39 089723 > div:nth-child(1) > img:nth-child(1)").click()
        sleep(2)
        self.chrome.find_element(By.CSS_SELECTOR, ".sc-3xrapk-2").click()
        sleep(3)
        self.chrome.find_element(By.CSS_SELECTOR, "li.sc-1pi0myn-1:nth-child(1) > div:nth-child(1) > label:nth-child(1) > div:nth-child(2)").click()
        sleep(2)
        self.chrome.find_element(By.CSS_SELECTOR, "button.kwtDkx:nth-child(1) > div:nth-child(2)").click()
        sleep(6)

    def test_10_schimbare_tara_site(self):#aici am verificat daca se poate schimba tara de origine a site-ului

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