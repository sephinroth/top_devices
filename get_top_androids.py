#encoding=utf-8
#!/usr/bin/python

import codecs
import jieba
import json
import string
import urllib2

meta_data = json.loads(urllib2.urlopen('http://www.umindex.com/api/devices/summaries/models/android').read())
print "Date: %s" % meta_data['date']
print "Device type: %s" % meta_data['name']

details = meta_data['children']

x2 = {}
for brand_index in details:
    #print brand_index['name']
    if brand_index.has_key('children'):
        for device_key in brand_index['children']:
            if string.find(device_key['name'], u'其他') == -1:
                x2[device_key['name']] = device_key['value'] 

sorted_results = sorted(x2.items(), lambda x, y: cmp(x[1], y[1]), reverse=True) 

result_file = codecs.open('devices.log', 'w', 'utf-8')
for item in sorted_results:
    result_file.write(u"%s %s\n" % (item[0], item[1]))
result_file.close()

#print(", ".join(jieba.cut_for_search('酷派8720L')))
