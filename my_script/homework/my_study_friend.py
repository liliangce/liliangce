# /usr/bin/evn python=2.7
# coding=utf-8

import os

import time
import selenium
from selenium import webdriver

URL = 'http://www.baidu.com'
WAIT_TIME = 2  # 等待时间，视网速定


class GetInfoFromBaidu(object):
    def __init__(self):
        self.driver = selenium.webdriver.Chrome()
        self.current_path = os.path.dirname(__file__)

    def open_web_site(self):
        self.driver.get(URL)

    def get_keyword_for_search(self):
        dir_path = os.path.join(self.current_path, 'my_needed_info', 'be_searched_info.txt')
        with open(dir_path, 'rb')as f:
            return f.read()

    def search_keyword_from_web(self):
        files_floder = os.path.join(self.current_path, 'tmp')
        os.chdir(files_floder)
        self.open_web_site()
        time.sleep(WAIT_TIME)
        search_info_box = self.driver.find_element_by_css_selector('#kw')
        keyword_info = self.get_keyword_for_search()
        print keyword_info.decode('utf-8')
        search_info_box.send_keys(keyword_info.decode('utf-8'))
        # print self.driver.page_source
        time.sleep(WAIT_TIME)
        content = self.driver.find_element_by_css_selector('body #content_left')  # 规律一：百度的搜索结果在这个元素内
        current_page = self.driver.current_window_handle
        pages = content.find_elements_by_css_selector('h3 a')

        for elements_url in pages:
              # 'unicode'object is not callable的错误一般是把字符串当做函数使用了
            a = elements_url.click()
            time.sleep(2)
            self.driver.switch_to.window(current_page)
            time.sleep(WAIT_TIME)
        num = len(pages)
        handles = self.driver.window_handles
        for i in range(num):
            tem_file_name = str(i) + '.html'
            self.driver.switch_to.window(handles[i])
            with open(tem_file_name, 'ab+') as f:
                f.write(self.driver.page_source.encode("utf-8"))
            time.sleep(WAIT_TIME)
        self.driver.quit()

if __name__ == '__main__':
    t = GetInfoFromBaidu()
    t.search_keyword_from_web()
