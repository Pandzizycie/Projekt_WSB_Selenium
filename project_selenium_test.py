# Import bibliotek
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import unittest
from time import sleep

# DANE TESTOWE
e_mail = "kamaprojekt@wsb.pl"
gender = "female"
name = "Ka"
last_name = "El"
password = "KL123456789!"
invalid_password = "kl"
birth_day = "28"
birth_month = "06"
birth_year = "1985"
address = "Przekichana 1000"
city = "WSB"
postal_code = "15190"
state = "Texas"
phone = "123234234"
alias = "warszawski"


class RegistrationTest(unittest.TestCase):
    def setUp(self):
        # Przygotowanie testu
        # Warunki wstępne testu
        # Otwarcie przeglądarki
        self.driver = webdriver.Chrome()
        # Otwarcie strony
        self.driver.get("http://automationpractice.com")
        # Maksymalizacja okna
        self.driver.maximize_window()
        # Ustawienie bezwarunkowego czekania na elementy przy wyszukiwaniu
        # maks. 10 sekund
        self.driver.implicitly_wait(10)

    def testPasswordTooShort(self):
        # Faktyczny test
        driver = self.driver
        # Kroki
        # 1. Kliknij „Sign in”
        # Szukam elementu
        # self.driver.find_element_by_partial_link_text("Sign in") # Selenium 3
        # Metoda find_element zwraca instancję klasy WebElement
        sign_in_link = driver.find_element(By.PARTIAL_LINK_TEXT, "Sign in")  # Selenium 4
        # Klkiknij element
        sign_in_link.click()
        # 2. Wpisz e-mail
        # Znajdź element
        email_input = driver.find_element(By.ID, "email_create")
        # Zastosuj metodę send_keys() żeby wpisać coś w element
        email_input.send_keys(e_mail)
        # 3. Kliknij przycisk „Create account”
        create_btn = driver.find_element(By.ID, "SubmitCreate")
        create_btn.click()
        # 4. Wybierz płeć
        if gender == "female":
            # kliknij Mrs
            driver.find_element(By.ID, "id_gender2").click()
        else:
            # Kliknij Mr
            driver.find_element(By.ID, "id_gender1").click()
        # 5. Wpisz imię nazwisko
        firstname_input = driver.find_element(By.ID, "customer_firstname")
        firstname_input.send_keys(name)
        lastname_input = driver.find_element(By.ID, "customer_lastname")
        lastname_input.send_keys(last_name)
        # 6. Sprawdź e-mail
        email_check = driver.find_element(By.ID, "email")
        email_expected = e_mail
        # Pobierz mail z pola
        email_fact = email_check.get_attribute("value")
        # Porównaj e-mail oczekiwany z faktycznym
        self.assertEqual(email_expected, email_fact)
        # 7. Wpisz hasło
        password_input = driver.find_element(By.ID, "passwd")
        password_input.send_keys(invalid_password)
        # 8. Wybierz datę urodzenia
        days_s = Select(driver.find_element(By.ID, "days"))
        days_s.select_by_value(birth_day)
        months_s = Select(driver.find_element(By.ID, "months"))
        months_s.select_by_value(str(int(birth_month)))
        years_s = Select(driver.find_element(By.ID, "years"))
        years_s.select_by_value(birth_year)
        # 9. Sprawdź pole "imię"
        address_name_input = driver.find_element(By.ID, "firstname")
        address_name_fact = address_name_input.get_attribute("value")
        # Przewiń do elementu
        address_name_input.location_once_scrolled_into_view
        self.assertEqual(name, address_name_fact)
        # 10. Sprawdź pole nazwisko
        address_lastname_fact = driver.find_element(By.ID, "lastname").get_attribute("value")
        self.assertEqual(last_name, address_lastname_fact)
        # 11. Wpisz adres
        addres_input = driver.find_element(By.ID, "address1")
        addres_input.send_keys(address)
        # 12. Wpisz miasto
        city_input = driver.find_element(By.ID, "city")
        city_input.send_keys(city)
        # 13. Wpisz kod pocztowy
        postal_code_input = driver.find_element(By.ID, "postcode")
        postal_code_input.send_keys(postal_code)
        # 14. Wybierz stan
        state_select = Select(driver.find_element(By.ID, "id_state"))
        state_select.select_by_visible_text(state)
        # 15. Wpisz nr telefonu komórkowego
        phone_input = driver.find_element(By.ID, "phone_mobile")
        phone_input.send_keys(phone)
        # 16. Wpisz alias adresu
        address_alias = driver.find_element(By.ID, "alias")
        address_alias.clear()
        address_alias.send_keys(alias)
        # 17. Kliknij Register
        register_btn = driver.find_element(By.ID, "submitAccount")
        register_btn.click()
        # Oczekiwany rezultat
        info_error_number = driver.find_element(By.XPATH, '//div[@class="alert alert-danger"]/p')
        # Sprawdzamy poprawność komunikatu o liczbie błędów
        self.assertEqual("There is 1 error", info_error_number.text)
        # Sprawdzenie poprawności treści błędu
        error_messages = driver.find_elements(By.XPATH, '//div[@class="alert alert-danger"]//li')
        self.assertEqual("passwd is invalid.", error_messages[0].text, "TRAGEDIA!!!!")
        # Śpij 3 sekundy, żebym widział co się dzieje
        # sleep(3)

    def testNoNameEntered(self):
        # Faktyczny test
        driver = self.driver
        # Kroki
        # 1. Kliknij „Sign in”
        # Szukam elementu
        # self.driver.find_element_by_partial_link_text("Sign in") # Selenium 3
        # Metoda find_element zwraca instancję klasy WebElement
        sign_in_link = driver.find_element(By.PARTIAL_LINK_TEXT, "Sign in")  # Selenium 4
        # Klkiknij element
        sign_in_link.click()
        # 2. Wpisz e-mail
        # Znajdź element
        email_input = driver.find_element(By.ID, "email_create")
        # Zastosuj metodę send_keys() żeby wpisać coś w element
        email_input.send_keys(e_mail)
        # 3. Kliknij przycisk „Create account”
        create_btn = driver.find_element(By.ID, "SubmitCreate")
        create_btn.click()
        # 4. Wybierz płeć
        if gender == "female":
            # kliknij Mrs
            driver.find_element(By.ID, "id_gender2").click()
        else:
            # Kliknij Mr
            driver.find_element(By.ID, "id_gender1").click()
        # 5. Wpisz nazwisko
        lastname_input = driver.find_element(By.ID, "customer_lastname")
        lastname_input.send_keys(last_name)
        # 6. Sprawdź e-mail
        email_check = driver.find_element(By.ID, "email")
        email_expected = e_mail
        # Pobierz mail z pola
        email_fact = email_check.get_attribute("value")
        # Porównaj e-mail oczekiwany z faktycznym
        self.assertEqual(email_expected, email_fact)
        # 7. Wpisz hasło
        password_input = driver.find_element(By.ID, "passwd")
        password_input.send_keys(password)
        # 8. Wybierz datę urodzenia
        days_s = Select(driver.find_element(By.ID, "days"))
        days_s.select_by_value(birth_day)
        months_s = Select(driver.find_element(By.ID, "months"))
        months_s.select_by_value(str(int(birth_month)))
        years_s = Select(driver.find_element(By.ID, "years"))
        years_s.select_by_value(birth_year)
        # 9. Sprawdź pole "imię"
        address_name_input = driver.find_element(By.ID, "firstname")
        address_name_fact = address_name_input.get_attribute("value")
        # Przewiń do elementu
        address_name_input.location_once_scrolled_into_view
        self.assertEqual("", address_name_fact)
        # 10. Sprawdź pole nazwisko
        address_lastname_fact = driver.find_element(By.ID, "lastname").get_attribute("value")
        self.assertEqual(last_name, address_lastname_fact)
        # 11. Wpisz adres
        addres_input = driver.find_element(By.ID, "address1")
        addres_input.send_keys(address)
        # 12. Wpisz miasto
        city_input = driver.find_element(By.ID, "city")
        city_input.send_keys(city)
        # 13. Wpisz kod pocztowy
        postal_code_input = driver.find_element(By.ID, "postcode")
        postal_code_input.send_keys(postal_code)
        # 14. Wybierz stan
        state_select = Select(driver.find_element(By.ID, "id_state"))
        state_select.select_by_visible_text(state)
        # 15. Wpisz nr telefonu komórkowego
        phone_input = driver.find_element(By.ID, "phone_mobile")
        phone_input.send_keys(phone)
        # 16. Wpisz alias adresu
        address_alias = driver.find_element(By.ID, "alias")
        address_alias.clear()
        address_alias.send_keys(alias)
        # 17. Kliknij Register
        register_btn = driver.find_element(By.ID, "submitAccount")
        register_btn.click()
        # Oczekiwany rezultat
        info_error_number = driver.find_element(By.XPATH, '//div[@class="alert alert-danger"]/p')
        # Sprawdzamy poprawność komunikatu o liczbie błędów
        self.assertEqual("There is 1 error", info_error_number.text)
        # Sprawdzenie poprawności treści błędu
        error_messages = driver.find_elements(By.XPATH, '//div[@class="alert alert-danger"]//li')
        self.assertEqual("firstname is required.", error_messages[0].text, "TRAGEDIA!!!!")
        # Śpij 3 sekundy, żebym widział co się dzieje
        # sleep(3)

    def tearDown(self):
        # Zakończenie testu
        # Wyłączenie przeglądarki
        self.driver.quit()
