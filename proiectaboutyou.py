import unittest
from time import sleep

from selenium.common import NoSuchElementException
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
        # element = WebDriverWait(self.chrome, 3).until(EC.visibility_of_element_located(self.FORM_AUTHENTICATION))
        # element.click()
        # element2 = WebDriverWait(self.chrome, 3).until(EC.visibility_of_element_located(self.FORM_AUTHENTICATION2))
        #element2.click()

    def setUpWithoutLoginModal(self):
        self.chrome = webdriver.Chrome(ChromeDriverManager().install())
        self.chrome.maximize_window()
        self.chrome.get("https://www.aboutyou.ro")

    def test_1_verificare_url(self):
        actual_url = self.chrome.current_url
        expected_url = "https://www.aboutyou.ro/magazinul-tau"
        assert actual_url == expected_url

    def test_2_verificare_titlu(self):
        actual_title = self.chrome.title
        expected_title = "Modă online de la mai mult de 1500 branduri de top | ABOUT YOU"
        assert actual_title == expected_title

    def test_3_verificare_text(self):
        element = WebDriverWait(self.chrome, 3).until(EC.visibility_of_element_located(self.FORM_AUTHENTICATION))
        element.click()
        element2 = WebDriverWait(self.chrome, 3).until(EC.visibility_of_element_located(self.FORM_AUTHENTICATION2))
        element2.click()
        h1_element = self.chrome.find_element(By.CSS_SELECTOR, '.jRNzAJ > span:nth-child(1) > span:nth-child(2)')
        h1_text = h1_element.text
        assert h1_text == "Apple"
    def test_4_afisare_buton_login(self):#aici am testat daca butonul de log-in este afisat
        element = WebDriverWait(self.chrome, 3).until(EC.visibility_of_element_located(self.FORM_AUTHENTICATION))
        element.click()
        element2 = WebDriverWait(self.chrome, 3).until(EC.visibility_of_element_located(self.FORM_AUTHENTICATION2))
        element2.click()
        butonul_login = self.chrome.find_element(By.CSS_SELECTOR, "div.sc-3ffazj-1:nth-child(2)") #cauta elementul login
        self.assertTrue(butonul_login.is_displayed())
    def test_5_verificare_href_link(self):
        element = WebDriverWait(self.chrome, 3).until(EC.visibility_of_element_located(self.FORM_AUTHENTICATION))
        element.click()
        element2 = WebDriverWait(self.chrome, 3).until(EC.visibility_of_element_located(self.FORM_AUTHENTICATION2))
        element2.click()
        self.chrome.find_element(By.CSS_SELECTOR, "div.sc-3ffazj-1:nth-child(1)").click()
        self.chrome.implicitly_wait(10)
        expected_url = "https://www.aboutyou.ro/?loginFlow=login"
        assert self.chrome.current_url != expected_url

    def test_6_verificare_capcha(self): #am verificat daca apare mesajul la introducerea gresita a datelor de login
        sleep(1)
        self.chrome.find_element(By.CLASS_NAME, "li167jd").click()
        sleep(2)
        WebDriverWait(self.chrome, 3).until(EC.visibility_of_element_located(self.FORM_AUTHENTICATION2)).click()
        sleep(1)
        self.chrome.find_element(By.CSS_SELECTOR, "div.sc-4wvktd-3:nth-child(1) > label:nth-child(1)").send_keys("aaa@yahoo.com")#am introdus adresa de mail gresita
        sleep(1)
        self.chrome.find_element(By.CSS_SELECTOR, "div.sc-4wvktd-3:nth-child(2) > label:nth-child(1)").send_keys("aaa")#am introdus parola gresita
        sleep(1)
        self.chrome.find_element(By.XPATH, "//span[@class='sc-iprg3j-1 jPkEJg'][normalize-space()='Logare']").click()#am dat click pe login
        sleep(2)
        try:
            self.chrome.find_element(By.XPATH,'//span[contains(text(),"e-mail") and @class="sc-qywjzy-1 kCVWSN"]')
            assert False, "Logarea a fost efectuata, desi nu am bifat capcha"
        except NoSuchElementException:
            print("Logarea nu a putut fi efectuata, fara bifarea capcha")


    def test_7_verificare_buton_x(self): #am verificat daca se poate inchide fereastra de login la apasarea botunului x
        element = WebDriverWait(self.chrome, 3).until(EC.visibility_of_element_located(self.FORM_AUTHENTICATION))
        element.click()
        element2 = WebDriverWait(self.chrome, 3).until(EC.visibility_of_element_located(self.FORM_AUTHENTICATION2))
        element2.click()
        self.chrome.find_element(By.CSS_SELECTOR, "svg.sc-1ahb4we-0:nth-child(2)").click()
        sleep(1)
        try:
            self.chrome.find_element(By.CSS_SELECTOR, "div.sc-3ffazj-1:nth-child(2)")
        except Exception as e:
            print("Nu mai exista butonul de login din modal dupa ce am apasat 'x'")

    def test_8_login_cu_succes(self): #am verificat daca la introducerea datelor corecte se poate loga pe pagina
        sleep(1)
        element = WebDriverWait(self.chrome, 3).until(EC.visibility_of_element_located(self.FORM_AUTHENTICATION))
        element.click()
        element2 = WebDriverWait(self.chrome, 3).until(EC.visibility_of_element_located(self.FORM_AUTHENTICATION2))
        element2.click()
        self.chrome.find_element(By.CSS_SELECTOR, "div.sc-4wvktd-3:nth-child(1) > label:nth-child(1)").send_keys(
            "biancatest@yahoo.com")#am introdus adresa de mail corecta
        self.chrome.find_element(By.CSS_SELECTOR, "div.sc-4wvktd-3:nth-child(2) > label:nth-child(1)").send_keys(
            "parola")#am introdus parola corecta
        self.chrome.find_element(By.CSS_SELECTOR, ".sc-ovefx6-15 > span:nth-child(1)").click()
        sleep(3)
    def test_9_cautare_produs_copii(self): #aici am verificat daca cauta un produs in categoria de copii a paginii
        sleep(1)
        self.chrome.find_element(By.XPATH, "//a[@class='sc-1x1l7vk-1 ichvGd'][normalize-space()='Copii']").click()
        self.chrome.find_element(By.XPATH, "//*[@id='@aboutyou/router::SCROLL_ANCHOR']/div[2]/section/div[2]/section/div[1]/ul/li[1]/a/div[1]/img").click()
        try:
            self.chrome.find_element(By.XPATH, "//img[@alt='Tommy Hilfiger Underwear']")
        except Exception as e:
            print("Brand-ul produsului nu apare pe pagina")
        sleep(2)

    def test_10_schimbare_tara_site(self):#aici am verificat daca se poate schimba tara de origine a site-ului

        # self.chrome.find_element(By.CSS_SELECTOR, "svg.sc-1ahb4we-0:nth-child(2)").click()
        # sleep(1)
        self.chrome.find_element(By.CSS_SELECTOR, ".sc-sjmh1l-4").click()
        sleep(1)
        self.chrome.find_element(By.CSS_SELECTOR, ".sc-8ng12u-6").click()
        sleep(1)
        self.chrome.find_element(By.CSS_SELECTOR, "a.sc-1hnuqjs-3:nth-child(2)").click()
        sleep(2)
        text = self.chrome.find_element(By.CSS_SELECTOR, ".sc-sjmh1l-4").text
        expected = "AT"#am schimbat tara din romania in austria

        assert expected == text