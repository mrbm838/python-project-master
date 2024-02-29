# 网页点赞功能
# 1. 通过selenium模拟浏览器打开网页
# 2. 通过selenium模拟点击点赞按钮
# 3. 通过selenium模拟点击提交按钮

from threading import Thread
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Edge
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException, StaleElementReferenceException, WebDriverException
import time
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import InvalidElementStateException
from selenium.common.exceptions import NoSuchWindowException
from selenium.common.exceptions import SessionNotCreatedException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option("detach", True)
edge = webdriver.Edge() # options=edge_options

# 设置浏览器窗口全屏
# edge.maximize_window()
# 设置浏览器窗口d大小
edge.set_window_size(1920, 1280)

# 打开网页
# edge.get("https://live.bilibili.com/30800241?live_from=82001&broadcast_type=1&spm_id_from=333.1007.top_right_bar_window_dynamic.content.click")
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
        print("-----------------------------失败-----------------------------")




def main(edge):
    try:
        for i in range(1500):
            try:
                # thumb = edge.find_element(By.XPATH, '//*[@id="control-panel-ctnr-box"]/div[1]/div[2]/div[1]')
                thumb = WebDriverWait(edge, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="control-panel-ctnr-box"]/div[1]/div[2]/div[1]')))
                time.sleep(0.3)
                thumb.click()
            except (NoSuchElementException):
                print("-------------------------NoSuchElementException---------------------------------")
            except (ElementNotInteractableException):
                print("-------------------------ElementNotInteractableException---------------------------------")
            except (StaleElementReferenceException):
                print("-------------------------StaleElementReferenceException---------------------------------")
            except (ElementClickInterceptedException):
                print("-------------------------ElementClickInterceptedException---------------------------------")
            except (InvalidElementStateException):
                print("-------------------------InvalidElementStateException---------------------------------")
            except (NoSuchWindowException):
                print("-------------------------NoSuchWindowException---------------------------------")
            except (SessionNotCreatedException):
                print("-------------------------SessionNotCreatedException---------------------------------")
            except (TimeoutException):
                print("-------------------------TimeoutException---------------------------------")
            except (UnexpectedAlertPresentException):
                print("-------------------------UnexpectedAlertPresentException---------------------------------")
            except (WebDriverException):
                print("-------------------------WebDriverException---------------------------------")

            continue

    except:
        print("-----------------------------EXCEPT-----------------------------")

if __name__ == "__main__":
    # login()
    # time.sleep(20)

    # 开一个线程运行main方法    
    t = Thread(target=main, args=(edge,))
    t.start()

    # Thread.start(main(edge))
