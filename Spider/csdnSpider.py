import requests
from bs4 import BeautifulSoup
from lxml import etree

class CsdnSpider(object):
    def __init__(self):
        self.count=10
        self.restullist=[]


    def start_request(self,keyword,count):
        self.count = count
        for i in  range(1,100):
            if len(self.restullist)>=self.count:
                break
            response=requests.get("https://so.csdn.net/so/search/s.do?p="+str(i)+"&q="+keyword)
            selector = etree.HTML(response.text)
            self.parse(selector)




    def parse(self,response):

        list1=response.xpath('//div[@class="search-list-con"]/dl[@class="search-list J_search"]')
        for info in list1:
            other=info.xpath("./dt")[0]
            type=other.xpath("./span")[0].xpath("string(.)")
            if type.strip()=="博客":
                dict1={}
                url=other.xpath("./div/a/@href")[0]
                title=other.xpath("./div/a")[0].xpath("string(.)")
                author=info.xpath("./dd/span/a")[0].xpath("string(.)")
                create_time=info.xpath("./dd/span")[1].xpath("string(.)").split("：")[1]
                response=requests.get(url)
                soup=BeautifulSoup(response.text,'html.parser')
                info=str(soup.find("div",id="article_content"))
                dict1['title']=title
                dict1['url']=url
                dict1['author']=author
                dict1['create_time']=create_time
                dict1['content']=info
                self.restullist.append(dict1)
                if len(self.restullist)>=self.count:
                    break







if __name__=="__main__":
    csdn =CsdnSpider()
    csdn.start_request("java语言",10)
    print(csdn.restullist)


