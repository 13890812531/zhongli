from selenium.webdriver.common.by import By

from base.base_page import Base


class Po_smtp(Base):
    #页面属性
    paimeng1=(By.ID,"3")
    paimeng2=(By.XPATH,'//*[@id="ext-gen1730"]/div')
    paimeng3=(By.XPATH,'//*[@id="gridview-1050-record-ext-record-544"]')
    paimeng4=(By.ID,'ext-gen1869')
    paimeng5=(By.XPATH,"//li[text()='out_net8']")
    paimeng6=(By.ID,'gridview-1050-record-ext-record-617')
    paimeng7=(By.XPATH,'//table[@id="combobox-1448-triggerWrap"]/tbody/tr/td/div[@class="x-trigger-index-0 x-form-trigger x-form-arrow-trigger x-form-trigger-first" and @role="button"]')
    paimeng8=(By.XPATH,'//li[text()="smtp"]')
    paimeng9=(By.ID,'tab-1093-btnInnerEl')
    paimeng10=(By.ID,'button-1041-btnIconEl')
    paimeng11=(By.ID,'button-1044-btnIconEl')
    paimeng12=r'G:\untitled\zy_232\picture\smtp_1.png'
    paimeng13=(By.XPATH,'//*[text()="帧速率/数据速率"]')
    paimeng14=r'G:\untitled\zy_232\picture\smtp_2.png'
    paimeng15=(By.XPATH, "//*[text()='导出PCAP文件']")
    #页面操作
    def caozuo10(self,handle_value,time1,time2,zhi):
        self.click(Po_smtp.paimeng1)
        self.handle(handle_value)
        self.double_click(Po_smtp.paimeng2)
        self.double_click(Po_smtp.paimeng3)
        self.click(Po_smtp.paimeng4)
        self.click(Po_smtp.paimeng5)
        self.double_click(Po_smtp.paimeng6)
        self.click(Po_smtp.paimeng7)
        self.click(Po_smtp.paimeng8)
        self.click(Po_smtp.paimeng9)
        self.click(Po_smtp.paimeng10)
        self.click(Po_smtp.paimeng11)
        self.sleep(time1)
        self.jietu(Po_smtp.paimeng12)
        self.click(Po_smtp.paimeng13)
        self.jietu(Po_smtp.paimeng14)
        self.sleep(time2)
        self.alert()
        self.assert1(Po_smtp.paimeng15,zhi)
        self.driver.close()