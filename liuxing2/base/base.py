from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains


class Base:
    def __init__(self):
        driver = webdriver.Chrome()
        self.driver = driver
        driver.get("https://tieba.baidu.com")
        driver.implicitly_wait(15)
    #单个定位元素
    def location(self,loc):
        return self.driver.find_element(*loc)
    #多个元素定位
    def locations(self,loc):
        return self.driver.find_elements(*loc)
    #获取单数文本值
    def text(self,loc):
        self.location(loc).text
    #获取复数文本值
    def texts(self,loc,valu):
        self.locations(loc)[valu].text
    #点击单数
    def click(self,loc):
        self.location(loc).click()
    #点击复数
    def clicks(self,loc,value1):
        self.locations(loc)[value1].click()
    #输入值
    def send_keys(self,loc,value):
        self.location(loc).send_keys(value)
    #切换窗口句柄
    def handles(self,handle_value):
        self.driver.switch_to.window(self.driver.window_handles[handle_value])
    #时间睡眠
    def sleep(self,shijian):
        sleep(shijian)
    #滚动条true
    def tiao(self,loc):
        self.driver.execute_script('arguments[0].scrollIntoView();',self.location(loc))
    #断言
    def vilidate(self,element,zhi):
        assert element==zhi
    #断言一个值
    def vilidata1(self,loc,zhi):
        assert self.location(loc).text==zhi
    #断言两个值
    def vilidate2(self,loc,zhi,dao):
        assert self.location(loc).text==zhi or self.location(loc).text==dao
    #截图
    def jietu(self,path):
        self.driver.get_screenshot_as_file(path)
    #单数鼠标事件悬停
    def subiao(self,loc):
        ActionChains(self.driver).move_to_element(self.location(loc)).perform()
    #复数鼠标时间悬停
    def subiaos(self,loc,value2):
        ActionChains(self.driver).move_to_element(self.locations(loc)[value2]).perform()
    #元素拖动
    def tuodong(self,loc1,loc2):
        ActionChains(self.driver).drag_and_drop(self.location(loc1),self.location(loc2)).perform()
    #滚动条false
    def tiaoxia(self,loc):
        self.driver.execute_script('arguments[0].scrollIntoView(false);',self.location(loc))
