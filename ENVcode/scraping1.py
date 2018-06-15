from bs4 import BeautifulSoup
import requests
import html5lib
def download(url,user_agent = 'wswp',num_retries = 2,proxies = None):
    print('Downloading :',url)
    headers = {'User-Agent':user_agent}
    try:
        resp = requests.get(url,headers = headers,proxies = proxies)
        demo = resp.text
        if resp.status_code >= 400:
            print('Download error:',resp.text)
            demo = None
            if num_retries and 500 <= resp.status_code < 600:
                return download(url,num_retries -1)
    except requests.exceptions.RequestException as e:
        print('Download error:',e.reason)
        demo = None
    return demo
def main():
    url = 'http://www.lottery.gov.cn/historykj/history.jspx?page=false&_ltype=dlt&termNum=0&startTerm=18001&endTerm=18067'
    demo1 = download(url)
    
    soup = BeautifulSoup(demo1,'html5lib')
    human = soup.prettify()
    #print(human)
    with open('test.html','w+',encoding = 'utf-8') as f:
         f.writelines(human)
    #dic = {'period':,'red_ball':,'blue_ball':}

main()