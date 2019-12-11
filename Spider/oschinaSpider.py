import requests
from bs4 import BeautifulSoup
from lxml import etree

class CsdnSpider(object):
    def __init__(self):
        self.count=10
        self.restullist=[]
        self.header={
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
        }


    def start_request(self,keyword,count):
        self.count = count
        for i in  range(1,100):
            if len(self.restullist)>=self.count:
                break
            response=requests.get("https://www.oschina.net/search?scope=blog&q="+keyword+"&p="+str(i),headers=self.header)
            selector = etree.HTML(response.text)
            self.parse(selector)




    def parse(self,response):

        list1=response.xpath('//div[@class="search-list"]/div/div/div[@class="item"]/div')

        for info in list1:
            title=info.xpath("./h3/a")[0].xpath("string(.)")

            url=info.xpath("./h3/a/@href")[0]


            dict1={}
            other=info.xpath("./div[@class='extra']/div/div")

            author=other[0].xpath("./a")[0].xpath("string(.)")
            create_time=other[1].xpath("string(.)")
            response=requests.get(url,headers=self.header)
            soup=BeautifulSoup(response.text,'html.parser')
            info=str(soup.find("div",id="articleContent"))
            dict1['title']=title.strip().split("原")[0].strip()

            dict1['url']=url.strip()
            dict1['author']=author.strip()
            dict1['create_time']=create_time.strip()
            dict1['content']=info.strip()
            self.restullist.append(dict1)
            if len(self.restullist)>=self.count:
                break









