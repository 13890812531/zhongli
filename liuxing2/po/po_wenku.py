from selenium.webdriver.common.by import By

from base.base import Base


class Po_5(Base):
    #元素属性
    qing1=(By.LINK_TEXT,"文库")
    qing2=(By.XPATH,'//*[text()="IT互联网"]')
    qing3=(By.XPATH,'//*[text()="法律经济"]')
    qing4=(By.XPATH, '//*[text()="生活艺术"]')
    qing5=(By.XPATH,'//div/span/div[@class="tag-item"][3]')
    qing6=(By.XPATH,'//div/span/div[@class="tag-item"][1]')
    qing7=(By.XPATH,'//*[@class="btn primary"]')
    #元素方法
    def qing(self,zhi):
        self.click(Po_5.qing1)
        self.click(Po_5.qing2)
        self.click(Po_5.qing3)
        self.click(Po_5.qing4)
        self.tuodong(Po_5.qing5,Po_5.qing6)
        self.vilidata1(Po_5.qing7,zhi)