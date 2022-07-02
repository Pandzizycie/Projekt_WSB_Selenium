from selenium import webdriver
from time import sleep

#otwarcie przegladarki

driver = webdriver.Chrome()
# driver2 = webdriver.Firefox()

#maksymalizacja okna

driver.maximize_window()

#otwarcie strony wp.pl

driver.get("http://www.wp.pl")

sleep(10)

#zamkniecie
driver.quit()

