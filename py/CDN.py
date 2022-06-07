import requests
import re

def if_url(url):
    urls = url
    res = re.findall(r'[\w_]+(?:\.[\w_]+){2,3}(?:/[\w_]+)*(?:\.[\w_]+)?/?', urls)  # https?://
    if res and res[0] == urls:
        return urls
    else:
        print('----->cdn查询ip地址格式为：www.baidu.com\n')
        while True:
            urls = input("请重新输入正确的url地址")
            res = re.findall(r'[\w_]+(?:\.[\w_]+){2,3}(?:/[\w_]+)*(?:\.[\w_]+)?/?', urls)  # https?://
            if res and res[0] == urls:
                return urls
                break
            else:
                print('----->您输入了错误的url地址')

def cms_class(url):
    heard = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0'
    }

    print("----->查询中请稍后")
    url = if_url(url)
    data = {
        'get_site_ip': 1,
        'input_website': url
    }

    r = requests.post('https://get-site-ip.com/inc/icey_ajax.php',headers=heard,data=data)
    rtext = re.findall('"geo_data":(.*?),"error"',r.text)
    cms = re.findall('"(.*?)":"(.*?)"',str(rtext))
    r.close()
    for i in cms:
        if str(i).find('ERROR')>0:
            print("----->响应为空->请检查地址可访问性")
            break
        else:
            print(i)
