#Program_27
#Grade of student

maths = int(input("Enter your score in Maths: "))
phy = int(input("Enter your score in Physics: "))
chem = int(input("Enter your score in Chemistry: "))
eng = int(input("Enter your score in English: "))
comp = int(input("Enter your score in Computer: "))

avg = (maths+phy+chem+eng+comp)/5

if(avg>=70):
    grade="A+(Distinction)"
    
elif(avg>=60 and avg<70):
    grade="A(I Div)"
    
elif(avg>=50 and avg<60):
    grade="B(II Div)"
    
elif(avg>=33 and avg<50):
    grade="C(III Div)"
    
else:
    grade="D(Fail)"

print(grade)
