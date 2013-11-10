#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""    version 1.0	"""
import urllib,urllib2
import sqlite3
import re

def main():
    db = sqlite3.connect('nku.db')
    db.text_factory = str 
    cur = db.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS class (b_name TEXT,r_name TEXT,start INT,end INT,day_num INT,day_time TEXT)''')
    url = "http://222.30.32.3/apps/xksc/index.asp"
    req = urllib2.Request(url)
    for i in range(100,141):
        print i
        post = urllib.urlencode([('Page',i)])
        fd = urllib2.urlopen(req,post)
        data = fd.read()
        start = data.find('<TABLE  width=100% height=50% >')
        data = data[start:]
        end = data.find('</TABLE>')
        data = data[:end]
        tr = data.split('</TR><TR>')
        for j in range(20):
            td = tr[j+1].split('</TD><TD>')
            #\xb6\xfe\xd6\xf7\xc2\xa5---erzhulou
            #\xc8\xfd\xbd\xcc---sanjiao
            #\xc6\xdf\xbd\xcc---qijiao
            day_num = td[6]
            day_time = daytime(td[7])
            week_start = td[8][:td[8].find('~')]
            week_end = td[8][td[8].find('~')+1:]
            name = td[9].decode('gbk').encode('utf-8')
            pat = '[0-9]+'
            if len(re.findall(pat,name))>0:
                b_name = name[:name.find(re.findall(pat,name)[0])]
                r_name = name[len(b_name):]
            else:
                b_name = name
                r_name = ''
            query = 'INSERT INTO class  VALUES (?,?,?,?,?,?)'
            cur.execute(query,(b_name,r_name,week_start,week_end,day_num,day_time))
            db.commit()
            #print r_name,b_name,week_start,week_end,day_num,day_time
#9/10/11  -->  '5,6'
def daytime(text):
    result = []
    info = text.split('/')
    for ii in range((len(info)-1)/2+1):
        if info[0]=='a' or info[0]=='A':
            result.append('1')
        elif info[0]=='c' or info[0]=='C':
            result.append('2')
        elif info[0]=='e' or info[0]=='E':
            result.append('3')
        elif info[0]=='g' or info[0]=='G':
            result.append('4')
        elif info[0]=='i' or info[0]=='I':
            result.append('5')
        elif info[0]=='k' or info[0]=='K':
            result.append('6')
        else:
            result.append(str((int(info[ii*2])+1)/2))
    return ','.join(result)

if __name__=='__main__':
    main()
