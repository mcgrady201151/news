#coding:utf-8

from common import *

def _36kr(url):   
    page = urllib2.urlopen(url).read()
    print 'now crawl %s at %s' %(url,ctime())
    soup = BeautifulSoup(page)
    links = soup.findAll('a')
    for link in links:
        if link.has_key('data-no-turbolink') and link.has_key('title') and not link.has_key('rel'):
            print link['href'],link['title']
            base_url = 'http://www.36kr.com'
            flag = '36kr'
            sql = "insert into dataset values(NULL,'%s','%s','%s')" %(link['title'],base_url + link['href'],flag)
            p.runSql(sql)
		