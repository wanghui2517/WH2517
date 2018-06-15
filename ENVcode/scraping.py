import urllib.request
from urllib.error import URLError, HTTPError, ContentTooShortError
def download(url,user_agent = 'wswp',num_retries = 2):
    print('Downloading :',url)
    request = urllib.request.Request(url)
    request.add_header('User-agent',user_agent)
    try:
        html = urllib.request.urlopen(request).read()
    except (URLError,HTTPError,ContentTooShortError) as e:
        print('Download error:',e.reason)
        html = None
        if num_retries > 0:
            if hasattr(e,'code') and 500 <= e.code < 600:
                return download(url,num_retries -1)
    return html
def main():
    url = 'http://www.lottery.gov.cn/historykj/history.jspx?page=false&_ltype=dlt&termNum=0&startTerm=18001&endTerm=18067'
    soup = download(url)
    f = open('test.html','w+')
    f.writelines(soup) 
main()