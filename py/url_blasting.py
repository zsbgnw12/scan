import aiohttp
import asyncio
import re
header={
'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Mobile Safari/537.36 Edg/101.0.1210.53'
}
async def requests_get(url,dir):
    urls = str(url.strip())+str(dir.strip())
    # print(type(urls),urls)
    # urls = "http://www.4399.com/flash"
    async with aiohttp.ClientSession() as session:

        async with session.get(urls,headers=header) as resp:
            # r = await resp.text()
            s = resp.status
            # print(r)
            print(urls+"状态码"+str(s))
            # print(url+dir,"请求结果为："+str(r))
            await asyncio.sleep(2)

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

async def main(url,url_file):
    dir_url = if_url(url)#str(input("请输入正确的url\n如http://www.4399.com："))
    # dir_txt = "../playload\\dir.txt" # str(input("请输入字典名字及后缀："))
    print("-" * 15 + "程序开始" + "-" * 15)
    with open('playload\\'+url_file,mode='r',encoding='utf-8') as ff:
        dirs_txt = ff.readlines()
    takes = []
    for i in dirs_txt:
        requests_code = requests_get(dir_url,i)
        takes.append(requests_code)
        # print(i)
    await asyncio.wait(takes)

def aiorun(url,urlfile):
    asyncio.run(main(url,urlfile))
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(main())