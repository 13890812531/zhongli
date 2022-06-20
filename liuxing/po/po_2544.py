from selenium.webdriver.common.by import By
from base.base_page import Base_page

class Po_2544(Base_page):
    #页面元素属性
    ele1 = (By.XPATH, "//*[@id='6']")
    ele2 = (By.XPATH, "//iframe[@scrolling='auto']")
    ele3 = (By.XPATH, "//*[@id='ext-gen1173']")
    ele4 = (By.XPATH, "//*[text()='network_2544']")
    ele5 = (By.XPATH, '//*[@id="radiofield-1036-inputEl"]')
    ele6 = (By.XPATH, '//*[@id="textfield-1048-inputEl"]')
    ele7 = (By.XPATH, '//*[@id="textfield-1048-inputEl"]')
    ele8 = (By.XPATH, '//*[@id="button-1087-btnIconEl"]')
    ele9 = r"G:\untitled\liuxing\test_case\tupian\2544.png"
    #页面元素操作
    def chaozuo2(self,value):
        self.click(Po_2544.ele1)
        self.iframe(Po_2544.ele2)
        self.click(Po_2544.ele3)
        self.click(Po_2544.ele4)
        self.click(Po_2544.ele5)
        self.clear(Po_2544.ele6)
        self.send_keys(Po_2544.ele7,value)
        self.click(Po_2544.ele8)
        self.screenshots(Po_2544.ele9)
        print("-----------------结束-----------------------")




