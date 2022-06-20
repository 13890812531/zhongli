from selenium.webdriver.common.by import By

from base.base import Base


class Po_1(Base):
    #页面元素属性
    keli1=(By.XPATH,'//*[text()="资讯"]')
    keli2=(By.XPATH,'//*[text()="新闻"]')
    keli3=(By.ID, "app_tooltip")
    keli4=(By.ID,'city_name')
    keli5=(By.ID,'change-city')
    keli6=(By.XPATH,'//*[@mon="col=10&locname=北京&locid=0"]')
    keli7=(By.ID,'city_name')
    keli8=r'G:\untitled\liuxing2\test_case\picture\zixun.png'
    #页面元素操作
    def keli(self,handle_value,zhi,dao):
        self.click(Po_1.keli1)
        self.click(Po_1.keli2)
        self.handles(handle_value)
        self.subiao(Po_1.keli3)
        self.tiaoxia(Po_1.keli4)
        self.click(Po_1.keli5)
        self.click(Po_1.keli6)
        self.vilidate2(Po_1.keli7,zhi,dao)
        self.jietu(Po_1.keli8)
