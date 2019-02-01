import csv
import re

sampleComment = {'comment':[{
    'idRev' : 1,
    'id_User' : 0,
    'isbn' : '1632168146',
    'desc' : 'The best book',
    'rating' : 5,
    'review' : "Paul Nelson, a military veteran home from Korea, refuses to stand by and watch Kenneth Pittman, a young man he’s just met, get beat up by a group of teens. After a few chance encounters with Kenneth, Paul questions parts of his identity he’s been trying to suppress, and despite his struggles re-acclimating to civilian life and his personal fears, Paul finds the courage to ask Kenneth on a date. The two then begin a relationship. But in the 1950s, cultural and societal norms threaten openly gay men. Paul and Kenneth can only see each other in secret, and Paul’s new boss, a former investigative journalist and proud bigot, has a habit of meddling in his employees' lives. After tragedy strikes close to home, the two men question whether their slice of happiness is worth the trouble or if safety is more important. After vacationing together in Provincetown, a gay haven, to escape the chaos, they decide to stick it out, only to return to the consequences of being outed to everyone they know. Ultimately, Paul realizes the freedom he fought for should apply to them too, and he must bravely act in defiance of societys expectations to be with the man he loves."
}]
}

path = r'C:/Users/mdebosz/AppData/Local/Programs/Python/Python37-32/Scripts/project1/'
f = open(path+"comments.csv")
reader = csv.reader(f)

liblary = []

#ID_rev	User_ID	ISBN	Desc	Raing	Review

for ID_rev, User_ID, ISBN, Desc,Raing,Review in reader:
    liblary.append({'ID_rev':ID_rev,'User_ID':User_ID,'ISBN':ISBN,'Description':Desc,'Rating':Raing,'Review':Review})

def check(word,liblary):
    arrayOfTitle = []
    PrzedWord = '\w+' + word
    ZaWord = word + '\w+'
    for i in range(len(liblary)):
        if re.search(ZaWord,liblary[i]['ISBN'])!= None or re.search(PrzedWord,liblary[i]['ISBN'])!= None or re.search(word,liblary[i]['ISBN'])!= None:
            arrayOfTitle.append(liblary[i])
    return arrayOfTitle

def checkUser(word,liblary):
    arrayOfTitle = []
    for i in range(len(liblary)):
        if re.search(word,liblary[i]['User_ID'])!= None:
            arrayOfTitle.append(liblary[i])
    return arrayOfTitle    
    
#print(liblary)
#print(check('1632168146',liblary))
#print(checkUser('2',liblary))