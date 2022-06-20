from selenium.webdriver.common.by import By

from base.base import Base


class Po_4(Base):
    #元素属性
    zhongli1=(By.LINK_TEXT,'知道')
    zhongli2=(By.XPATH,'//*[@class="triangle_icon"]')
    zhongli3=(By.XPATH,'//*[@class="triangle_icon"]')
    zhongli4=(By.XPATH,'//*[@data-type="video-author"]')
    zhongli5=(By.ID,'TANGRAM__PSP_11__regLink')
    zhongli6=r'G:\untitled\liuxing2\test_case\picture\zhidao.png'
    #元素方法
    def zhongli(self,value1,handle_value,value2,handle_value1,zhi):
        self.click(Po_4.zhongli1)
        self.clicks(Po_4.zhongli2,value1)
        self.handles(handle_value)
        self.subiaos(Po_4.zhongli3,value2)
        self.click(Po_4.zhongli4)
        self.handles(handle_value1)
        self.vilidata1(Po_4.zhongli5,zhi)
        self.jietu(Po_4.zhongli6)

