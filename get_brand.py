#encoding=utf-8
#!/usr/bin/python

import codecs
import jieba

result_file = codecs.open('devices.log', 'r', 'utf-8')

for line in result_file:
    print line
