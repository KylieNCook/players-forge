
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

class SeleniumTests(unittest.TestCase):

    def setUp(self):
        chrome_options = Options() 
        chrome_options.add_experimental_option("detach", True)
        chrome_options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(options=chrome_options)

    def test_explore_pages(self):
        driver = self.driver
        driver.get("http://127.0.0.1:5000/") 

        self.assertIn("PlayersForge", driver.title)
        time.sleep(2)

        elem = driver.find_element_by_name("view")
        elem.send_keys(Keys.RETURN)
        time.sleep(2)

        elem = driver.find_element_by_name("download")
        elem.send_keys(Keys.RETURN)
        time.sleep(2)

        elem = driver.find_element_by_name("mods")
        elem.send_keys(Keys.RETURN)
        time.sleep(2)

        elem = driver.find_element_by_name("forums")
        elem.send_keys(Keys.RETURN)
        time.sleep(2)
        
        print("\n SUCCESSFUL FRONTPAGE EXPLORATION ")
    
    def test_signup(self):
        driver = self.driver
        driver.get("http://127.0.0.1:5000/")

        self.assertIn("PlayersForge", driver.title)
        time.sleep(2)

        elem = driver.find_element_by_name("login")
        elem.send_keys(Keys.RETURN)
        time.sleep(2)

        elem = driver.find_element_by_name("signup")
        elem.send_keys(Keys.RETURN)
        time.sleep(2)
        
        elem = driver.find_element_by_id("email")
        elem.send_keys("newuser@gmail.com")
        time.sleep(2)

        elem = driver.find_element_by_id("username")
        elem.send_keys("newuser")
        time.sleep(2)

        elem = driver.find_element_by_id("password")
        elem.send_keys("newuser")
        time.sleep(2)

        elem = driver.find_element_by_name("submit")
        elem.send_keys(Keys.RETURN)
        time.sleep(2)

        print("\n SUCCESSFUL SIGNUP ")

    def test_login(self):
        driver = self.driver
        driver.get("http://127.0.0.1:5000/")

        self.assertIn("PlayersForge", driver.title)
        time.sleep(2)

        elem = driver.find_element_by_name("login")
        elem.send_keys(Keys.RETURN)
        time.sleep(2)

        elem = driver.find_element_by_id("email")
        elem.send_keys("admin")
        time.sleep(2)

        elem = driver.find_element_by_id("password")
        elem.send_keys("admin")
        time.sleep(2)

        elem = driver.find_element_by_name("submit")
        elem.send_keys(Keys.RETURN)
        time.sleep(2)

        print("\n SUCCESSFUL LOGIN ")

    def test_upload(self):
        driver = self.driver
        driver.get("http://127.0.0.1:5000/")

        self.assertIn("PlayersForge", driver.title)
        time.sleep(2)

        elem = driver.find_element_by_name("login")
        elem.send_keys(Keys.RETURN)
        time.sleep(2)

        elem = driver.find_element_by_id("email")
        elem.send_keys("admin")
        time.sleep(2)

        elem = driver.find_element_by_id("password")
        elem.send_keys("admin")
        time.sleep(2)

        elem = driver.find_element_by_name("submit")
        elem.send_keys(Keys.RETURN)
        time.sleep(5)

        elem = driver.find_element_by_name("upload")
        elem.send_keys(Keys.RETURN)
        time.sleep(2)

        elem = driver.find_element_by_id("name")
        elem.send_keys("some mod")
        time.sleep(2)

        elem = driver.find_element_by_id("game")
        elem.send_keys("some game")
        time.sleep(2)

        elem = driver.find_element_by_id("description")
        elem.send_keys("some description")
        time.sleep(2)

        elem = driver.find_element_by_name("inputFile")
        elem.send_keys("C:\\Users\\kylie\\Documents\\sims_4.txt")
        time.sleep(2)

        elem = driver.find_element_by_name("imageFile")
        elem.send_keys("C:\\Users\\kylie\\Pictures\\Screenshots\\Screenshot (1).png")
        time.sleep(2)

        elem = driver.find_element_by_name("submit")
        elem.send_keys(Keys.RETURN)
        time.sleep(2)

        elem = driver.find_element_by_name("profile")
        elem.send_keys(Keys.RETURN)
        time.sleep(5)

        print("\n SUCCESSFUL UPLOAD ")

    def test_loginlogout(self):
        driver = self.driver
        driver.get("http://127.0.0.1:5000/")

        self.assertIn("PlayersForge", driver.title)
        time.sleep(2)

        elem = driver.find_element_by_name("login")
        elem.send_keys(Keys.RETURN)
        time.sleep(2)

        elem = driver.find_element_by_id("email")
        elem.send_keys("admin")
        time.sleep(2)

        elem = driver.find_element_by_id("password")
        elem.send_keys("admin")
        time.sleep(2)

        elem = driver.find_element_by_name("submit")
        elem.send_keys(Keys.RETURN)
        time.sleep(5)

        elem = driver.find_element_by_name("logout")
        elem.send_keys(Keys.RETURN)
        time.sleep(5)

        print("\n SUCCESSFUL LOGIN/LOGOUT ")
        
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()