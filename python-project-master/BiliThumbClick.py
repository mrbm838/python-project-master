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


def open_browser():
    edge_options = webdriver.EdgeOptions()
    edge_options.add_experimental_option("detach", True)

    edge_options.add_argument('--ignore-certificate-errors') #忽略CERT证书错误

    edge_options.add_argument('--ignore-ssl-errors') #忽略SSL错误

    edge_options.add_argument('--disable-gpu')

    edge_options.add_argument('--ignore-certificate-errors-spki-list')

    edge_options.add_argument('--ignore-urlfetcher-cert-requests')

    capability = edge_options.to_capabilities()

    capability["acceptInsecureCerts"] = True
    capability['acceptSslCerts'] = True

    # 启动浏览器驱动
    
    


    edge = webdriver.Edge()
    edge.set_window_size(1920, 1280)

    edge.get("https://live.bilibili.com/31846655?live_from=82001&broadcast_type=1&spm_id_from=333.1007.top_right_bar_window_dynamic.content.click") # 菠菜
    # edge.get("https://live.bilibili.com/31681075?live_from=82001&broadcast_type=1&spm_id_from=333.1007.top_right_bar_window_dynamic.content.click") # 依依

    return edge

def login(edge):
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
        for i in range(1200):
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
    edge = open_browser()

    login(edge)

    # 开一个线程运行main方法    
    t = Thread(target=main, args=(edge,))
    t.start()

    # Thread.start(main(edge))
