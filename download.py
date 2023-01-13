import time
import requests
import re
import os
headers = {
        'authority': 'github.com',
        'accept': 'text/html',
        'accept-language': 'en,en-GB;q=0.9,zh-CN;q=0.8,zh;q=0.7',
        'cache-control': 'no-cache',
        'pragma': 'no-cache',
        'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }
proxies={
    "http":"ip:port",
    "https":"ip:port"
}

def get_urllist(url:str)->list:
    response = requests.get(url=url.replace('tag','expanded_assets'),headers=headers,proxies=proxies)
    dinfo=response.text
    durllist=re.findall(r'href="(.*?)"',dinfo)
    print(durllist)
    return durllist

def gendir(path:str):
    dir_path=os.getcwd()
    if not os.path.exists(dir_path+'/'+path):
        os.mkdir(path)

def downfiles(uri:str,path:str):
    filename=uri.split('/')[-1]
    response = requests.get(url="https://github.com"+uri,headers=headers,proxies=proxies)
    with open(f'{path}/{filename}','wb')as f:
        f.write(response.content)

def main(url:str):
    path='files'
    gendir(path)
    durllist=get_urllist(url)
    for index,uri in enumerate(durllist):
        downfiles(uri,path)
        print(f"第{index+1}个文件下载成功")

if __name__ == '__main__':
    url=''
    main(url)
