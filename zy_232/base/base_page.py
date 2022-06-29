import time
from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
class Base():
    def __init__(self):
        driver = webdriver.Chrome()
        self.driver = driver
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get("http://192.168.2.32")
        driver.find_element(By.ID, "ext-gen1035").click()
        # 切换中英文
        driver.find_element(By.XPATH, '//*[@class="x-boundlist-item"]').click()
        driver.find_element(By.ID, "username-inputEl").send_keys("JohnSmith")
        driver.find_element(By.ID, "password-inputEl").send_keys(123456)
        sleep(2)
        # 进入首页
        driver.find_element(By.ID, "button-1017-btnIconEl").click()
    #定位单个元素
    def location(self,loc):
        return self.driver.find_element(*loc)
    #定位多个元素
    def locations(self,loc):
        return self.driver.find_elements(*loc)
    #点击单个元素
    def click(self,loc):
        self.location(loc).click()


    #进入iframe页面
    def iframe(self,loc):
        self.driver.switch_to.frame(self.location(loc))
    #退出iframe页面
    def out_iframe(self):
        self.driver.switch_to.default_content()
    #时间睡眠
    def sleep(self,loc):
        time.sleep(loc)
    #清空并输入值
    def send_keys(self,loc,value1):
        self.location(loc).clear()
        self.location(loc).send_keys(value1)
    #结果截图
    def jietu(self,file_path):
        self.driver.get_screenshot_as_file(file_path)
    #弹出框alert处理接受
    def alert(self):
        self.driver.switch_to.alert.accept()
    #切换handles
    def handle(self,handle_value):
        self.driver.switch_to.window(self.driver.window_handles[handle_value])
    #结果断言
    def assert1(self,loc,zhi):
        assert self.location(loc).text == zhi
    #鼠标双击
    def double_click(self,loc):
        ActionChains(self.driver).double_click(self.location(loc)).perform()
    #


