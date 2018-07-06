'''
**************************
Author: Yibing Zhang
Email:yibing1031@gmail.com
**************************
This file is used to generate train dataset and test dataset(split the data generated manually) from the database.
If you already have dataset following the format of my train data file, you don't need to use this file.y
'''

'''
Input:HTML
Output Labels:
O
SUBJECT:
B-
I-
CONDITION:
B-
I-
BEHAVIOR:
B-
I-
RESULT:
B-
I-
KEY:
B-
I-
FORBIDDEN:
B-
RIGHT:
B-
OBLIGATION:
B-

''' 

import pymysql
import re
import jieba
import sys
import os

jieba.load_userdict("dict.txt")
def readAndSplit(filePath):
    events=[]
    pat='<span class="label-event'
    skiplen=len('<span class="label-event3 label">。<img class="close-image" alt="" src="/lekg/images/close.png"></span>')
    with open(filePath,'r',encoding="UTF-8") as f:
        items=f.readlines()
        for item in items:
            i=0
            pre=0
            while True:
                i=item.find(pat,i)
                if i==-1:
                    break;
                i=i+skiplen
                events.append(item[pre:i].strip())
                pre=i
    return events

                

def Segment(sen):
    words=jieba.lcut(sen)
    return words

def writeTsv(outPutTsv,sentence,label):
    words=Segment(sentence)
    if label=="O":
        for i in range(len(words)):
            outPutTsv.write(words[i] + u"\t" +label+ u"\n")
        return
    for i in range(len(words)):
        if i==0:
            outPutTsv.write(words[i] + u"\t" + "B-" +label+ u"\n")
        else:
            outPutTsv.write(words[i] + u"\t" + "I-" +label+ u"\n")
    

def extractLabel(s):
    if s.find('subject')!=-1:
        return 'SUBJECT'
    elif s.find('author')!=-1:
        return 'CONDITION'
    elif s.find('object')!=-1:
        return 'BEHAVIOR'
    elif s.find('power')!=-1:
        return 'RESULT'
    elif s.find('condition')!=-1:
        return 'KEY'
    elif s.find('event1')!=-1:
        return 'FORBIDDEN'
    elif s.find('event2')!=-1:
        return 'RIGHT'
    elif s.find('event3')!=-1:
        return 'OBLIGATION'
    else:
        return 'WTF'
def SegmentAndOutput(filePath,outPutTsv):
    htmlevents=readAndSplit(filePath)
    with open(outPutTsv,'w',encoding='UTF-8') as outfile:
        for eve in htmlevents:
            label='O'
            cur=0
            i=0
            nextp=0
            while i<len(eve):
                if eve[i]=='<':
                    cur=i
                    nextp=i
                    if eve[i+1:i+5]=='span':
                        label=extractLabel(eve[i+len('<span class="label-'):i+len('<span class="label-')+10])
                        while eve[cur]!='>' and cur<len(eve):
                            cur+=1
                        cur+=1
                        nextp=cur
                        while eve[nextp]!='<' and nextp<len(eve):
                            nextp+=1
                        writeTsv(outfile,eve[cur:nextp],label)
                        i=nextp
                    else:
                        label='O'
                        while eve[i]!='>':
                            i+=1
                        i+=1
                else:
                    cur=i
                    nextp=i
                    while eve[nextp]!='<' and nextp<len(eve):
                        nextp+=1
                    writeTsv(outfile,eve[cur:nextp],label)
                    i=nextp
            outfile.write(u"\n")

    return







def get_full_address():
    #conn = pymysql.connect(host="192.3333.234234.324", port=33044, user="root", password="23333333", db="flfgk", charset='utf8')  #connect your own database!
    with conn.cursor() as cursor:
        sql = "select labelvalue from lawitemlabel where label = 'CRF'"
        cursor.execute(sql)
        records = cursor.fetchall()
    return records



#SegmentAndOutput(jjj,kkk)
res=get_full_address()
with open("./htmlfile.txt",'w',encoding='UTF-8') as outfile:
    for s in res:
        outfile.write(s[0]+u'\n')

SegmentAndOutput("./htmlfile.txt","./Trainfile")