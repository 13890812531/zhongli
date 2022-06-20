import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from time import sleep

from common.read_yaml import Yaml
from po.po_page import Po
from po.po_shipin import Po_2
from po.po_tieba import Po_6
from po.po_tupian import Po_3
from po.po_wenku import Po_5
from po.po_zhidao import Po_4
from po.po_zixun import Po_1
class Test_web:
    # def setup(self):
    #     # global driver
    #     driver = webdriver.Chrome()
    #     self.driver = driver
    #     driver.get("https://tieba.baidu.com")
    #     driver.implicitly_wait(10)
    @pytest.mark.parametrize("args",Yaml(r"data\page.yaml").read_yaml())
    def test_page(self,args):
        page=Po()
        page.keqing(args["value"],args["handle_value"],args["shijian"],args["element"],args["valu"],args["zhi"])
        # self.driver.find_element(By.LINK_TEXT,'网页').click()#点击网页
        # self.driver.find_element(By.ID,'kw').send_keys("刻晴")
        # self.driver.find_element(By.ID,'su').click()
        # self.driver.find_element(By.PARTIAL_LINK_TEXT,'游戏《原神》中的5星雷系角色').click()
        # all_handles=self.driver.window_handles
        # self.driver.switch_to.window(all_handles[1])
        # sleep(2)
        # ele=self.driver.find_element(By.XPATH,'//*[@nslog-type="10000204"]')
        # self.driver.execute_script('arguments[0].scrollIntoView();', ele)
        # ll=self.driver.find_elements(By.XPATH, '//*[@rel="nofollow" and @target="_blank"]')[0]
        # el=ll.text
        # print(ll.text)
        # assert 1==1
        # self.driver.get_screenshot_as_file(r'G:\untitled\liuxing2\test_case\picture\page.png')
    @pytest.mark.parametrize("keqing",Yaml(r"data\zuxun.yaml").read_yaml())
    def test_zixun(self,keqing):
        ll=Po_1()
        ll.keli(keqing["handle_value"],keqing["zhi"],keqing["dao"])
        # self.driver.find_element(By.XPATH,'//*[text()="资讯"]').click()
        # self.driver.find_element(By.XPATH,'//*[text()="新闻"]').click()
        # all_handles=self.driver.window_handles
        # self.driver.switch_to.window(all_handles[1])
        # ele=self.driver.find_element(By.ID,"app_tooltip")
        # ActionChains(self.driver).move_to_element(ele).perform()
        # ele1=self.driver.find_element(By.ID,'city_name')
        # self.driver.execute_script('arguments[0].scrollIntoView(false);', ele1)
        # self.driver.find_element(By.ID,'change-city').click()
        # self.driver.find_element(By.XPATH,'//*[@mon="col=10&locname=北京&locid=0"]').click()
        # ele3=self.driver.find_element(By.ID,'city_name').text
        # assert ele3 == "成都新闻"
        # self.driver.get_screenshot_as_file(r'G:\untitled\liuxing2\test_case\picture\zixun.png')
    @pytest.mark.parametrize("ganyu",Yaml(r"data\shipin.yaml").read_yaml())
    def test_shipin(self,ganyu):
        ganyu1=Po_2()
        ganyu1.ganyu(ganyu["shijian"],ganyu["handle_value"],ganyu["value"],ganyu["zhi"])
        # self.driver.find_element(By.XPATH,'//*[text()="视频"]').click()
        # sleep(2)
        # self.driver.find_element(By.LINK_TEXT,"视频").click()
        # all_handles=self.driver.window_handles
        # self.driver.switch_to.window(all_handles[1])
        # self.driver.find_element(By.XPATH,'//*[@maxlength="255"]').send_keys("刻晴")
        # self.driver.find_element(By.XPATH,'//*[@class="search-input-btn"]').click()
        # ele5=self.driver.find_element(By.XPATH,'//*[@class="ant-tabs-tab-active ant-tabs-tab"]').text
        # assert ele5 == "视频"
        # self.driver.get_screenshot_as_file(r'G:\untitled\liuxing2\test_case\picture\shiping.png')
    @pytest.mark.parametrize("qi",Yaml(r"data\tupian.yaml").read_yaml())
    def test_tupian(self,qi):
        qq=Po_3()
        qq.qiqi(qi["value"],qi["zhi"])
        # self.driver.find_element(By.XPATH,'//*[text()="图片"]').click()
        # self.driver.find_element(By.ID,"kw").send_keys("可莉")
        # self.driver.find_element(By.XPATH,'//*[@value="百度一下" and @class="s_newBtn"]').click()
        # ele7=self.driver.find_element(By.XPATH,'//*[text()="炸弹"]').text
        # print(ele7)
        # assert ele7 == "炸弹"
        # self.driver.get_screenshot_as_file(r'G:\untitled\liuxing2\test_case\picture\tupain.png')
    @pytest.mark.parametrize("li",Yaml(r"data\zhidao.yaml").read_yaml())
    def test_zhidao(self,li):
        aa=Po_4()
        aa.zhongli(li["value1"],li["handle_value"],li["value2"],li["handle_value1"],li["zhi"])
    #     # self.driver.find_element(By.LINK_TEXT,'知道').click()
    #     # self.driver.find_elements(By.XPATH,'//*[@class="triangle_icon"]')[0].click()
    #     # all_handles=self.driver.window_handles
    #     # self.driver.switch_to.window(all_handles[1])
    #     # ele9=self.driver.find_elements(By.XPATH,'//*[@class="triangle_icon"]')[1]
    #     # ActionChains(self.driver).move_to_element(ele9).perform()
    #     # self.driver.find_element(By.XPATH,'//*[@data-type="video-author"]').click()
    #     # all_handles=self.driver.window_handles
    #     # self.driver.switch_to.window(all_handles[2])
    #     # ele10=self.driver.find_element(By.ID,'TANGRAM__PSP_11__regLink').text
    #     # assert ele10=="立即注册"
    #     # self.driver.get_screenshot_as_file(r'G:\untitled\liuxing2\test_case\picture\zhidao.png')
    @pytest.mark.parametrize("qing1",Yaml(r"data\wenku.yaml").read_yaml())
    def test_wenku(self,qing1):
        pp=Po_5()
        pp.qing(qing1["zhi"])
        # self.driver.find_element(By.LINK_TEXT,"文库").click()
        # self.driver.find_element(By.XPATH,'//*[text()="IT互联网"]').click()
        # self.driver.find_element(By.XPATH,'//*[text()="法律经济"]').click()
        # self.driver.find_element(By.XPATH, '//*[text()="生活艺术"]').click()
        # ele1=self.driver.find_element(By.XPATH,'//div/span/div[@class="tag-item"][3]')
        # ele2=self.driver.find_element(By.XPATH,'//div/span/div[@class="tag-item"][1]')
        # ActionChains(self.driver).drag_and_drop(ele1,ele2).perform()
        # ll=self.driver.find_element(By.XPATH,'//*[@class="btn primary"]').text
        # assert ll== "确定"
    @pytest.mark.parametrize("ba",Yaml(r"data\tieba.yaml").read_yaml())
    def test_tieba(self,ba):
        kk=Po_6()
        kk.baer(ba["value"],ba["zhi"])
        # self.driver.find_element(By.XPATH,'//*[text()="贴吧"]').click()
        # self.driver.find_element(By.ID,"wd1").send_keys("刻晴")
        # self.driver.find_element(By.XPATH,'//*[text()="进入贴吧"]').click()
        # keqing=self.driver.find_element(By.LINK_TEXT,"刻晴吧").text
        # assert keqing=="刻晴吧"




