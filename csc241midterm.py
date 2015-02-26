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
"""            
# Question 3
def apr(info):
    for i in range(len(info)):
        if info[i] == ' ' and info[i+1] in '0123456789':
            no = info[i+1]+info[i+2]+info[i+3]
        if (info[-1:]=='A' or info[-1:]=='a' or info[-1:]=='B' or info[-1:]=='b' 
            or info[-2:]=='A+' or info[-2:]=='a+' or info[-2:]=='A-' or info[-2:]=='a-'
            or info[-2:]=='B+' or info[-2:]=='b+' or info[-2:]=='b-' or info[-2:]=='B-'):
            print('Congratulations, you are doing well in',info[0:3],no+'!')

        elif (info[-1:]=='C' or info[-1:]=='c' or info[-2:]=='C+' or info[-2:]=='c+' 
            or info[-2:]=='C-' or info[-2:]=='c-'):
            print('You are passing',info[0:3],no+'.')

        elif(info[-1:]=='D' or info[-1:]=='d' or info[-1:]=='F' or info[-1:]=='f' 
            or info[-2:]=='D+' or info[-2:]=='d+' or info[-2:]=='D-' or info[-2:]=='d-'):
            print('You need to improve your performance in',info[0:3],no+'.')

        else:
            print('An invalid grade for',info[0:3],no,'was provided.')

print(apr('CSC      241    A-'))
print(apr("CSC  242    c"))
print(apr("CSC     373       d+"))
print(apr('WRD 104 B+'))
print(apr('IT    130    f'))
print(apr('CSC 241 E'))
"""
# Question 4
def sentenceCount(fname):
    inf=open(fname,'r')
    con=inf.read()
    inf.close()

    count = 0
    if len(con) == 0 :
        return (count) 
    j = ''
    for i in con:
        if i in ('!?'):
            count =  count + 1
        elif j in ('.') and i in ('\n'):
            count = count + 1
        j = i
    return (count)

print (sentenceCount('csc241midterm/test1.txt'))
num = sentenceCount('csc241midterm/test2.txt')
print (num)
print (sentenceCount('csc241midterm/empty.txt'))

