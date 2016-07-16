'''
Created on 2016年7月5日

@author: HCQ
'''
from urllib import request

class HtmlDownload(object):
    
    
    def download(self,url):
        if url is  None:
            return None
        
        response = request.urlopen(url)
        
        if response.getcode() != 200:
            return None
        
        return response.read()
    
    



