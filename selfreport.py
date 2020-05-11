from selenium import webdriver


class SelfReport(object):

    def __init__(self):
        self.driver = webdriver.Chrome()

    def auto_report(self):
        driver = self.driver
        driver.get('https://selfreport.shu.edu.cn/Default.aspx')
        print("="*100)
        print("已进入填报网站")
        username = driver.find_element_by_id("username")
        username.send_keys("SHU一卡通账号")
        password = driver.find_element_by_id("password")
        password.send_keys("SHU一卡通密码")
        print("自动填入账号密码完成")
        submit = driver.find_element_by_id("login-submit")
        submit.click()
        print("进入每日一报网站")
        driver.find_element_by_id("lnkReport").click()
        promise = driver.find_element_by_id("p1_ChengNuo-inputEl-icon")
        promise.click()
        temperature = driver.find_element_by_id("p1_TiWen-inputEl")
        temperature.send_keys("36")
        print("填报体温完成")
        print("勾选承诺完成")
        submit_res = driver.find_element_by_id("p1_ctl00_btnSubmit")
        submit_res.click()
        driver.find_element_by_id("fineui_33").click()
        print("每日一报已完成")
        print("="*100)

    def run(self):
        self.auto_report()


if __name__ == '__main__':
    sp = SelfReport()
    sp.run()
