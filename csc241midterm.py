# CSC 241-404
# Midterm exam template
# Qili Sui

# You DO NOT have to write doc strings

# Question 1
def countPos(lst):
    count=0
    for i in lst:
        if i<=0:
            count = 0
        elif i>0:
            count=count+1
        elif len(lst)==0:
            count = 0
    return count

# Question 2
def censorNum(s):
    for i in s:
        if i in ('1234567890'):
            for i in s:
                temp=s.replace(i,'*')
            print(temp)
        elif(len(s)==0):
            pass
        elif i not in ('1234567890'):
            print(s)
        
            
# Question 3
def apr(info):
    apr.split(" ")
    listG=['A','A+','A-','B','B+','B-','a','a+','a-','b','b+','b-']
    listP=['C','C+','C-','c','c+','c-']
    lsitF=['D','D+','D-','F','f','d+','d-','d']
    for i in apr:
        if apr[-2:] in listG:
            for i in ('01234567890'):
                print('Congratulations, you are doing well in',apr[:4],i,"!")
        elif apr[-2:] in listP:
            for i in ('01234567890'):  
                print('You are passing',apr[:4],i,'.')
        elif apr[-2:] in listF:
            for i in ('01234567890'):  
                print('You need to improve your performance in',apr[:4],i,'.')
        else:
            for i in ('01234567890'):  
                print('An invalid grade for … was provided.',apr[:4],i,'.')

# Question 4
def sentenceCount(fname):
    inf=open(fname,'r')
    con=inf.read()
    inf.close()

    for i in con:
        if i in( '.!?'):
            p=con.split(".")
            temp1=p.split("!")
            temp2=temp1.split("?")
            temp3=temp2.split("\n")
        len(temp3)
