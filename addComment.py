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

last_row = ""
lines = []
 
with open(path+"comments.csv", 'r', newline='') as csvfile:
    reader  = csv.reader(csvfile)
    lines = list(reader)
    last_row = lines[-1] 
    
def insertComment(simplecomment={"id_User":"1","isbn":"1233214567","desc":"Good","rating":"5","review":"Very good book"},id="0"):
  with open(path+"comments.csv", 'a', newline='') as csvfile:
      commentwriter = csv.writer(csvfile)
      
      x = [id,simplecomment['id_User'],simplecomment['isbn'],simplecomment['desc'],simplecomment['rating'],simplecomment['review']]
      
      commentwriter.writerow(x)
      print("Added")
      
#insertComment(id=int(last_row[0])+1)
print(last_row)
for line in lines:
    print(line)