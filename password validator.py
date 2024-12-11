from tokenize import Special


string = "Adbh90@,af JG2##9,2Weehdjgj"
allowed = ["#", "@", "$"]
lst = string.split(",")
new_lst = []

for word in lst:
    capital_count = 0
    small_count = 0
    number_count = 0
    special_char_count = 0
    if (word.isupper() or word.islower() or len(word)<6 or len(word)>12):
        continue
    else:
        for char in word:
            o = ord(char)
            if (o>=65 and o<=90):
                capital_count =+1
            elif(o>=97 and o<=122):
                small_count =+1
            elif(o>=48 and o<=57):
                number_count =+1
            elif char in allowed:
                special_char_count =+ 1
            else:
                break
            
    
    if small_count>0 and capital_count>0 and number_count>0 and special_char_count>0:
        new_lst.append(word)

print(new_lst)
        
            
    
        
