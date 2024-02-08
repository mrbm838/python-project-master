import time
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
from selenium import webdriver
from threading import Thread

# 不自动关闭浏览器
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome1 = webdriver.Chrome(options=chrome_options)
chrome2 = webdriver.Chrome(options=chrome_options)
chrome3 = webdriver.Chrome(options=chrome_options)
# 声明浏览器对象，这里是谷歌浏览器
# chrome = Chrome()
flag2 = False


def main(chrome, name1, id1, today, delay):
    try:
        time.sleep(0.5)
        name = chrome.find_element(
            By.XPATH, '//*[@id="question_q-1-CfjY"]/div[2]/input'
        )
        name.send_keys(name1)

        time.sleep(0.5)
        id_num = chrome.find_element(
            By.XPATH, '//*[@id="question_q-2-NJDC"]/div[2]/input'
        )
        id_num.send_keys(id1)

        time.sleep(0.2)
        morning = chrome.find_element(
            By.XPATH, '//*[@id="question_q-4-R7xD"]/div[2]/div[1]/label/p/div/p'
        )
        morning.click()

        time.sleep(0.2)
        if delay:
            night = chrome.find_element(
                By.XPATH, '//*[@id="question_q-3-Eqn5"]/div[2]/div[1]/label/p/div/p'
            )
            night.click()
        else:
            night = chrome.find_element(
                By.XPATH, '//*[@id="question_q-3-Eqn5"]/div[2]/div[4]/label/p/div/p'
            )
            night.click()

        time.sleep(delay)
        submit = chrome.find_element(By.CLASS_NAME, "btn-submit")
        submit.click()

        print()
        print("-----------------------------Completed-----------------------------")
    except:
        # 未开始
        # page_btn = chrome.find_element(By.CLASS_NAME, 'page-btn')
        # time.sleep(1)
        # page_btn.click()
        chrome.get("https://wj.qq.com/s/10833452/4af6")
        time.sleep(3)
        main(chrome, name1, id1, today, delay)


def process1():
    chrome1.get("https://wj.qq.com/s/10833452/4af6")
    time.sleep(3)
    time_tuple = time.localtime(time.time())
    main(chrome1, "游精前", "cwa4142", True, 3)


def process2():
    chrome2.get("https://wj.qq.com/s/10833452/4af6")
    time.sleep(3)
    time_tuple = time.localtime(time.time())
    while not flag2:
        main(chrome2, "余心阳", "cwa4136", False, 2.5)
        break


def process3():
    chrome3.get("https://wj.qq.com/s/10833452/4af6")
    time.sleep(3)
    time_tuple = time.localtime(time.time())
    main(chrome3, "凡世杰", "cwa8238", False, 2)


if __name__ == "__main__":

    thread1 = Thread(target=process1)
    thread1.start()
    thread2 = Thread(target=process2)
    thread2.start()
    thread3 = Thread(target=process3)
    thread3.start()

# pass
