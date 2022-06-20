from selenium.webdriver.common.by import By

from base.base_page import Base


class Po_pop3(Base):
    #页面属性
    paimeng1=(By.ID,"3")
    paimeng2=(By.XPATH,'//*[@id="ext-gen1729"]/div')
    paimeng3=(By.XPATH,'//*[@id="gridview-1050-record-ext-record-544"]')
    paimeng4=(By.ID,'ext-gen1869')
    paimeng5=(By.XPATH,"//li[text()='out_net8']")
    paimeng6=(By.ID,'gridview-1050-record-ext-record-617')
    paimeng7=(By.XPATH,'//*[@id="ext-gen1874"]')
    paimeng8=(By.XPATH,'//li[text()="pop3"]')
    paimeng9=(By.ID,'tab-1093-btnInnerEl')
    paimeng10=(By.ID,'button-1041-btnIconEl')
    paimeng11=(By.ID,'button-1044-btnIconEl')
    paimeng12=r'G:\untitled\zy_232\picture\pop3_1.png'
    paimeng13=(By.XPATH,'//*[text()="帧速率/数据速率"]')
    paimeng14=r'G:\untitled\zy_232\picture\pop3_2.png'
    paimeng15=(By.XPATH, "//*[text()='导出PCAP文件']")
    #页面操作
    def caozuo9(self,handle_value,time1,time2,zhi):
        self.click(Po_pop3.paimeng1)
        self.handle(handle_value)
        self.double_click(Po_pop3.paimeng2)
        self.double_click(Po_pop3.paimeng3)
        self.click(Po_pop3.paimeng4)
        self.click(Po_pop3.paimeng5)
        self.double_click(Po_pop3.paimeng6)
        self.click(Po_pop3.paimeng7)
        self.click(Po_pop3.paimeng8)
        self.click(Po_pop3.paimeng9)
        self.click(Po_pop3.paimeng10)
        self.click(Po_pop3.paimeng11)
        self.sleep(time1)
        self.jietu(Po_pop3.paimeng12)
        self.click(Po_pop3.paimeng13)
        self.jietu(Po_pop3.paimeng14)
        self.sleep(time2)
        self.alert()
        self.assert1(Po_pop3.paimeng15,zhi)
        self.driver.close()









