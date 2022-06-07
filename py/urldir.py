import optparse
import requests
import math,re
import threading
import os

def if_url(url):
    urls = url
    res = re.findall(r'https?://[\w_]+(?:\.[\w_]+){2,3}(?:/[\w_]+)*(?:\.[\w_]+)?/?', urls)  # https?://
    if res and res[0] == urls:
        return urls
    else:
        print('----->目录猜测的格式为：http://www.4399.com')
        while True:
            urls = input("请重新输入正确的url地址\n----->如http://www.4399.com：")
            res = re.findall(r'https?://[\w_]+(?:\.[\w_]+){2,3}(?:/[\w_]+)*(?:\.[\w_]+)?/?', urls)  # https?://
            if res and res[0] == urls:
                return urls
                break
            else:
                print('----->您输入了错误的url地址')

def file_url(url_file,ths_dic):
    result_list = []
    with open('playload\\'+url_file,mode='r',encoding='utf-8') as f:
        pass_line_list = f.readlines()
        if len(pass_line_list) % int(ths_dic) == 0:
            thread_read_line_num = len(pass_line_list) / int(ths_dic)#判断线程数是否可以被整分
        else:#math.ceil(2,1）向上取整->3
             thread_read_line_num = math.ceil(len(pass_line_list) / int(ths_dic))#每个线程读取的行数
        i = 0
        temp_list = []#制作一个临时列表
        threads_list = []#制作一个多线程列表
        # print('被取数', thread_read_line_num)
        # print('总数', len(pass_line_list))
        # print('线程数', int(ths_dic))

        for line in pass_line_list:
            i = i +1
            if i % thread_read_line_num == 0:#判断读取行数与线程数是否为零
                 temp_list.append(line.strip())#当读取到求余为零时，将temp临时所有的行放入线程输出列表result中
                 result_list.append(temp_list)
                 temp_list = []#最后将临时列表清空然后再次循环
            else:  # 不等于零都读取到temp临时列表中
                 temp_list.append(line.strip())
                 if (len(pass_line_list))-i == 0:#当总数读取行等于i时临时列表存入result列表中
                     result_list.append(temp_list)

            #如果最后一个为空就排除
               #result_list.append(temp_list)#最后将余的行也加入result输出列表中
    #print(result_list)
    #lends = len(result_list)
    return result_list

def requst_if(url,threads):
    threads_list = []
    for i in threads:
        threading.Thread
        #*args和**kwargs给表示可变的参数传递，可变的i传入url给scan，
        threads_list.append(threading.Thread(target=scan, args=(url,i)))#多线程并发执行
        # print(threads)
    for t in threads_list:#启动线程
        t.start()

def scan(url,dic):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0"}
    for line in dic:
        # print(line)
        r = requests.get(url+line,headers=headers)
        if r.status_code == 200:
            print(r.url + '\t' + str(r.status_code))
            r.close()
        else:
            print(r.url + '\t' + str(r.status_code))
            r.close()


def threads(url,threads,urlfile):
    # print(parser_option.urlfile)url文件
    # print(parser_option.website)url
    # print(parser_option.threads)线程数
    threads_list = file_url(urlfile,threads)
    urls = if_url(url)
    requst_if(urls,threads_list)
