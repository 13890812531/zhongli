from selenium.webdriver.common.by import By

from base.base import Base


class Po_2(Base):
    #元素属性
    ganyu1=(By.XPATH,'//*[text()="视频"]')
    ganyu2=(By.LINK_TEXT,"视频")
    ganyu3=(By.XPATH,'//*[@maxlength="255"]')
    ganyu4=(By.XPATH,'//*[@class="search-input-btn"]')
    ganyu5=(By.XPATH,'//*[@class="ant-tabs-tab-active ant-tabs-tab"]')
    ganyu6=r'G:\untitled\liuxing2\test_case\picture\shiping.png'
    #元素方法
    def ganyu(self,shijian,handle_value,value,zhi):
        self.click(Po_2.ganyu1)
        self.sleep(shijian)
        self.click(Po_2.ganyu2)
        self.handles(handle_value)
        self.send_keys(Po_2.ganyu3,value)
        self.click(Po_2.ganyu4)
        self.vilidata1(Po_2.ganyu5,zhi)
        self.jietu(Po_2.ganyu6)



