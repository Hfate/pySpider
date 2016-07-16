'''
Created on 2016年7月5日

@author: HCQ
'''
from baike_spider import url_manager, html_download, html_output, html_parser
from asyncio.tasks import sleep


class SpiderMain(object):
    def __init__(self):
        self.urls=url_manager.UrlManager()
        self.download=html_download.HtmlDownload()
        self.output=html_output.HtmlOutput()
        self.parser = html_parser.HtmlParser()

    
    
    
    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print ('craw %d : %s'%(count,new_url))
                html_cont = self.download.download(new_url)
                new_urls,new_data = self.parser.parser(new_url,html_cont)
                self.urls.add_new_urls(new_urls)
                self.output.collect_data(new_data)
            
                if count==500:
                    break
                count=count+1
            except:
                print ('craw failed')    
        self.output.output_html()
        

if __name__ == "__main__":
    root_url="http://baike.baidu.com/view/582.htm"
    obj_spider=SpiderMain()
    obj_spider.craw(root_url)