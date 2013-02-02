#coding:utf-8
from threading import Thread
from Queue import Queue
from time import sleep
import urllib2
from PyMySQL import PyMySQL
from BeautifulSoup import BeautifulSoup
import re
import _36kr
import leiphone
import yueguang
import ithome
import internet2share
import chuangyejia
import huxiu

NUM = 7

q = Queue()

def working():
    while True:
        url = q.get()
        regex_kr = re.compile(r'kr')
        regex_yueguang = re.compile(r'williamlong')
        regex_ithome = re.compile(r'ithome')
        regex_chuangyejia = re.compile(r'chuangyejia')
        regex_huxiu = re.compile(r'huxiu')
        regex_leiphone = re.compile(r'leiphone')
        regex_internet2share = re.compile(r'internet2share')

        if len(regex_kr.findall(url)) > 0:
            _36kr._36kr(url)
            print 'sleep 3 sec'
            sleep(3)
            q.task_done()

        elif len(regex_leiphone.findall(url)) > 0:
            leiphone.leiphone(url)
            print 'sleep 3 sec'
            sleep(3)
            q.task_done()

        elif len(regex_yueguang.findall(url)) > 0:
            yueguang.yueguang(url)
            print 'sleep 3 sec'
            sleep(3)
            q.task_done()

        elif len(regex_ithome.findall(url)) > 0:
            ithome.ithome(url)
            print 'sleep 3 sec'
            sleep(3)
            q.task_done()

        elif len(regex_chuangyejia.findall(url)) > 0:
            chuangyejia.chuangyejia(url)
            print 'sleep 3 sec'
            sleep(3)
            q.task_done()

        elif len(regex_huxiu.findall(url)) > 0:
            huxiu.huxiu(url)
            print 'sleep 3 sec'
            sleep(3)
            q.task_done()

        elif len(regex_internet2share.findall(url)) > 0:
            internet2share.internet2share(url)
            print 'sleep 3 sec'
            sleep(3)
            q.task_done()
   
for i in range(NUM):
    t = Thread(target=working)
    t.setDaemon(True)
    t.start()

id = 115
while id < 200:
    yueguang_url = 'http://www.williamlong.info/cat/?page=' + str(id)
    ithome_url = 'http://it.ithome.com/category/1_' + str(id) + '.html'
    huxiu_url = 'http://www.huxiu.com/focus/?more=1&page=' + str(id)
    _36kr_url = 'http://www.36kr.com/?page=' + str(id)
    leiphone_url = 'http://www.leiphone.com/page/' + str(id)
    if id < 115:
        chuangyejia_url = 'http://www.chuangyejia.com/page/' + str(id)
        q.put(chuangyejia_url)
    if id < 30:
        internet2share_url = 'http://www.internet2share.com/archives/category/lnews/page/' + str(id) 
        q.put(internet2share_url)
    q.put(yueguang_url)
    q.put(_36kr_url)
    q.put(leiphone_url)
    q.put(ithome_url)
    q.put(huxiu_url)
    
    id += 1
        
q.join()
print'crawl done!'

