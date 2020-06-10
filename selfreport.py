#!/usr/bin/python3
# coding=UTF-8
from selenium import webdriver
import time
import random


class SelfReport(object):

    def __init__(self):

        self.driver = webdriver.Chrome()

    def auto_report(self):
        file_handle = open('log.txt', mode='a',encoding='utf-8')
        driver = self.driver
        driver.get('https://selfreport.shu.edu.cn/Default.aspx')
        print("="*100)
        file_handle.write('\n')
        file_handle.write('='*100)
        file_handle.write('\n')
        print("已进入填报网站")
        file_handle.write(time.ctime())
        file_handle.write('\n')
        username = driver.find_element_by_id("username")
        username.send_keys("input your username")
        password = driver.find_element_by_id("password")
        password.send_keys("input your password")
        print("自动填入账号密码完成")
        submit = driver.find_element_by_id("login-submit")
        submit.click()
        print("进入每日一报网站")
        driver.find_element_by_id("lnkReport").click()
        promise = driver.find_element_by_id("p1_ChengNuo-inputEl-icon")
        promise.click()
        temperature = driver.find_element_by_id("p1_TiWen-inputEl")
        store = ["36.8","36.9","37","37.1","37.2"]
        i = random.randint(0,4)
        choose = store[i]
        temperature.send_keys(choose)
        print("填报体温完成")
        print("勾选承诺完成")
        time.sleep(1)
        submit_res = driver.find_element_by_id("p1_ctl00_btnSubmit")
        submit_res.click()
        time.sleep(1)
        driver.find_elements_by_css_selector(".f-btn.f-noselect.f-state-default.f-corner-all"
                                                    ".f-btn-normal.f-btn-icon-no.f-cmp.f-widget"
                                                    ".f-toolbar-item")[3].click()
        # driver.find_element_by_id("fineui_37").click()
        print(time.ctime())
        time.sleep(1)
        driver.close()
        print("每日一报已完成")
        print("="*100)
        file_handle.write('体温为'+choose+'度\n')
        file_handle.write('已完成每日一报自动填写\n')
        file_handle.write('='*100)
        file_handle.write('\n')

        file_handle.close()

    def run(self):
        self.auto_report()


if __name__ == '__main__':
    sp = SelfReport()
    sp.run()
