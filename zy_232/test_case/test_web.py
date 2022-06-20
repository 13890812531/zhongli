from time import sleep
import pytest as pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from common.read_yaml import read_yaml
from po.po_pop3_9 import Po_pop3
from po.po_smtp_10 import Po_smtp
from po.po_test_1 import Po
from po.po_test_2 import Po_2
from po.po_test_3 import Po_3
from po.po_test_4 import Po_4
from po.po_test_5 import Po_5
from po.po_test_6 import Po_6
from po.po_test_7 import Po_7
from po.po_test_8 import Po_8
class Test_web():
    #登录
    # def setup(self):
    #     driver=webdriver.Chrome()
    #     self.driver=driver
    #     driver.maximize_window()
    #     driver.implicitly_wait(10)
    #     driver.get("http://192.168.2.32")
    #     driver.find_element(By.ID,"ext-gen1035").click()
    #     # 切换中英文
    #     driver.find_element(By.XPATH,'//*[@class="x-boundlist-item"]').click()
    #     driver.find_element(By.ID,"username-inputEl").send_keys("JohnSmith")
    #     driver.find_element(By.ID,"password-inputEl").send_keys(123456)
    #     sleep(2)
    #     # 进入首页
    #     driver.find_element(By.ID,"button-1017-btnIconEl").click()
    # 光口1速率
    @pytest.mark.parametrize("data_1",read_yaml("data/test1.yaml"))
    def test_1(self,data_1):
        keqing=Po()
        keqing.caozuo1(data_1["value1"],data_1["time1"],data_1["time2"],data_1["zhi"])
        # self.driver.find_element(By.ID,"1").click()
        # # 进入iframe网页
        # ele1=self.driver.find_element(By.XPATH,'//iframe[@scrolling="yes"]')
        # self.driver.switch_to.frame(ele1)
        # # 选择网络配置
        # self.driver.find_element(By.ID,'ext-gen1150').click()
        # #点击配置
        # self.driver.find_element(By.XPATH,"//*[text()='out_net1']").click()
        # #选择协议
        # self.driver.find_element(By.ID,"ext-gen1165").click()
        # #点击协议
        # self.driver.find_element(By.XPATH,'//*[text()="aIPv4"]').click()
        # #测试时间
        # ele2=self.driver.find_element(By.ID,"textfield-1060-inputEl")
        # ele2.clear()
        # ele2.send_keys(30)
        # #端口速率测试
        # self.driver.find_element(By.ID,'ext-gen1174').click()
        # self.driver.find_element(By.XPATH,'//*[text()="1G"]').click()
        # #运行
        # self.driver.find_element(By.XPATH,'//*[@id="button-1074-btnIconEl"]').click()
        # #退出frame页面
        # self.driver.switch_to.default_content()
        # #进入运行页面
        # frame1=self.driver.find_element(By.XPATH,'//iframe[@scrolling="yes"]')
        # self.driver.switch_to.frame(frame1)
        # sleep(25)
        # #截图1
        # self.driver.get_screenshot_as_file(r"G:\untitled\zy_232\picture\out_net1_1.png")
        # self.driver.find_element(By.XPATH,'//*[text()="帧速率/数据速率"]').click()
        # #截图2
        # self.driver.get_screenshot_as_file(r"G:\untitled\zy_232\picture\out_net1_2.png")
        # sleep(20)
        # #弹出框处理
        # alert=self.driver.switch_to.alert
        # alert.accept()
        # wenben=self.driver.find_element(By.XPATH,'//*[text()="帧速率/数据速率"]')
        # #断言
        # assert wenben.text=='帧速率/数据速率'
        # # 退出运行界面
        # self.driver.switch_to.default_content()
    @pytest.mark.parametrize("data_2",read_yaml("data/test1.yaml"))
    def test_2(self,data_2):
        keli=Po_2()
        keli.caozuo2(data_2["value1"],data_2["time1"],data_2["time2"],data_2["zhi"])
    # #     # self.driver.find_element(By.ID, "1").click()
    # #     # # 进入iframe网页
    # #     # ele1 = self.driver.find_element(By.XPATH, '//iframe[@scrolling="yes"]')
    # #     # self.driver.switch_to.frame(ele1)
    # #     # # 选择网络配置
    # #     # self.driver.find_element(By.ID, 'ext-gen1150').click()
    # #     # # 点击配置
    # #     # self.driver.find_element(By.XPATH, "//*[text()='out_net2']").click()
    # #     # # 选择协议
    # #     # self.driver.find_element(By.ID, "ext-gen1165").click()
    # #     # # 点击协议
    # #     # self.driver.find_element(By.XPATH, '//*[text()="IPv4"]').click()
    # #     # # 测试时间
    # #     # ele2 = self.driver.find_element(By.ID, "textfield-1060-inputEl")
    # #     # ele2.clear()
    # #     # ele2.send_keys(30)
    # #     # # 端口速率测试
    # #     # self.driver.find_element(By.ID, 'ext-gen1174').click()
    # #     # self.driver.find_element(By.XPATH, '//*[text()="1G"]').click()
    # #     # # 运行
    # #     # self.driver.find_element(By.XPATH, '//*[@id="button-1074-btnIconEl"]').click()
    # #     # # 退出frame页面
    # #     # self.driver.switch_to.default_content()
    # #     # # 进入运行页面
    # #     # frame1 = self.driver.find_element(By.XPATH, '//iframe[@scrolling="yes"]')
    # #     # self.driver.switch_to.frame(frame1)
    # #     # sleep(25)
    # #     # # 截图1
    # #     # self.driver.get_screenshot_as_file(r"G:\untitled\zy_232\picture\out_net2_1.png")
    # #     # self.driver.find_element(By.XPATH, '//*[text()="帧速率/数据速率"]').click()
    # #     # # 截图2
    # #     # self.driver.get_screenshot_as_file(r"G:\untitled\zy_232\picture\out_net2_2.png")
    # #     # sleep(20)
    # #     # # 弹出框处理
    # #     # alert = self.driver.switch_to.alert
    # #     # alert.accept()
    # #     # wenben = self.driver.find_element(By.XPATH, '//*[text()="帧速率/数据速率"]')
    # #     # # 断言
    # #     # assert wenben.text == '帧速率/数据速率'
    # #     # # 退出运行界面
    # #     # self.driver.switch_to.default_content()
    #
    # #光口3速率
    @pytest.mark.parametrize("data_3",read_yaml("data/test1.yaml"))
    def test_3(self,data_3):
        zhongli=Po_3()
        zhongli.caozuo3(data_3["value1"],data_3["time1"],data_3["time2"],data_3["zhi"])
    # # #     self.driver.find_element(By.ID, "1").click()
    # # #     # 进入iframe网页
    # # #     ele1 = self.driver.find_element(By.XPATH, '//iframe[@scrolling="yes"]')
    # # #     self.driver.switch_to.frame(ele1)
    # # #     # 选择网络配置
    # # #     self.driver.find_element(By.ID, 'ext-gen1150').click()
    # # #     # 点击配置
    # # #     self.driver.find_element(By.XPATH, "//*[text()='out_net3']").click()
    # # #     # 选择协议
    # # #     self.driver.find_element(By.ID, "ext-gen1165").click()
    # # #     # 点击协议
    # # #     self.driver.find_element(By.XPATH, '//*[text()="IPv4"]').click()
    # # #     # 测试时间
    # # #     ele2 = self.driver.find_element(By.ID, "textfield-1060-inputEl")
    # # #     ele2.clear()
    # # #     ele2.send_keys(30)
    # # #     # 端口速率测试
    # # #     self.driver.find_element(By.ID, 'ext-gen1174').click()
    # # #     self.driver.find_element(By.XPATH, '//*[text()="1G"]').click()
    # # #     # 运行
    # # #     self.driver.find_element(By.XPATH, '//*[@id="button-1074-btnIconEl"]').click()
    # # #     # 退出frame页面
    # # #     self.driver.switch_to.default_content()
    # # #     # 进入运行页面
    # # #     frame1 = self.driver.find_element(By.XPATH, '//iframe[@scrolling="yes"]')
    # # #     self.driver.switch_to.frame(frame1)
    # # #     sleep(25)
    # # #     # 截图1
    # # #     self.driver.get_screenshot_as_file(r"G:\untitled\zy_232\picture\out_net3_1.png")
    # # #     self.driver.find_element(By.XPATH, '//*[text()="帧速率/数据速率"]').click()
    # # #     # 截图2
    # # #     self.driver.get_screenshot_as_file(r"G:\untitled\zy_232\picture\out_net3_2.png")
    # # #     sleep(20)
    # # #     # 弹出框处理
    # # #     alert = self.driver.switch_to.alert
    # # #     alert.accept()
    # # #     wenben = self.driver.find_element(By.XPATH, '//*[text()="帧速率/数据速率"]')
    # # #     # 断言
    # # #     assert wenben.text == '帧速率/数据速率'
    # # #     # 退出运行界面
    # # #     self.driver.switch_to.default_content()
    @pytest.mark.parametrize("data_4",read_yaml("data/test1.yaml"))
    def test_4(self,data_4):
        qiqi=Po_4()
        qiqi.caozuo4(data_4["value1"],data_4["time1"],data_4["time2"],data_4["zhi"])
    @pytest.mark.parametrize("data_5",read_yaml("data/test1.yaml"))
    def test_5(self,data_5):
        xiangling=Po_5()
        xiangling.caozuo5(data_5["value1"],data_5["time1"],data_5["time2"],data_5["zhi"])
    @pytest.mark.parametrize("data_6",read_yaml("data/test1.yaml"))
    def test_6(self,data_6):
        lingguang=Po_6()
        lingguang.caozuo6(data_6["value1"],data_6["time1"],data_6["time2"],data_6["zhi"])
        # lingguang.caozuo6(30,25,20,'帧速率/数据速率')
    @pytest.mark.parametrize("data_7",read_yaml("data/test1.yaml"))
    def test_7(self,data_7):
        qing=Po_7()
        qing.caozuo7(data_7["value1"],data_7["time1"],data_7["time2"],data_7["zhi"])
    @pytest.mark.parametrize("data_8",read_yaml("data/test1.yaml"))
    def test_8(self,data_8):
        shengli=Po_8()
        shengli.caozuo8(data_8["value1"],data_8["time1"],data_8["time2"],data_8["zhi"])
    #pop3协议
    @pytest.mark.parametrize("pop3_9",read_yaml("data/pop3.yaml"))
    def test_pop3(self,pop3_9):
        paimeng=Po_pop3()
        paimeng.caozuo9(pop3_9["handle_value"],pop3_9["time1"],pop3_9["time2"],pop3_9["zhi"])
        # paimeng.caozuo9(1,50,70,"导出PCAP文件")
    #     # #点击应用流量
    #     # self.driver.find_element(By.ID,"3").click()
    #     # #切换窗口句柄
    #     # all_handles=self.driver.window_handles
    #     # self.driver.switch_to.window(all_handles[1])
    #     # #双击测试配置
    #     # element=self.driver.find_element(By.XPATH,'//*[@id="ext-gen1729"]/div')
    #     # ActionChains(self.driver).double_click(element).perform()
    #     # #双击network配置
    #     # element1=self.driver.find_element(By.XPATH,'//*[@id="gridview-1050-record-ext-record-544"]')
    #     # ActionChains(self.driver).double_click(element1).perform()
    #     # #选择network
    #     # self.driver.find_element(By.ID,'ext-gen1869').click()
    #     # self.driver.find_element(By.XPATH,"//li[text()='out_net8']").click()
    #     # #双击appmix配置
    #     # e1=self.driver.find_element(By.ID,'gridview-1050-record-ext-record-617')
    #     # ActionChains(self.driver).double_click(e1).perform()
    #     # #选择appmix
    #     # self.driver.find_element(By.XPATH,'//*[@id="ext-gen1874"]').click()
    #     # self.driver.find_element(By.XPATH,'//li[text()="pop3"]').click()
    #     # #递增/递减
    #     # self.driver.find_element(By.ID,'tab-1093-btnInnerEl').click()
    #     # #保存
    #     # self.driver.find_element(By.ID,'button-1041-btnIconEl').click()
    #     # #运行
    #     # self.driver.find_element(By.ID,'button-1044-btnIconEl').click()
    #     # sleep(50)
    #     # #截图
    #     # self.driver.get_screenshot_as_file(r'G:\untitled\zy_232\picture\pop3_1.png')
    #     # #切换帧数率
    #     # self.driver.find_element(By.XPATH,'//*[text()="帧速率/数据速率"]').click()
    #     # self.driver.get_screenshot_as_file(r'G:\untitled\zy_232\picture\pop3_2.png')
    #     # sleep(70)
    #     # #处理弹出框
    #     # alert=self.driver.switch_to.alert
    #     # alert.accept()
    #     # #导出文件
    #     # a=self.driver.find_element(By.XPATH, "//*[text()='导出PCAP文件']")
    #     # assert a.text=="导出PCAP文件"
    @pytest.mark.parametrize("smtp_10",read_yaml("data/pop3.yaml"))
    def test_smtp(self,smtp_10):
        xing=Po_smtp()
        xing.caozuo10(smtp_10["handle_value"],smtp_10["time1"],smtp_10["time2"],smtp_10["zhi"])
        # xing.caozuo10(1,50,70,"导出PCAP文件")
    #     # #点击应用流量
    #     # self.driver.find_element(By.ID,"3").click()
    #     # #切换窗口句柄
    #     # all_handles=self.driver.window_handles
    #     # self.driver.switch_to.window(all_handles[1])
    #     # #双击测试配置
    #     # ele1=self.driver.find_element(By.XPATH,'//*[@id="ext-gen1730"]/div')
    #     # ActionChains(self.driver).double_click(ele1).perform()
    #     # #双击network配置
    #     # element1=self.driver.find_element(By.XPATH,'//*[@id="gridview-1050-record-ext-record-544"]')
    #     # ActionChains(self.driver).double_click(element1).perform()
    #     # #选择network
    #     # self.driver.find_element(By.ID,'ext-gen1869').click()
    #     # self.driver.find_element(By.XPATH,"//li[text()='out_net8']").click()
    #     # # 双击appmix配置
    #     # e1=self.driver.find_element(By.ID,'gridview-1050-record-ext-record-617')
    #     # ActionChains(self.driver).double_click(e1).perform()
    #     # #选择appmix
    #     # self.driver.find_element(By.XPATH,'//table[@id="combobox-1448-triggerWrap"]/tbody/tr/td/div[@class="x-trigger-index-0 x-form-trigger x-form-arrow-trigger x-form-trigger-first" and @role="button"]').click()
    #     # self.driver.find_element(By.XPATH,'//li[text()="smtp"]').click()
    #     # #递增/递减
    #     # self.driver.find_element(By.ID,'tab-1093-btnInnerEl').click()
    #     # #保存
    #     # self.driver.find_element(By.ID, 'button-1041-btnIconEl').click()
    #     # #运行
    #     # self.driver.find_element(By.ID,'button-1044-btnIconEl').click()
    #     # sleep(50)
    #     # #截图
    #     # self.driver.get_screenshot_as_file(r'G:\untitled\zy_232\picture\smtp_1.png')
    #     # #切换帧数率
    #     # self.driver.find_element(By.XPATH,'//*[text()="帧速率/数据速率"]').click()
    #     # self.driver.get_screenshot_as_file(r'G:\untitled\zy_232\picture\smtp_2.png')
    #     # sleep(70)
    #     # #处理弹出框
    #     # alert=self.driver.switch_to.alert
    #     # alert.accept()
    #     # #导出文件
    #     # a=self.driver.find_element(By.XPATH, "//*[text()='导出PCAP文件']")
    #     # assert a.text=="导出PCAP文件"

# if __name__ == '__main__':
#     Test_web()





