# -*- coding: utf-8 -*-
"""
Created on Wed May  5 19:13:47 2021

@author: Noa Mor
"""

##יצירת רשימת טקסטים לפי שורות
def fileToList (file):
    textList= []
    for line in file:
        line=line.rstrip()
        textList.append(line)
    return textList


##הוספת שורות בודדות להודעה הרלוונטית
def fixText (textList):
    numOfLine= 0
    for text in textList:
        text=str(text)
        count = text.count(":")
        if count==0:
            textList[numOfLine-1]= textList[numOfLine-1]+' ' +text
        numOfLine+= 1
    return textList


##מציאת כותב ההודעה והוספה למילון לפי אינדקס
def idDict (textList):
    idWriter= {}
    for text in textList:
        text=str(text)
        count = text.count(":")
        if count>1:
            writer=str(text.split('-')[1:]).split(':')[0]
            idWriter[writer]=idWriter.get(writer,len(idWriter)+1)
    return idWriter


## יצירת רשימת מילונים, ופירוק הטקסט לשעה, כותב מתוך המילון, וטקסט
def textData (textList, idWriter):
    listMessengeData= []
    for text in textList:
        text=str(text)
        count = text.count(":")
        if count>1:
            messengeData={}
            datetime=text.split(' - ')[0].replace('.','-').replace(',','')
            writerId=idWriter[str(text.split('-')[1:]).split(':')[0]]
            textMessege=text.split(': ')[1]
            messengeData['datetime']=datetime
            messengeData['id']=writerId
            messengeData['text']=textMessege
            listMessengeData.append(messengeData)
    return listMessengeData


## מציאת פרטי הקמת קבוצה
def groupData (textList, idWriter):
    metadata={}
    for text in textList:
        text=str(text)
        if 'הקבוצה' in text:
            chat_name= text.split('"')[1]
            creation_date= text.split(' - ')[0].replace('.','-').replace(',','')
            num_of_participants= len(idWriter)
            creator= text.split('נוצרה על ידי ')[1]
            metadata['chat_name']=chat_name
            metadata['creation_date']=creation_date
            metadata['num_of_participants']=num_of_participants
            metadata['creator']=creator
    return metadata


##איחד המילון והרשימה
def allData (listMessengeData, metadata):
    totalData={}
    totalData['messages']=listMessengeData
    totalData['metadata']=metadata
    return totalData


## ג'ייסון
def makeJson (totalData):
    import json
    file= totalData['metadata']['chat_name']+".txt"
    with open(file,'w',encoding='utf8') as file:
        json.dump(totalData, file, ensure_ascii=False, indent= 4)


##קליטת קובץ
file=open("�צאט WhatsApp עם יום הולדת בנות לנויה.txt" ,encoding='utf-8')
##המרת הנתונים לקובץ ג'ייסון ב5 שלבים נפרדים
step1= fileToList(file)
step2= fixText(step1)
step3= idDict(step2)
step4= allData(textData(step2,step3),groupData(step2,step3))
step5= makeJson(step4)

##קליטת קובץ בונוס
##file=open("�צ'אט WhatsApp עם יום הולדת לשקד הפתעה.txt" ,encoding='utf-8')
##המרת הנתונים לקובץ ג'ייסון ב5 שלבים נפרדים
##step1= fileToList(file)
##step2= fixText(step1)
##step3= idDict(step2)
##step4= allData(textData(step2,step3),groupData(step2,step3))
##step5= makeJson(step4)