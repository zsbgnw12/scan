import requests
import re
def reques(url):
    header={
        "User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Mobile Safari/537.36 Edg/102.0.1245.30"
    }
    r = requests.get(url,headers=header)
    r_text = r.text
    r.close()
    return r_text
def repas(ts):
    ts = ts.replace('[','')
    ts = ts.replace(']', '')
    ts = ts.replace('</a>', '')
    ts = ts.replace('</s>', '')
    ts = ts.replace("'", '')
    return ts
def if_url(url):
    urls = url
    res = re.findall(r'[\w_]+(?:\.[\w_]+)', urls)  # https?://
    if res and res[0] == urls:
        return urls
    else:
        print('----->cms查询格式为：baidu.com:')
        while True:
            urls = input("请重新输入正确的url地址")
            res = re.findall(r'[\w_]+(?:\.[\w_]+)', urls)  # https?://
            if res and res[0] == urls:
                return urls
                break
            else:
                print('----->您输入了错误的url地址')

def text(url):
    url = "https://w3techs.com/sites/info/"+if_url(url) #+ input("请输入要查询cmd的ip\n如baidu.com：")
    r = reques(url)
    # print(r)
    re_title = re.findall('<a href="https://w3techs.com/technologies.*?(.*?)<p class=si_h>',r)
    # print(re_title)
    if str(re_title) == "[]":
        print("----->响应为空->请检查地址的可访问性")
    for i in re_title[:-2]:
        # print(i)
        re_head = re.findall('">(.*?)</a><',i)[0:1]
        re_text = re.findall('<a href="https://w3techs.com/technologies.*?">(.*?)<br',i)
        re_heads = repas(str(re_head))
        re_texts = repas(str(re_text))
        print("----->",re_heads)
        print(re_texts.strip(),'\n')
