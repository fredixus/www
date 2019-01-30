import csv
import re

path = r'C:/Users/mdebosz/AppData/Local/Programs/Python/Python37-32/Scripts/project1/'
f = open(path+"books.csv")
reader = csv.reader(f)

liblary = []

for isbn, title, author, year in reader:
    liblary.append({'isbn':isbn,'title':title,'author':author,'year':year})
    
#print(liblary)
#for row in liblary:
#    print(row)
    
#value = '0765317508'

def check(value,liblary):
    boolVal = False
    for i in range(len(liblary)):
        if liblary[i]['isbn']==value:
            boolVal = True
            return liblary[i]
        else:
            boolVal = False
    return boolVal
    
def checkTitle(word,liblary):
    arrayOfTitle = []
    word = word.lower()   
    PrzedWord = '\w+' + word
    ZaWord = word + '\w+'
    for i in range(len(liblary)):
        if re.search(ZaWord,liblary[i]['title'].lower())!= None or re.search(PrzedWord,liblary[i]['title'].lower())!= None or re.search(word,liblary[i]['title'].lower())!= None:
            #print(liblary[i])
            arrayOfTitle.append(liblary[i])
    return arrayOfTitle

def checkYear(word,liblary):
    arrayOfTitle = []
    word = word.lower()   
    PrzedWord = '\d+' + word
    ZaWord = word + '\d+'
    for i in range(len(liblary)):
        if re.search(ZaWord,liblary[i]['year'].lower())!= None or re.search(PrzedWord,liblary[i]['year'].lower())!= None or re.search(word,liblary[i]['year'].lower())!= None:
            #print(liblary[i])
            arrayOfTitle.append(liblary[i])
    return arrayOfTitle
         
def checkAuthor(word,liblary):
    arrayOfTitle = []
    word = word.lower()   
    PrzedWord = '\w+' + word
    ZaWord = word + '\w+'
    for i in range(len(liblary)):
        if re.search(ZaWord,liblary[i]['author'].lower())!= None or re.search(PrzedWord,liblary[i]['author'].lower())!= None or re.search(word,liblary[i]['author'].lower())!= None:
            #print(liblary[i])
            arrayOfTitle.append(liblary[i])
    return arrayOfTitle         
         
#print(check('1632168146',liblary))
#print(checkTitle('jaw',liblary))
#print(checkAuthor('Margaret Peterson Haddix',liblary))
#print(checkYear('1964',liblary))