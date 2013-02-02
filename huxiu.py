#coding:utf-8

from common import *

def huxiu(url):
    page = urllib2.urlopen(url).read()
    print 'now crawl %s at %s' %(url,ctime())
    soup = BeautifulSoup(page) 
    links = soup.findAll('li')
    base_url = 'http://www.huxiu.com/'
    for link in links:
    	if link.has_key('class') and link['class'] == 'title-c':	
	        print link.a['href'],len(link.a.text)
	        flag = 'huxiu'
	        sql = "insert into dataset values(NULL,'%s','%s','%s')" %(link.a.text,base_url + link.a['href'],flag)
	        p.runSql(sql)




