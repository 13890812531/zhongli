from selenium.webdriver.common.by import By

from base.base_page import Base_page


class Po_3918(Base_page):
    #页面元素属性
    keli1=(By.ID, '8')
    keli2=(By.XPATH, '//iframe[@scrolling="auto"]')
    keli3=(By.ID, "ext-gen1208")
    keli4=(By.XPATH, '//*[text()="network_3918"]')
    keli5=(By.ID, 'button-1087-btnIconEl')
    keli6=(By.XPATH, '//iframe[@scrolling="auto"]')
    keli7=(By.ID, 'tab-1113-btnInnerEl')
    keli8=(By.ID,'fieldset-1103-legendTitle')
    keli9=r'G:\untitled\liuxing\test_case\tupian\3918.png'
    #页面元素操作
    def chaozuo_3918(self,value):
        self.click(Po_3918.keli1)
        self.iframe(Po_3918.keli2)
        self.click(Po_3918.keli3)
        self.click(Po_3918.keli4)
        self.click(Po_3918.keli5)
        self.quite_iframe()
        self.sleep(10)
        self.iframe(Po_3918.keli6)
        self.click(Po_3918.keli7)
        self.duanyan(Po_3918.keli8,value)
        self.screenshots(Po_3918.keli9)