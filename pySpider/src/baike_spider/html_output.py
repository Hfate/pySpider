'''
Created on 2016年7月5日

@author: HCQ
'''


class HtmlOutput(object):
    def __init__(self):
        self.datas = []
    
    def collect_data(self,data):
        if data is None:
            return
        self.datas.append(data)

    
    def output_html(self):
        ##ascii
        for data in self.datas:
            fname=data['url'][7:].replace("/","_").replace('?force=1','')
            fout=open(r"D:\spider\newbaike"+"\\"+fname+'l', 'w',encoding='utf-8')   #保存的目录  
            fout.write("<html>")
            fout.write("<head>")
            fout.write("<meta charset='utf-8'>")
            fout.write('<title>'+data['title']+'</title>')
            fout.write("</head>")
            fout.write("<body>")
            fout.write('<div class="main-content">')
            fout.write(data['miandiv'])
            fout.write("</div>")
            fout.write("<table>")
            fout.write("<tr>")
            fout.write("</tr>")
            fout.write("</table>")
            fout.write("</body>")
            fout.write("</html>")
            fout.close()
    
    
    
    
    
    



