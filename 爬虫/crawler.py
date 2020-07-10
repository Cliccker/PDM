import string
import json
import os
import pandas as pd
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time
import random

string.punctuation = string.punctuation + '；'


# 读取上次爬虫的字典
# def Dict(Path):
#     a = []
#     corpus = pd.read_csv(Path)
#     corpus = corpus.values.tolist()
#     for i in range(len(corpus)):
#         a.append(corpus[i][1])
#     b = set(a)
#     return b


def ch():
    iframe = browser.find_element_by_id('iframeResult')
    if iframe:
        browser.switch_to.frame(iframe)
    browser.find_element_by_class_selector('a.Ch').click()
    time.sleep(random.uniform(1, 3))
    # browser.find_element_by_class_name('Btn5').click()
    time.sleep(5)
    browser.switch_to.parent_frame()


# 搜寻关键词
def init(keyword):
    browser.get('https://kns.cnki.net/kns/brief/result.aspx?dbprefix=scdb')
    time.sleep(random.uniform(1, 3))
    screach_text = browser.find_element_by_id('magazine_value1')
    screach_text.send_keys(keyword)
    pull = browser.find_element_by_id('magazine_special1')
    Select(pull).select_by_value('=')
    browser.find_element_by_class_name('buttOther').click()
    time.sleep(30)


# 返回首页
def switch2firsturl():
    n = browser.window_handles
    for handle in n:
        if handle != firstHandle:
            browser.switch_to.window(handle)
            browser.close()
    browser.switch_to.window(firstHandle)


# 获取数据
def downdata(i):
    time.sleep(random.uniform(2, 4))
    iframe = browser.find_element_by_css_selector('iframe#iframeResult')
    if iframe:
        browser.switch_to.frame('iframeResult')
    a = browser.find_elements_by_css_selector('a.fz14')
    a[i].click()
    # 句柄控制
    n = browser.window_handles
    print('当前句柄: ', n)
    browser.switch_to.window(n[-1])
    # 从浏览器中提取信息
    # 等待2秒
    time.sleep(random.uniform(1, 3))
    # 把数据读到内存
    divpaper_name = browser.find_element_by_css_selector('h2.title')
    divwxBaseinfo = browser.find_element_by_css_selector('div.wxBaseinfo')
    divChDivSummary = divwxBaseinfo.find_element_by_id('ChDivSummary')
    divcatalog_KEYWORDs = divwxBaseinfo.find_elements_by_xpath("//label[@id='catalog_KEYWORD']/..")[0]. \
        find_elements_by_css_selector('a')
    keys = []
    paper_list = []
    for y in range(len(divcatalog_KEYWORDs)):
        keys.append(divcatalog_KEYWORDs[y].text.translate(str.maketrans('', '', string.punctuation)))
        # Keywords.add(divcatalog_KEYWORDs[y].text.translate(str.maketrans('', '', string.punctuation)))
    paper_name = divpaper_name.text
    summary = divChDivSummary.text
    paper_list.append({'paper_name': paper_name, 'summary': summary, 'keywords': keys})
    switch2firsturl()
    return paper_list


if __name__ == '__main__':

    browser = webdriver.Chrome()
    firstHandle = browser.window_handles[0]

    magazine = "化工机械"  # 这里填写杂志名称
    path = '../data/srcData/' + magazine
    # Keywords = Dict(path)

    init(magazine)

    if os.path.isfile(path + '_data.json'):
        content = json.load(open(path + '_data.json', 'r', encoding='utf-8'))  # 加载已经爬取的数据
    else:
        content = []  # 如没有数据则创建一个空列表

    count = 0
    while count < 10000:
        for i in range(50):
            try:
                papers = downdata(i)
                count += 1
                content.append(papers)
            except Exception as e:
                print(e)
                switch2firsturl()
                continue
            except IndexError:
                ActionChains(browser).key_down(Keys.ARROW_LEFT).perform()
                continue
        # list_k = list(Keywords)
        print('目前已处理%d篇文献' % count)
        # dataframe = pd.DataFrame({'关键词': list_k})
        with open(path + '_data.json', 'w', encoding='utf-8') as f:
            json.dump(content, f, ensure_ascii=False)
        # dataframe.to_csv(path + "_dict.csv", sep=',', encoding='utf-8')
        # 将DataFrame存储为csv,index表示是否显示行名，default=True
        # 不是每次循环都会存储字典
        ActionChains(browser).key_down(Keys.ARROW_RIGHT).perform()
        time.sleep(random.uniform(2, 4))
