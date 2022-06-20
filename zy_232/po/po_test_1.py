from selenium.webdriver.common.by import By
from base.base_page import Base
class Po(Base):
    #页面属性
    keqing1=(By.ID,"1")
    keqing2=(By.XPATH,'//iframe[@scrolling="yes"]')
    keqing3=(By.ID,'ext-gen1150')
    keqing4=(By.XPATH,"//*[text()='out_net1']")
    keqing5=(By.ID,"ext-gen1165")
    keqing6=(By.XPATH,'//*[text()="IPv4"]')
    keqing7=(By.ID,"textfield-1060-inputEl")
    keqing8=(By.ID, 'ext-gen1174')
    keqing9=(By.XPATH,'//*[text()="1G"]')
    keqing10=(By.XPATH,'//*[@id="button-1074-btnIconEl"]')
    keqing11=(By.XPATH,'//iframe[@scrolling="yes"]')
    keqing12=r"G:\untitled\zy_232\picture\out_net1_1.png"
    keqing13=(By.XPATH,'//*[text()="帧速率/数据速率"]')
    keqing14=r"G:\untitled\zy_232\picture\out_net1_2.png"
    keqing15=(By.XPATH,'//*[text()="帧速率/数据速率"]')
    #页面方法
    def caozuo1(self,value1,time1,time2,zhi):
        self.click(Po.keqing1)
        self.iframe(Po.keqing2)
        self.click(Po.keqing3)
        self.click(Po.keqing4)
        self.click(Po.keqing5)
        self.click(Po.keqing6)
        self.send_keys(Po.keqing7,value1)
        self.click(Po.keqing8)
        self.click(Po.keqing9)
        self.click(Po.keqing10)
        self.out_iframe()
        self.iframe(Po.keqing11)
        self.sleep(time1)
        self.jietu(Po.keqing12)
        self.click(Po.keqing13)
        self.jietu(Po.keqing14)
        self.sleep(time2)
        self.alert()
        self.assert1(Po.keqing15,zhi)
        self.out_iframe()
        self.driver.close()









