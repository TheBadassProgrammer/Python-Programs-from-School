#Calculating gross and net salary.

bs=int(input("Enter your basic salary: "))

if(bs<5000):
       hra = bs*0.06
       da = bs*0.05
       pf = bs*0.03
       lic = bs*0.01
       gross = bs + hra + da
       net = bs + hra + da - (pf + lic)
       print("Your gross salary is: ", gross)
       print("Your net salary is: ", net)
       
elif(bs>=5000)and(bs<10000):
       hra = bs*0.08
       da = bs*0.07
       pf = bs*0.05
       lic = bs*0.02
       gross = bs + hra + da
       net = bs + hra + da - (pf + lic)
       print("Your gross salary is: ", gross)
       print("Your net salary is: ", net)
      
elif(bs>=10000):
       hra = bs*0.12
       da = bs*0.09
       pf = bs*0.06
       lic = bs*0.03
       gross = bs + hra + da
       net = bs + hra + da - (pf + lic)
       print("Your gross salary is: ", gross)
       print("Your net salary is: ", net)
       

