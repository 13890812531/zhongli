from selenium.webdriver.common.by import By
from time import sleep

from base.base_page import Base_page


class Po_2889(Base_page):
    #页面元素属性
    keqing1=(By.ID, "7")
    keqing2=(By.XPATH, '//iframe[@scrolling="auto"]')
    keqing3=(By.ID, "tab-1048-btnInnerEl")
    keqing4=(By.ID, 'ext-gen1127')
    keqing5=(By.XPATH, '//*[text()="network_2889"]')
    keqing6=(By.ID, "button-1053-btnIconEl")
    keqing8=(By.XPATH, '//iframe[@scrolling="auto"]')
    keqing9=(By.ID, 'tab-1111-btnInnerEl')
    keqing10=(By.ID,'tab-1112-btnInnerEl')
    keqing11=r'G:\untitled\liuxing\test_case\tupian\2889.png'
    #页面元素操作
    def chaozuo2889(self,value):
        self.click(Po_2889.keqing1)
        self.iframe(Po_2889.keqing2)
        self.click(Po_2889.keqing3)
        self.click(Po_2889.keqing4)
        self.click(Po_2889.keqing5)
        self.click(Po_2889.keqing6)
        self.quite_iframe()
        sleep(15)
        self.iframe(Po_2889.keqing8)
        self.click(Po_2889.keqing9)
        self.duanyan(Po_2889.keqing10,value)
        self.screenshots(Po_2889.keqing11)
        print("——————————结束——————————")





