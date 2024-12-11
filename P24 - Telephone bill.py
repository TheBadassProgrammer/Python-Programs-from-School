#Program_24
#Print telephone bill.

calls = int(input("Enter the number of calls: "))

if (calls<=100):
    charge = calls*0
    amount = charge + 500
    net = amount*1.18

elif (100<=calls<200):
    calls = calls-100
    charge = calls*0.5
    amount = charge + 500
    net = amount*1.18

elif (200<=calls<300):
    charge = (calls-200)*0.75+50
    amount = charge + 500
    net = amount*1.18

elif (300<=calls<400):
    charge = (calls-300)*1+75+50
    amount = charge + 500
    net = amount*1.18

elif (calls>400):
    charge = (calls-400)*1.5+100+75+50
    amount = charge + 500
    net = amount*1.18

print("Net payable amount is: ", net)
