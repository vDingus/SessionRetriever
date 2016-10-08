import numpy
import glob
import csv
import urllib

a = numpy.loadtxt('raw_download_urls.txt', delimiter=',', dtype='str')
c = a[:, 0]
d = c.tolist()
b = glob.glob("/users/Administrator/Desktop/VMworld2016/*.mp4")
e = [item.replace('/users/Administrator/Desktop/VMworld2016/','') for item in b]
f = [item.replace('.mp4','') for item in e]

#compare f and d
g = set(d)-set(f)
g = list(g)

for i in g:
	print "downloading %s" % i
	string1 = i+".mp4"
	string2 ="http://vstuff.org/VMworld2016-Vegas/"+string1
	print string2
	download = urllib.URLopener()
	download.retrieve(string2, string1)