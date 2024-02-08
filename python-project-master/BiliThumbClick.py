# 网页点赞功能
# 1. 通过selenium模拟浏览器打开网页
# 2. 通过selenium模拟点击点赞按钮
# 3. 通过selenium模拟点击提交按钮

from threading import Thread
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Edge
import time

edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option("detach", True)
edge = webdriver.Edge(options=edge_options)

# 打开网页
edge.get("https://live.bilibili.com/31846655?live_from=82001&broadcast_type=1&spm_id_from=333.1007.top_right_bar_window_dynamic.content.click")


def login():
    try:
        time.sleep(1)
        login = edge.find_element(By.CLASS_NAME, "header-login-entry")
        login.click()

        # time.sleep(2)
        # account = edge.find_element(By.CLASS_NAME, "bili-mini-account")
        # account.send_keys("17682300000")
        # time.sleep(1)
        # password = edge.find_element(By.CLASS_NAME, "bili-mini-password")
        # password.send_keys("17682300000")


    except:
        print("-----------------------------登录失败-----------------------------")



def main(chrome):
    try:

        thumb = chrome.find_element(By.XPATH, '//*[@id="control-panel-ctnr-box"]/div[1]/div[2]/div[1]')

        for (i) in range(0, 10000):
            time.sleep(0.3)
            thumb.click()


    except:
        print("-----------------------------EXCEPT-----------------------------")

if __name__ == "__main__":
    login()
    time.sleep(18)
    Thread.start(main(edge))
