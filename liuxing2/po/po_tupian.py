from selenium.webdriver.common.by import By

from base.base import Base


class Po_3(Base):
    #页面属性
    qiqi1=(By.XPATH,'//*[text()="图片"]')
    qiqi2=(By.ID,"kw")
    qiqi3=(By.XPATH,'//*[@value="百度一下" and @class="s_newBtn"]')
    qiqi4=(By.XPATH,'//*[text()="炸弹"]')
    qiqi5=r'G:\untitled\liuxing2\test_case\picture\tupain.png'
    #页面方法
    def qiqi(self,value,zhi):
        self.click(Po_3.qiqi1)
        self.send_keys(Po_3.qiqi2,value)
        self.click(Po_3.qiqi3)
        self.vilidata1(Po_3.qiqi4,zhi)
        self.jietu(Po_3.qiqi5)

