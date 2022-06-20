from selenium.webdriver.common.by import By

from base.base import Base


class Po_6(Base):
    #元素属性
    baer1=(By.XPATH,'//*[text()="贴吧"]')
    baer2=(By.ID,"wd1")
    baer3=(By.XPATH,'//*[text()="进入贴吧"]')
    baer4=(By.LINK_TEXT,"刻晴吧")
    #元素方法
    def baer(self,value,zhi):
        self.click(Po_6.baer1)
        self.send_keys(Po_6.baer2,value)
        self.click(Po_6.baer3)
        self.vilidata1(Po_6.baer4,zhi)