

from selenium.webdriver.common.by import By

from base.base import Base


class Po(Base):
    #页面元素属性
    keqing1=(By.LINK_TEXT,'网页')
    keqing2=(By.ID,'kw')
    keqing3=(By.ID,'su')
    keqing4=(By.PARTIAL_LINK_TEXT,'游戏《原神》中的5星雷系角色')
    keqing5=(By.XPATH,'//*[@nslog-type="10000204"]')
    keqing6=(By.XPATH, '//*[@rel="nofollow" and @target="_blank"]')
    keqing7=(r'G:\untitled\liuxing2\test_case\picture\page.png')
    #页面元素方法
    def keqing(self,value,handle_value,shijian,element,valu,zhi):
        self.click(Po.keqing1)
        self.send_keys(Po.keqing2,value)
        self.click(Po.keqing3)
        self.click(Po.keqing4)
        self.handles(handle_value)
        self.sleep(shijian)
        self.tiao(Po.keqing5)
        self.texts(Po.keqing6,valu)
        self.vilidate(element,zhi)
        self.jietu(Po.keqing7)




