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
print ("--- Q1 test ---")
# test 1
print (">>> countPos([1, 3, 5, -5, -3, -1])")
print (countPos([1, 3, 5, -5, -3, -1]))
# test 2
print (">>> num = countPos([6, 4, 2, 0])")
print (">>> num")
num = countPos([6, 4, 2, 0])
print (num)
# test 3
print (">>> countPos([3.1415, 2.178, -3.333, 17.159, 0.11])")
print (countPos([3.1415, 2.178, -3.333, 17.159, 0.11]))
# test 4
print (">>> countPos([-1, -2, -3])")
print (countPos([-1, -2, -3]))
# test 5
print (">>> countPos([])")
print (countPos([]))
print (">>> \n")


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
print ("--- Q2 test ---")
# test 1
print (">>> censorNum('1, 2, 3, blast off!')")
print (censorNum('1, 2, 3, blast off!'))
# test 2
print ('>>> censorNum("My favourite number is 17.")')
print (censorNum("My favourite number is 17."))
# test 3
print ('>>> censorNum("This is a test. This is only a test.")')
print (censorNum("This is a test. This is only a test."))
# test 4
print (">>> censorNum('')")
print (censorNum(''))
# test 5
print ('>>> censorNum("12345")')
print (censorNum("12345"))
print ('>>>> \n')


         
# Question 3
def apr(info):
    print(info.split())
    name = info.split()[0]
    num = info.split()[1]
    grade = info.split()[2]
    lv = grade[0].upper()
    if lv in ('A','B') :
        print ('Congratulations, you are doing well in', name, num + '!')
    elif lv in ('C') :
        print('You are passing',name, num + '.')
    elif lv in ('D', 'F') :
        print('You need to improve your performance in', name, num + '.')
    else :
        print('An invalid grade for', name, num, 'was provided.')

# Q3 test
print ("--- Q3 test ---")
# test 1
#print(">>> apr('CSC  241    A-')")
apr('CSC      241    A-')
# test 2
#print ('>>> apr("CSC  242    c")')
apr("CSC  242    c")
# test 3
#print ('>>> apr("CSC     373       d+")')
apr("CSC     373       d+")
# test 4
#print (">>> apr('WRD 104 B+')")
apr('WRD 104 B+')
# test 5
#print (">>> apr('IT 130    f')")
apr('IT    130    f')
# test 6
print (">>> apr('CSC 241 E')")
apr('CSC 241 E')
print (">>> \n")


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

# Q4 test
print ("--- Q4 test ---")
# test 1
print (">>> sentenceCount('csc241midterm/test1.txt')")
print (sentenceCount('csc241midterm/test1.txt'))
# test 2
print (">>> num = sentenceCount('csc241midterm/test2.txt')")
print (">>> num")
num = sentenceCount('csc241midterm/test2.txt')
print (num)
# test 3
print (">>> sentenceCount('csc241midterm/empty.txt')")
print (sentenceCount('csc241midterm/empty.txt'))
print (">>> \n")
