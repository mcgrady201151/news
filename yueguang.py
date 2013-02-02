#coding:utf-8

from common import *

def yueguang(url):
    page = urllib2.urlopen(url).read()
    print 'now crawl %s at %s' %(url,ctime())
    soup = BeautifulSoup(page) 
    links = soup.findAll('a')
    for link in links:
	    if link.has_key('rel') and link['rel'] == 'bookmark':
		    print link['href'],len(link.text)
		    flag = 'yueguang'
		    sql = "insert into dataset values(NULL,'%s','%s','%s')" %(link.text,link['href'],flag)
		    p.runSql(sql)


