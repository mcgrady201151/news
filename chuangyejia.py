#coding:utf-8

from common import *

def chuangyejia(url):
    page = urllib2.urlopen(url).read()
    print 'now crawl %s at %s' %(url,ctime())
    soup = BeautifulSoup(page) 
    links = soup.findAll('a')
    for link in links:
    	if link.has_key('alt') and link.has_key('title'):
    		regex = re.compile(r'img')
    		is_img = regex.findall(str(link))
    		if len(is_img) is not 0:
	            print link['href'],link['title']
	            flag = 'chuangyejia'
	            sql = "insert into dataset values(NULL,'%s','%s','%s')" %(link['title'],link['href'],flag)
	            p.runSql(sql)


