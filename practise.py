#ANSWER-1
""" 
def nthRoot(x,n):
    return (x**(1/n))

print(nthRoot(625,4))
 """

 #ANSWER-2
"""  
def special(st):
    if st[0]==st[len(st)-1]:
        return True
    else:
        return False

print(special("nitin")) """

#ANSWER-3
""" 
import random
print(int(20+random.random()*5), end=' ')
print(int(20+random.random()*5), end=' ')
print(int(20+random.random()*5), end=' ')
print(int(20+random.random()*5), end=' ') 
#lowest value = 20, highest value = 24 """

#ANSWER-4
""" 
c=12
def add():
    global c
    c+=2
    print("inside:",c)
add()
c=18
print("in Main:",c) """

#ANSWER-5
""" 
d = {0:'a',1:'b',2:'c'}
for x in d.values():
    print(d[x])
#KeyError """

#ANSWER-6&7
""" 
inv="Anuj_Astha"
p=200
l=1
def play():
    m_l = l+10
    print(len(inv)==0)
    return m_l
res=play()
print(res) """

#ANSWER-10
""" 
def myfun(st):
    rst=''
    l=len(st)
    while(l>0):
        if (st[l-1].isalpha()):
            rst+=st[l-1]
        l=l-1
    return rst
print(myfun("123Anuj")) """

#ANSWER-13
""" 
import os
cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directory
print("Files in %r: %s" % (cwd, files))

fh = open("nitin.txt", "r")
lines = fh.readlines()
for line in lines:
    print(line)
 """

#ANSWER-14
""" 
fh = open("nitin.txt", "r")
words = []
lines = fh.readlines()

for line in lines:
    temp = line.rstrip("\n").split()
    words += temp

for word in words:
    if len(word)<4:
        print(word) """

#ANSWER-15
""" 
fh = open("nitin.txt", "r")
words = []
lines = fh.readlines()
count = 0

for line in lines:
    temp = line.rstrip("\n").split()
    words += temp

for word in words:
    if word=="India":
        count += 1

print(count) """


