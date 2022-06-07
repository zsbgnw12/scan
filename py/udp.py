import socket,re
from datetime import datetime
from multiprocessing.dummy import Pool as ThreadPool
import start
def if_url():
    urls = start.udp_data()
    res = re.findall(r'[\w_]+(?:\.[\w_]+){2,3}(?:/[\w_]+)*(?:\.[\w_]+)?/?', urls)  # https?://
    if res and res[0] == urls:
        return urls
    else:
        print('----->端口查询的格式为：www.baidu.com\n')
        while True:
            urls = input("请重新输入正确的url地址")
            res = re.findall(r'[\w_]+(?:\.[\w_]+){2,3}(?:/[\w_]+)*(?:\.[\w_]+)?/?', urls)  # https?://
            if res and res[0] == urls:
                return urls
                break
            else:
                print('----->您输入了错误的url地址')
class ScanPort:
    def __init__(self):
        self.ip = None

    def scan_port(self, port):
        list_ip_port = []
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            res = s.connect_ex((self.ip, port))
            if res == 0:  # 端口开启
                print('Ip:{} Port:{} 开放'.format(self.ip, port))
                ip_port = str(self.ip)+':'+str(port)
                # print(ip_port)
                list_ip_port.append(ip_port)
                # print(list_ip_port)
                with open("collect\\" + self.ip + '开放端口.txt', mode='a') as f:
                    f.write(str(list_ip_port) + '\n')

            else:
                print('Ip:{} Port:{}: 未开放'.format(self.ip, port))
        except Exception as e:
            print(e)
        finally:
            s.close()



    def start(self):
        remote_servers = if_url()#input("端口查询\n输入要扫描IP如www.baidu.com:")
        remote_server = remote_servers
        self.ip = socket.gethostbyname(remote_server)
        ports = [i for i in range(1, 81)]
        socket.setdefaulttimeout(0.5)
        t1 = datetime.now()
        threads = []
        pool = ThreadPool(processes=8)
        pool.map(self.scan_port, ports)
        pool.close()
        pool.join()
        t2 = datetime.now()
        print('端口扫描已完成，耗时：', t2 - t1)
        print('可用端口已保存在collect文件下')