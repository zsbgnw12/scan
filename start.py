import optparse
import math
def udp_data():
    remota_servers = start_help()
    return remota_servers.website
def start_help():
    parser = optparse.OptionParser()#初始化
    parser.usage = 'start.py [-u|--url] target [-p playlaod] function [-t thread] threading [-s urlfile] file'
    #帮助信息输出
    #制作参数传递信息，保存在dest中，action传递，类型为string
    parser.add_option("-u","--site",metavar='URL    ',dest="website",help="website to test",action="store",type="string")
    parser.add_option('-s','--urlfile',metavar='URLTEXT',dest='urlfile',help='user from file',action='store',type='string')
    parser.add_option('-t','--threads',metavar='THREADS',dest='threads',help='number of threads',action='store',type='int')
    parser.add_option('-p',"--playload",metavar='PLAYLOAD',dest='playload',help="choice what you need playload   (-p whois , whois查询)   (-p udp , 开放端口查询)   (-p cdn , CDN查询)   (-p domain , 查询子域名)   (-p urldir , 目录猜测-多线程 , -p  urldirs , 目录猜测-异步协程)   (-p cms , cms查询)",action='store',type='string')
    (options,args) = parser.parse_args()
    return options

    # ths_dic = options.threads
    # user_dic = options.urlfile
    # pass_dic = options.playload
    # site = options.website

def choice(start):
    i = str(start.playload)
    url = start.website
    thread = start.threads
    urlfile = start.urlfile
    if i.lower() == "whois":
        from py.whois import start_whois
        start_whois(url)
    elif i.lower() == "udp":
        from py.udp import ScanPort
        ScanPort().start()
    elif i.lower() == "cdn":
        from py.CDN import cms_class
        cms_class(url)
    elif i.lower() == "domain":
        from py.subdomain import start_domain
        start_domain(url)
    elif i.lower() == "urldir":
        from py.url_blasting import aiorun
        aiorun(url,urlfile)
    elif i.lower() == "cms":
        from py.cms import text
        text(url)
    elif i.lower() == "urldirs":
        from py.urldir import threads
        threads(url,thread,urlfile)
    else:
        print("错误参数")




if __name__ == '__main__':
    print("""

                                ___              —————————|    —————————|
                           __A__                |  ———————|   |  ———————|  {6.6.6.6#dev}
                     ___ ___[']_____ ___ ___    |  |          |  |
                    |_ -| . [,]     | .'| . |   |  |          |  |
                    |___|_  [.]_|_|_|__,|  _|   |  |——————|   |  |——————|
                          |_|V...       |_|     ——————————|   ——————————|  @Chenchen Disclaimers
                           
                          You can download it in https://github.com/zsbgnw12/scanccs.git
    """)
    print("""
                                提供查询内容如下:
                                -p whois                           whois查询
                                -p udp                             开放端口查询
                                -p cdn                             CDN查询
                                -p domain                          子域名查询
                                -p cms                             cms查询
                                -p urldir -s urlfile               目录猜测（异步协程模式）
                                -p urldirs  -s urlfile -t thread   目录猜测（多线程模式）
                                          
    """)
    satrt = start_help()
    choice(satrt)
