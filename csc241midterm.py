# CSC 241-404
# Midterm exam template
# Qili Sui

# You DO NOT have to write doc strings

# Question 1
def countPos(lst):
    count=0
    for i in lst:
        if i<=0:
            pass
        elif i>0:
            count=count+1
        elif len(lst)==0:
            count = 0
    return count
# Q1 test
print (countPos([1,3,5,-5,-3,-1]))
num = countPos([6, 4, 2, 0])
print (num)
print (countPos([3.1415, 2.178, -3.333, 17.159, 0.11]))
print (countPos([-1, -2, -3]))
print (countPos([]))

# Question 2
def censorNum(s):
    if(len(s)==0):
            pass
    s1 = ''
    for i in s:
        if i in "1234567890":
            i = '*'
        s1 = s1 + i
    return(s1)
# Q2 test
print (censorNum('1,2,3,blast off!'))
print (censorNum("My favourite number is 17."))
print (censorNum("This is a test. This is only a test."))
print (censorNum(''))
print (censorNum("12345"))
            
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
