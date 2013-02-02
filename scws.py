# -*- coding: utf-8 -*-
#encode:utf-8
import urllib2,urllib,json

def seg(sentence):
    post_data = {'data':sentence,'respond':'json','ignore':'yes'}
    post_data = urllib.urlencode(post_data)
    url = 'http://www.xunsearch.com/scws/api.php'
    f = urllib2.urlopen(url,post_data)
    result = json.loads(f.read())
    words = result['words']
    wordlist = list()
    idflist = list()
    for w in words:
    	wordlist.append(w['word'])
    	idflist.append(w['idf'])
        #return w['word'].encode('utf-8'),w['idf']
    return wordlist,idflist

def tagCount(tags):
	tagfreq = {}
	for tag in tags:
		if tag not in tagfreq:
			tagfreq[tag] = 1
		else:
		    tagfreq[tag] += 1
	return tagfreq
#sentence = "我爱你北京"
#seg(sentence)
#print "\xe6\x83\x9f"