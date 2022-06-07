import re
import os
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
opt = Options()
opt.add_argument('--headless')
opt.add_argument('--disable-gpu')
web = Chrome(chrome_options=opt)

def if_url(url):
    urls = url
    res = re.findall(r'[\w_]+(?:\.[\w_]+)', urls)  # https?://
    if res and res[0] == urls:
        return urls
    else:
        print('----->whois查询url地址格式为:baidu.com')
        while True:
            urls = input("请重新输入url地址")
            res = re.findall(r'[\w_]+(?:\.[\w_]+)', urls)  # https?://
            if res and res[0] == urls:
                return urls
                break
            else:
                print('----->您输入了错误的url地址')

def chianz(url):
    web.get('https://whois.aizhan.com/')
    web.find_element_by_xpath('//*[@id="domain"]').send_keys(url,Keys.ENTER)
    content = web.find_element_by_xpath('/html/body/div[4]/div[2]').text
    print(content)
    return content
def start_whois(url):
    url = if_url(url)
    print("正在查询中请稍后")
    whois = chianz(url)
    print(whois)
    if str(whois).find('正在更新') >= 0:
        print("----->响应为空，请检查地址可访问性")
    names = url
    web.close()
    if_write = input('是否保存查询数据y/n(默认n)')
    if if_write != 'y':
        print('未保存数据')
    else:
        with open('collect\\'+names+'whois查询.txt',mode='w') as f:
            f.write(whois)
            print('保存数据成功！在文件collect中的whois文件')
