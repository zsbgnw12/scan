# **Requirement**

**Requirement: python 3.6 or higher**

Choose one of these installation options:

- Install with git: `git clone https://github.com/zsbgnw12/scan.git (RECOMMENDED)
- Install with ZIP file: [Download here](https://github.com/zsbgnw12/scan/archive/refs/heads/master.zip)

**All in one:**

```
git clone https://github.com/zsbgnw12/scanccs.git
cd scanccs
pip3 install requests,selenium,asyncio,aiohttp
python3 start.py -u <URL> -p <FUNCTION> -t <THREADING> -s <FILE>
```


Options
-------

```python
Usage: start.py [-u|--url] target [-p playlaod] function [-t thread] threading [-s urlfile] file

Options:
  -h         , --help            show this help message and exit
  -u URL     , --site=URL
                                 website to test
  -s URLTEXT , --urlfile=URLTEXT
                                 user from file
  -t THREADS , --threads=THREADS
                                 number of threads
  -p PLAYLOAD, --playload=PLAYLOAD
                                 choice what you need playload                                               (-p whois , whois查询)
                                    (-p udp , 开放端口查询)   
                                    (-p cdn , CDN查询)   
                                    (-p cms , cms查询)
                                    (-p domain ,查询子域名)   
                                    (-p urldir , 目录猜测-多线程 )
                                    (-p  urldirs , 目录猜测-异步协程)   
```

Use
---------------

```
python start.py -u <URL> -p <FUNCTION>
```



# Be careful

```
python环境必须为3.0及以上。
path文件中提供3.8.8版本安装。
本工具需使用Google浏览器。
请安装path文件夹下的Chrome浏览器。
并将chromoeadriver文件移动至您python编译中的scripts文件下。
如果使用pycharm工具将chromoeadriver移动编译scripts文件下。
安装所需的运行环境库。
```

