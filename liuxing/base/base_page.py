from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


class Base_page:
    #构造方法
    def __init__(self):
        driver = webdriver.Chrome()
        self.driver=driver
        self.driver.get("http://192.168.2.243")
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.ID, "ext-gen1035").click()  # 切换中英文
        self.driver.find_element(By.XPATH, "//*[text()='中文']").click()
        self.driver.find_element(By.ID, "username-inputEl").send_keys("JohnSmith")  # 账号密码登录
        self.driver.find_element(By.ID, "password-inputEl").send_keys(123456)
        sleep(2)
        self.driver.find_element(By.ID, "button-1017-btnIconEl").click()
    #定位元素
    def location_element(self,loc):
        return self.driver.find_element(*loc)
    #切换frame页面
    def iframe(self,loc):
        self.driver.switch_to.frame(self.location_element(loc))
    #退出iframe页面
    def quite_iframe(self):
        self.driver.switch_to.default_content()
    #点击元素
    def click(self,loc):
        self.location_element(loc).click()
    #输入值
    def send_keys(self,loc,value):
        self.location_element(loc).send_keys(value)
    #元素清空
    def clear(self,loc):
        self.location_element(loc).clear()
    #屏幕截图
    def screenshots(self, path):
        self.driver.get_screenshot_as_file(path)
    #断言
    def duanyan(self,loc,value):
        assert self.location_element(loc).text == value
    #睡眠
    def sleep(self,value):
        sleep(value)