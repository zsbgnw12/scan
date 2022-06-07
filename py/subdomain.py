import time
import re
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
opt = Options()
opt.add_argument("ignore-certificate-errors")
#设置忽略ssl证书认证错误
opt.add_argument('--headless')
opt.add_argument('--disable-gpu')
web = Chrome(chrome_options=opt)

def user_input(url):
    urls = url
    res = re.findall(r'[\w_]+(?:\.[\w_]+)', urls)  # https?://
    if res and res[0] == urls:
        return urls
    else:
        print('----->子域名查询的格式为：baidu.com\n')
        while True:
            urls = input("请重新输入正确的url地址")
            res = re.findall(r'[\w_]+(?:\.[\w_]+)', urls)  # https?://
            if res and res[0] == urls:
                return urls
                break
            else:
                print('----->您输入了错误的url地址')

def ruo_me(url):
    web.get('https://ruo.me/',)
    web.find_element_by_xpath('//*[@id="domain"]').send_keys(url)
    web.find_element_by_xpath('//*[@id="button_s"]').click()
    print('----->子域名查询中请等待十五秒左右')
    for t in range(500):
        time.sleep(5)
        contents = web.find_element_by_xpath('//*[@id="div_msg"]').text
        content_text = str(contents)
        if content_text.find('查询成功')<0:
            print('----->您等待了5秒')
        else:
            content = web.find_element_by_xpath('//*[@id="div_msg"]').text
            #print(content)
            available = re.findall('查询成功：(.*?) - (.*?)\n',content)
            if str(available) == '[]':
                    print("----->没有查询到可访问的子域名")
            else:
                file_ok(available,url)
                print("----->已将可访问子域名保存")
            #print(available)
            for line in available:
                lines = str(line)
                print('----->可访问的子域名有'+lines)
            return content
            break

def file_ok(lines,url):
    with open('collect\\'+url+".txt",mode='w',encoding="UTF-8") as f:
        f.write(str(lines))

def start_domain(url):
    url = user_input(url)
    whois = ruo_me(url)
    names = url
    web.close()
    if_write = input('----->可访问url已保存是否保存查询全部数据y/n(默认n)')
    if if_write.lower() != 'y':
        print('----->未保存数据')
    else:
        with open('../collect\\' + names + '子域名.txt', mode='w') as f:
            f.write(whois)
            print('----->保存数据成功！在文件collect中的whois文件')

    is_if_no = input('----->是否显示所有子域名查询结果y/n')
    if is_if_no.lower() != 'y':
        print('----->未显示详细子域名')
    else:print('----->详细结果如下\n'+whois)