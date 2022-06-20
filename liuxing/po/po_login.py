from selenium.webdriver.common.by import By

from base.base_page import Base_page


class Login(Base_page):
    #页面元素属性
    element=(By.XPATH,'//*[text()="转码"]')
    jietu=r'G:\untitled\liuxing\test_case\tupian\login.png'
    #页面元素操作
    def chaozuo(self,value):
        self.duanyan(Login.element,value)
        self.screenshots(Login.jietu)