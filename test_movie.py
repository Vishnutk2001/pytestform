from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import time

@pytest.fixture
def setUp():
    global driver,movie,year,director,distributor,producer,language
    movie = input("enter movie name")
    year = input("enter released year")
    director = input("enter director name")
    distributor = input("enter distributor name")
    producer = input("enter producer name")
    language = input("enter language name")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    yield
    time.sleep(10)
    driver.close()
def test_movie(setUp):
    driver.get("https://iprimedtraining.herokuapp.com/movie.php")
    driver.find_element_by_name("mname").send_keys(movie)
    time.sleep(1)
    driver.find_element_by_name("myear").send_keys(year)
    time.sleep(1)
    driver.find_element_by_name("mdirector").send_keys(director)
    time.sleep(1)
    driver.find_element_by_name("mdist").send_keys(distributor)
    time.sleep(1)
    driver.find_element_by_name("mproducer").send_keys(producer)
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div/div/div[2]/form/table/tbody/tr[6]/td[2]/select/option[1]").click()
    driver.find_element_by_name("subbtn").click()
    time.sleep(5)
