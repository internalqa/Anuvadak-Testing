from selenium import webdriver
import unittest
import random
import string
import time
from PagesPM.CreateprojectpagePM import Createprojectpmmixin
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()  
chrome_options.add_argument("--headless")


class login(unittest.TestCase,Createprojectpmmixin):

    qa_username = 'chandanpm@gmail.com'
    qa_username1 = 'admin@reverieincz.com'
    qa_password = 'admin'
    qa_password1 = 'admin1'
    randstring = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))

    @classmethod
    def setUpClass(cls):

        cls.driver = webdriver.Chrome(executable_path="C:\\Users\\taan\\Desktop\\Auto\\Drivers\\chrome\\chromedriver.exe", options=chrome_options)
        #cls.driver = webdriver.Chrome("C:\\Users\\taan\\Desktop\\Auto\\Drivers\\chrome\\chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.get("https://qa-dashboard.reverieinc.com/")
        cls.driver.set_window_size(1920, 1080)

    def test_1_Login_anuvadak(self):
        self.Login_Anuvadak_PM()
    
    def test_2_Delete_Admin_User(self):
        self.Delete_Admin_User_PM()

    def xtest_3_Delete_PM_User(self):
        self.Delete_PM_User_PM()
        self.driver.close()

    @classmethod
    def tearDown(cls):
        print("Test Passed")
        
        
if __name__ == '__main__':
    unittest.main()