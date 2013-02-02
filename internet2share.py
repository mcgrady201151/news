#coding:utf-8

from common import *

def internet2share(url):
    page = urllib2.urlopen(url).read()
    print 'now crawl %s at %s' %(url,ctime())
    soup = BeautifulSoup(page) 
    links = soup.findAll('h2')
    for link in links:
	    print link.a['href'],len(link.a.text)
	    flag = 'internet2share'
	    sql = "insert into dataset values(NULL,'%s','%s','%s')" %(link.a.text,link.a['href'],flag)
	    p.runSql(sql)


