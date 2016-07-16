'''
Created on 2016年7月5日

@author: HCQ
'''
from bs4 import BeautifulSoup
import re
import urllib.parse

class HtmlParser(object):

    
    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        
        
        links = soup.find_all('a',href=re.compile(r"/view/\d+\.htm"))
        for link in links:
            new_url=link['href']
            
            new_full_url = urllib.parse.urljoin(page_url,new_url)
            new_urls.add(new_full_url)
        return new_urls
    
    
    def _get_new_data(self, page_url, soup):
        res_data={}
        
        #url
        res_data['url']=page_url
        
        #title
        title_node=soup.find('dd',class_="lemmaWgt-lemmaTitle-title").find("h1")
        res_data['title'] = title_node.get_text()
        
        #简介
        summary_node = soup.find('div',class_="lemma-summary")
        res_data['summary']=summary_node.get_text()
        
        #百度百科主内容   div
        main_node = soup.find('div',class_="main-content")
        res_data['miandiv']=main_node.get_text()
        
        #main_css = soup.find('link',ref_="stylesheet")
        #res_data['main_css']=main_css.get_all()
        
        return res_data
    
    def parser(self,page_url,html_cont):
        if page_url is None or html_cont is None:
            return
        
        soup = BeautifulSoup(html_cont,"html.parser",from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url,soup)
        new_data = self._get_new_data(page_url,soup)
        return new_urls,new_data
        
    