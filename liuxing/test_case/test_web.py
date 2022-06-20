from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import pytest

from base.base_page import Base_page
from po.po_2544 import Po_2544
from po.po_2889 import Po_2889
from po.po_3918 import Po_3918
from po.po_login import Login


class Test_web:
    # def setup(self):
    #     global driver
    #     driver = webdriver.Chrome()
    #     self.driver=driver
    #     self.driver.get("http://192.168.2.243")
    #     self.driver.implicitly_wait(10)
    #     self.driver.find_element(By.ID, "ext-gen1035").click()  # 切换中英文
    #     self.driver.find_element(By.XPATH, "//*[text()='中文']").click()
    #     self.driver.find_element(By.ID, "username-inputEl").send_keys("JohnSmith")  # 账号密码登录
    #     self.driver.find_element(By.ID, "password-inputEl").send_keys(123456)
    #     sleep(2)
    #     self.driver.find_element(By.ID, "button-1017-btnIconEl").click()
    # def teardown(self):
    #     pass
    def test_login(self):
        # 登录模块01****************************
        ls=Login()
        ls.chaozuo("转码")
        # assert ele.text=="转码"
    def test_2544(self):
        # 2544模块02*******************************
        lc=Po_2544()
        lc.chaozuo2(7)
        # assert 1
        # driver.find_element(By.XPATH, "//*[@id='6']").click()  # 点击2544模块
        # iframe1 = driver.find_element(By.XPATH, "//iframe[@scrolling='auto']")  # 切换iframe页面
        # driver.switch_to.frame(iframe1)
        # driver.find_element(By.XPATH, "//*[@id='ext-gen1173']").click()
        # driver.find_element(By.XPATH, "//*[text()='network_2544']").click()
        # driver.find_element(By.XPATH, '//*[@id="radiofield-1036-inputEl"]').click()  # 选择填充负载
        # driver.find_element(By.XPATH, '//*[@id="textfield-1048-inputEl"]').clear()
        # driver.find_element(By.XPATH, '//*[@id="textfield-1048-inputEl"]').send_keys(7)  # 选择时间
        # driver.find_element(By.XPATH, '//*[@id="button-1087-btnIconEl"]').click()  # 点击运行
        # driver.get_screenshot_as_file(r"G:\untitled\liuxing\test_case\tupian\2544.png")
        # sleep(10)
        # iframe2=driver.find_element(By.XPATH,'//iframe[@scrolling="auto"]')#切换结果页面
        # driver.switch_to.frame(iframe2)
        # driver.find_element(By.XPATH,'//*[text()="吞吐量"]').click()#点击吞吐量结果
    def test_2889(self):
        ll=Po_2889()
        ll.chaozuo2889("转发率")
        #2889模块02 ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
        # driver.find_element(By.ID, "7").click()  # 点击2889
        # iframe3 = driver.find_element(By.XPATH, '//iframe[@scrolling="auto"]')  # 切换iframe页面
        # driver.switch_to.frame(iframe3)
        # driver.find_element(By.ID, "tab-1048-btnInnerEl").click()
        # driver.find_element(By.ID, 'ext-gen1127').click()
        # driver.find_element(By.XPATH, '//*[text()="network_2889"]').click()
        # driver.find_element(By.ID, "button-1053-btnIconEl").click()  # 点击运行
        # driver.switch_to.default_content()  # 退出此页面
        # sleep(15)
        # iframe4 = driver.find_element(By.XPATH, '//iframe[@scrolling="auto"]')  # 切换页面
        # driver.switch_to.frame(iframe4)
        # driver.find_element(By.ID, 'tab-1111-btnInnerEl').click()  # 点击吞吐量
        # ele=driver.find_element(By.ID,'tab-1112-btnInnerEl')
        # assert ele.text=="转发率"
        # driver.get_screenshot_as_file(r'G:\untitled\liuxing\test_case\tupian\2889.png')
    def test_3918(self):
        # 3918模块02*******************************
        ll=Po_3918()
        ll.chaozuo_3918("吞吐量")
        # driver.find_element(By.ID, '8').click()  # 点击3918
        # iframe5 = driver.find_element(By.XPATH, '//iframe[@scrolling="auto"]')  # 定位iframe页面
        # driver.switch_to.frame(iframe5)
        # driver.find_element(By.ID, "ext-gen1208").click()  # 选择网络配置
        # driver.find_element(By.XPATH, '//*[text()="network_3918"]').click()
        # driver.find_element(By.ID, 'button-1087-btnIconEl').click()  # 点击运行
        # driver.switch_to.default_content()
        # sleep(10)
        # iframe6 = driver.find_element(By.XPATH, '//iframe[@scrolling="auto"]')  # 切换为运行界面
        # driver.switch_to.frame(iframe6)
        # driver.find_element(By.ID, 'tab-1113-btnInnerEl').click()
        # ele5=driver.find_element(By.ID,'fieldset-1103-legendTitle')
        # assert ele5.text=="吞吐量"
        # driver.get_screenshot_as_file(r'G:\untitled\liuxing\test_case\tupian\3918.png')
