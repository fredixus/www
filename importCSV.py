import csv
import re

path = r'C:/Users/mdebosz/AppData/Local/Programs/Python/Python37-32/Scripts/project0/'
f = open(path+"books.csv")
reader = csv.reader(f)

liblary = []

for isbn, title, author, year in reader:
    liblary.append({'isbn':isbn,'title':title,'author':author,'year':year})

#print(liblary)
#for row in liblary:
#    print(row)

#value = '0765317508'

def check(word,liblary):
    arrayOfTitle = []
    PrzedWord = '\w+' + word
    ZaWord = word + '\w+'
    for i in range(len(liblary)):
        if re.search(ZaWord,liblary[i]['isbn'])!= None or re.search(PrzedWord,liblary[i]['isbn'])!= None or re.search(word,liblary[i]['isbn'])!= None:
            arrayOfTitle.append(liblary[i])
    return arrayOfTitle

def checkSingle(word,liblary):
    #single ISBN
    boolVal = False
    for i in range(len(liblary)):
        if liblary[i]['isbn']==word:
            boolVal = True
            return [liblary[i]]
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
            arrayOfTitle.append(liblary[i])
    return arrayOfTitle

def checkTitleAndAuthor(word,word2,liblary):
    arrayOfTitle = []
    word = word.lower()
    PrzedWord = '\w+' + word
    ZaWord = word + '\w+'

    word2 = word2.lower()
    PrzedWord2 = '\w+' + word2
    ZaWord2 = word2+ '\w+'

    for i in range(len(liblary)):
        if re.search(ZaWord,liblary[i]['title'].lower())!= None or re.search(PrzedWord,liblary[i]['title'].lower())!= None or re.search(word,liblary[i]['title'].lower())!= None:
            if re.search(ZaWord2,liblary[i]['author'].lower())!= None or re.search(PrzedWord2,liblary[i]['author'].lower())!= None or re.search(word2,liblary[i]['author'].lower())!= None:
                arrayOfTitle.append(liblary[i])
    return arrayOfTitle

def checkIsbnAndAuthor(word,word2,liblary):
    arrayOfTitle = []
    word = word.lower()
    PrzedWord = '\w+' + word
    ZaWord = word + '\w+'

    word2 = word2.lower()
    PrzedWord2 = '\w+' + word2
    ZaWord2 = word2+ '\w+'

    for i in range(len(liblary)):
        if re.search(ZaWord,liblary[i]['isbn'].lower())!= None or re.search(PrzedWord,liblary[i]['isbn'].lower())!= None or re.search(word,liblary[i]['isbn'].lower())!= None:
            if re.search(ZaWord2,liblary[i]['author'].lower())!= None or re.search(PrzedWord2,liblary[i]['author'].lower())!= None or re.search(word2,liblary[i]['author'].lower())!= None:
                arrayOfTitle.append(liblary[i])
    return arrayOfTitle
    
def checkIsbnAndTitle(word,word2,liblary):
    arrayOfTitle = []
    word = word.lower()
    PrzedWord = '\w+' + word
    ZaWord = word + '\w+'

    word2 = word2.lower()
    PrzedWord2 = '\w+' + word2
    ZaWord2 = word2+ '\w+'

    for i in range(len(liblary)):
        if re.search(ZaWord,liblary[i]['isbn'].lower())!= None or re.search(PrzedWord,liblary[i]['isbn'].lower())!= None or re.search(word,liblary[i]['isbn'].lower())!= None:
            if re.search(ZaWord2,liblary[i]['title'].lower())!= None or re.search(PrzedWord2,liblary[i]['title'].lower())!= None or re.search(word2,liblary[i]['title'].lower())!= None:
                arrayOfTitle.append(liblary[i])
    return arrayOfTitle
    
def checkAll(word,word2,word3,liblary):
    arrayOfTitle = []
    word = word.lower()
    PrzedWord = '\w+' + word
    ZaWord = word + '\w+'

    word2 = word2.lower()
    PrzedWord2 = '\w+' + word2
    ZaWord2 = word2+ '\w+'
    
    word3 = word3.lower()
    PrzedWord3 = '\w+' + word3
    ZaWord3 = word3+ '\w+'

    for i in range(len(liblary)):
        if re.search(ZaWord,liblary[i]['isbn'].lower())!= None or re.search(PrzedWord,liblary[i]['isbn'].lower())!= None or re.search(word,liblary[i]['isbn'].lower())!= None:
            if re.search(ZaWord2,liblary[i]['author'].lower())!= None or re.search(PrzedWord2,liblary[i]['author'].lower())!= None or re.search(word2,liblary[i]['author'].lower())!= None:
                if re.search(ZaWord3,liblary[i]['title'].lower())!= None or re.search(PrzedWord3,liblary[i]['title'].lower())!= None or re.search(word3,liblary[i]['title'].lower())!= None:
                    arrayOfTitle.append(liblary[i])
    return arrayOfTitle
    
def checkYear(word,liblary):
    arrayOfTitle = []
    word = word.lower()
    PrzedWord = '\d+' + word
    ZaWord = word + '\d+'
    for i in range(len(liblary)):
        if re.search(ZaWord,liblary[i]['year'].lower())!= None or re.search(PrzedWord,liblary[i]['year'].lower())!= None or re.search(word,liblary[i]['year'].lower())!= None:
            arrayOfTitle.append(liblary[i])
    return arrayOfTitle

def checkAuthor(word,liblary):
    arrayOfTitle = []
    word = word.lower()
    PrzedWord = '\w+' + word
    ZaWord = word + '\w+'
    for i in range(len(liblary)):
        if re.search(ZaWord,liblary[i]['author'].lower())!= None or re.search(PrzedWord,liblary[i]['author'].lower())!= None or re.search(word,liblary[i]['author'].lower())!= None:
            arrayOfTitle.append(liblary[i])
    return arrayOfTitle

#print(check('1632168146',liblary))
#print(checkTitle('jaw',liblary))
#print(checkAuthor('Margaret Peterson Haddix',liblary))
#print(checkYear('1964',liblary))
